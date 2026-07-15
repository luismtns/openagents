#!/usr/bin/env python3
"""Validate the OpenAgents v2 package using only the Python standard library."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILLS = {"openagents", "openagents-handoff", "openagents-doctor"}
REQUIRED = {
    "README.md",
    "AGENTS.md",
    "CHANGELOG.md",
    "LICENSE",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "SUPPORT.md",
    "CODE_OF_CONDUCT.md",
    "skills.sh.json",
    "skillfish.json",
    "package.json",
    "skills/openagents/SKILL.md",
    "skills/openagents/references/status.md",
    "skills/openagents-handoff/SKILL.md",
    "skills/openagents-handoff/references/format.md",
    "skills/openagents-handoff/references/security.md",
    "skills/openagents-handoff/references/launch.md",
    "skills/openagents-doctor/SKILL.md",
    "skills/openagents-doctor/references/checks.md",
    "claude-plugin/.claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
    ".github/workflows/validate.yml",
    ".github/workflows/publish.yml",
    ".github/workflows/pr-policy.yml",
    ".github/pull_request_template.md",
    "evals/handoff/cases.md",
    "evals/handoff/rubric.md",
    "evals/doctor/cases.md",
    "scripts/release.py",
    "tests/test_release.py",
}


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def load_json(path: str, errors: list[str]) -> dict:
    try:
        value = json.loads((ROOT / path).read_text())
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"{path}: invalid JSON: {exc}", errors)
        return {}
    if not isinstance(value, dict):
        fail(f"{path}: root must be an object", errors)
        return {}
    return value


def frontmatter(path: Path, errors: list[str]) -> tuple[dict[str, str], str]:
    text = path.read_text()
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        fail(f"{path.relative_to(ROOT)}: frontmatter must start on line 1", errors)
        return {}, text
    try:
        end = lines.index("---", 1)
    except ValueError:
        fail(f"{path.relative_to(ROOT)}: unterminated frontmatter", errors)
        return {}, text

    fields: dict[str, str] = {}
    current: str | None = None
    for line in lines[1:end]:
        match = re.match(r"^([a-z][a-z0-9-]*):(?:\s*(.*))$", line)
        if match:
            current, value = match.groups()
            if current in fields:
                fail(f"{path.relative_to(ROOT)}: duplicate field {current}", errors)
            fields[current] = "" if value in {"|", ">"} else value.strip()
        elif line.startswith("  ") and current:
            fields[current] = f"{fields[current]} {line.strip()}".strip()
        elif line.strip():
            fail(f"{path.relative_to(ROOT)}: unsupported frontmatter line: {line}", errors)
    return fields, "\n".join(lines[end + 1 :])


def validate_skills(version: str, errors: list[str]) -> None:
    skill_root = ROOT / "skills"
    actual = {
        path.name
        for path in skill_root.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    }
    if actual != SKILLS:
        fail(f"skills/: expected {sorted(SKILLS)}, found {sorted(actual)}", errors)

    for name in sorted(SKILLS):
        path = skill_root / name / "SKILL.md"
        fields, body = frontmatter(path, errors)
        for required in ("name", "description", "allowed-tools", "version", "author", "license", "user-invocable"):
            if not fields.get(required):
                fail(f"skills/{name}/SKILL.md: missing {required}", errors)
        if fields.get("name") != name:
            fail(f"skills/{name}/SKILL.md: name must match directory", errors)
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", fields.get("name", "")):
            fail(f"skills/{name}/SKILL.md: invalid skill name", errors)
        description = fields.get("description", "")
        if not 1 <= len(description) <= 1024 or "Use when" not in description:
            fail(f"skills/{name}/SKILL.md: description must be 1-1024 chars and contain 'Use when'", errors)
        if fields.get("version") != version:
            fail(f"skills/{name}/SKILL.md: version must be {version}", errors)
        tools = fields.get("allowed-tools", "")
        if re.search(r"(?:^|\s)Bash(?:\s|$)", tools):
            fail(f"skills/{name}/SKILL.md: Bash must be scoped", errors)
        if "Bash(command:*)" in tools or "Bash(git:*)" in tools:
            fail(f"skills/{name}/SKILL.md: generic command or git scope is forbidden", errors)
        if re.search(r"Bash\(git [^)]*:\*\)", tools):
            fail(f"skills/{name}/SKILL.md: wildcard git scope is forbidden", errors)
        if "Bash(git branch" in tools or "Bash(git hash-object" in tools:
            fail(f"skills/{name}/SKILL.md: mutation-capable git command is forbidden", errors)
        if name in {"openagents", "openagents-doctor"} and "Write" in tools.split():
            fail(f"skills/{name}/SKILL.md: read-only skill grants Write", errors)
        if len(path.read_text().splitlines()) > 200:
            fail(f"skills/{name}/SKILL.md: exceeds 200 lines", errors)

        for reference in re.findall(r"\]\(references/([^)]+\.md)\)", body):
            if "/" in reference or not (path.parent / "references" / reference).is_file():
                fail(f"skills/{name}/SKILL.md: invalid reference {reference}", errors)


def validate_manifests(expected_version: str, errors: list[str]) -> None:
    skills_manifest = load_json("skills.sh.json", errors)
    groups = skills_manifest.get("groupings", [])
    listed = set(groups[0].get("skills", [])) if len(groups) == 1 and isinstance(groups[0], dict) else set()
    if listed != SKILLS:
        fail(f"skills.sh.json: expected skills {sorted(SKILLS)}, found {sorted(listed)}", errors)

    package = load_json("package.json", errors)
    plugin = load_json("claude-plugin/.claude-plugin/plugin.json", errors)
    marketplace = load_json(".claude-plugin/marketplace.json", errors)
    versions = {
        "package.json": package.get("version"),
        "plugin.json": plugin.get("version"),
        "marketplace.json": (marketplace.get("plugins") or [{}])[0].get("version"),
    }
    for source, version in versions.items():
        if version != expected_version:
            fail(f"{source}: version must be {expected_version}, found {version}", errors)

    if plugin.get("name") != "openagents" or not plugin.get("repository"):
        fail("plugin.json: missing name or repository", errors)
    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or len(plugins) != 1:
        fail("marketplace.json: plugins must contain one entry", errors)
    elif plugins[0].get("name") != "openagents" or plugins[0].get("source") != "./claude-plugin":
        fail("marketplace.json: invalid plugin name or source", errors)

    skillfish = load_json("skillfish.json", errors)
    if skillfish.get("skills") != ["luismtns/openagents"]:
        fail("skillfish.json: unexpected source inventory", errors)


def validate_release(errors: list[str]) -> None:
    workflow = (ROOT / ".github/workflows/publish.yml").read_text()
    policy = (ROOT / ".github/workflows/pr-policy.yml").read_text()
    if "pull_request_target:" not in workflow or "types: [closed]" not in workflow:
        fail("release workflow must run after pull request closure", errors)
    if "workflow_dispatch:" not in workflow or "group: release-main" not in workflow:
        fail("release workflow must support recovery and serialized execution", errors)
    if "pull_request:" not in policy or "scripts/release.py check-pr" not in policy:
        fail("PR policy workflow must validate release labels", errors)
    for forbidden in ("@latest", "continue-on-error", "skillfish submit", "refs/pull"):
        if forbidden in workflow:
            fail(f"release workflow contains forbidden pattern: {forbidden}", errors)
    for path, content in (("publish.yml", workflow), ("pr-policy.yml", policy)):
        for action in re.findall(r"(?m)^\s*- uses:\s*([^\s]+)", content):
            if not re.fullmatch(r"[^@]+@[0-9a-f]{40}", action):
                fail(f"{path}: action must be pinned by full commit SHA: {action}", errors)


def main() -> int:
    errors: list[str] = []
    for relative in sorted(REQUIRED):
        path = ROOT / relative
        if not path.is_file():
            fail(f"missing required file: {relative}", errors)
        elif path.is_symlink():
            fail(f"required file must not be a symlink: {relative}", errors)

    if (ROOT / "scripts/clean.sh").exists():
        fail("scripts/clean.sh must not exist", errors)

    version = "unknown"
    if not errors:
        package = load_json("package.json", errors)
        version = package.get("version", "")
        if not isinstance(version, str) or not re.fullmatch(
            r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)", version
        ):
            fail(f"package.json: invalid semantic version {version!r}", errors)
    if not errors:
        validate_skills(version, errors)
        validate_manifests(version, errors)
        validate_release(errors)

    if errors:
        print("OpenAgents validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"OpenAgents validation passed: 3 skills, version {version}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
