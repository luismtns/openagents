#!/usr/bin/env python3
"""Prepare idempotent OpenAgents releases from merged pull request metadata."""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
from pathlib import Path


RELEASE_LABELS = {"release:major", "release:minor", "release:patch", "release:none"}
CHANGE_SECTIONS = {
    "change:added": "Added",
    "change:changed": "Changed",
    "change:deprecated": "Deprecated",
    "change:removed": "Removed",
    "change:fixed": "Fixed",
    "change:security": "Security",
}
SKILLS = ("openagents", "openagents-handoff", "openagents-doctor")
VERSION_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")


class ReleaseError(ValueError):
    pass


def load_json(path: Path) -> dict:
    value = json.loads(path.read_text())
    if not isinstance(value, dict):
        raise ReleaseError(f"{path}: expected a JSON object")
    return value


def pull_request(payload: dict) -> dict:
    pr = payload.get("pull_request", payload)
    if not isinstance(pr, dict) or not isinstance(pr.get("number"), int):
        raise ReleaseError("event does not contain pull request metadata")
    return pr


def label_names(pr: dict) -> set[str]:
    labels = pr.get("labels", [])
    if not isinstance(labels, list):
        raise ReleaseError("pull request labels must be a list")
    return {
        label["name"]
        for label in labels
        if isinstance(label, dict) and isinstance(label.get("name"), str)
    }


def check_policy(payload: dict, require_merged: bool = False) -> dict:
    pr = pull_request(payload)
    base = pr.get("base", {})
    if not isinstance(base, dict) or base.get("ref") != "main":
        raise ReleaseError("pull request must target main")
    if require_merged and not pr.get("merged_at"):
        raise ReleaseError("pull request is not merged")

    labels = label_names(pr)
    release_prefixed = {label for label in labels if label.startswith("release:")}
    change_prefixed = {label for label in labels if label.startswith("change:")}
    unknown = (release_prefixed - RELEASE_LABELS) | (change_prefixed - CHANGE_SECTIONS.keys())
    if unknown:
        raise ReleaseError(f"unknown release labels: {sorted(unknown)}")
    release = sorted(labels & RELEASE_LABELS)
    changes = sorted(labels & CHANGE_SECTIONS.keys())
    if len(release) != 1:
        raise ReleaseError("exactly one release:* label is required")
    if release[0] == "release:none":
        if changes:
            raise ReleaseError("release:none must not have a change:* label")
        return {"eligible": False, "release": release[0], "change": None, "pr": pr["number"]}
    if len(changes) != 1:
        raise ReleaseError("eligible releases require exactly one change:* label")
    return {"eligible": True, "release": release[0], "change": changes[0], "pr": pr["number"]}


def parse_version(value: str) -> tuple[int, int, int]:
    match = VERSION_RE.fullmatch(value)
    if not match:
        raise ReleaseError(f"invalid semantic version: {value}")
    return tuple(map(int, match.groups()))  # type: ignore[return-value]


def bump_version(current: str, release_label: str) -> str:
    major, minor, patch = parse_version(current)
    if release_label == "release:major":
        return f"{major + 1}.0.0"
    if release_label == "release:minor":
        return f"{major}.{minor + 1}.0"
    if release_label == "release:patch":
        return f"{major}.{minor}.{patch + 1}"
    raise ReleaseError(f"cannot bump version for {release_label}")


def current_version(root: Path) -> str:
    value = load_json(root / "package.json").get("version")
    if not isinstance(value, str):
        raise ReleaseError("package.json: missing version")
    parse_version(value)
    return value


def skill_version(path: Path) -> str:
    matches = re.findall(r"(?m)^version:\s*(\S+)\s*$", path.read_text())
    if len(matches) != 1:
        raise ReleaseError(f"{path}: expected exactly one frontmatter version")
    return matches[0]


def version_inventory(root: Path) -> dict[str, str]:
    plugin = load_json(root / "claude-plugin/.claude-plugin/plugin.json")
    marketplace = load_json(root / ".claude-plugin/marketplace.json")
    plugins = marketplace.get("plugins", [])
    if not isinstance(plugins, list) or len(plugins) != 1 or not isinstance(plugins[0], dict):
        raise ReleaseError("marketplace.json: expected one plugin")
    inventory = {
        "package.json": current_version(root),
        "plugin.json": plugin.get("version"),
        "marketplace.json": plugins[0].get("version"),
    }
    for skill in SKILLS:
        inventory[f"skills/{skill}/SKILL.md"] = skill_version(root / f"skills/{skill}/SKILL.md")
    if not all(isinstance(value, str) for value in inventory.values()):
        raise ReleaseError("one or more manifests are missing versions")
    return inventory  # type: ignore[return-value]


def verify_versions(root: Path) -> str:
    inventory = version_inventory(root)
    versions = set(inventory.values())
    if len(versions) != 1:
        details = ", ".join(f"{path}={version}" for path, version in inventory.items())
        raise ReleaseError(f"version mismatch: {details}")
    return versions.pop()


def update_versions(root: Path, version: str) -> None:
    parse_version(version)
    for relative in (
        "package.json",
        "claude-plugin/.claude-plugin/plugin.json",
        ".claude-plugin/marketplace.json",
    ):
        path = root / relative
        load_json(path)
        text, count = re.subn(
            r'(?m)^(\s*"version"\s*:\s*")[^"]+("\s*,?\s*)$',
            rf"\g<1>{version}\g<2>",
            path.read_text(),
        )
        if count != 1:
            raise ReleaseError(f"{path}: expected one JSON version replacement")
        path.write_text(text)

    for skill in SKILLS:
        path = root / f"skills/{skill}/SKILL.md"
        text, count = re.subn(
            r"(?m)^version:\s*\S+\s*$",
            f"version: {version}",
            path.read_text(),
        )
        if count != 1:
            raise ReleaseError(f"{path}: expected one version replacement")
        path.write_text(text)


def sanitize_title(value: str) -> str:
    title = " ".join(value.split())
    if not title:
        raise ReleaseError("pull request title is empty")
    title = html.escape(title, quote=False).replace("\\", "\\\\")
    return title.replace("[", "\\[").replace("]", "\\]")


def add_entry(body: str, section: str, entry: str) -> str:
    heading = f"### {section}"
    match = re.search(rf"(?m)^{re.escape(heading)}\s*$", body)
    if not match:
        return f"{body.rstrip()}\n\n{heading}\n\n- {entry}".strip()
    next_heading = re.search(r"(?m)^###\s+", body[match.end() :])
    end = match.end() + next_heading.start() if next_heading else len(body)
    section_body = body[match.end() : end].rstrip()
    replacement = f"\n\n{section_body.strip()}\n- {entry}" if section_body.strip() else f"\n\n- {entry}"
    return body[: match.end()] + replacement + "\n\n" + body[end:].lstrip()


def existing_release(text: str, pr_number: int) -> str | None:
    marker = f"[#{pr_number}]("
    position = text.find(marker)
    if position < 0:
        return None
    headings = list(re.finditer(r"(?m)^## \[(\d+\.\d+\.\d+)\] - .+$", text[:position]))
    if not headings:
        raise ReleaseError(f"PR #{pr_number} marker is outside a release section")
    return headings[-1].group(1)


def normalize_pull_request(value: dict) -> dict:
    if "html_url" in value:
        return value
    return {
        "number": value.get("number"),
        "title": value.get("title"),
        "html_url": value.get("url"),
        "merged_at": value.get("mergedAt"),
        "base": {"ref": value.get("baseRefName")},
        "labels": value.get("labels", []),
    }


def release_queue(values: list, changelog: str) -> list[int]:
    pending: list[tuple[str, int]] = []
    for value in values:
        if not isinstance(value, dict):
            raise ReleaseError("pull request queue entries must be objects")
        pr = normalize_pull_request(value)
        labels = label_names(pr)
        if not any(label.startswith(("release:", "change:")) for label in labels):
            continue
        policy = check_policy(pr, require_merged=True)
        if policy["eligible"] and not existing_release(changelog, pr["number"]):
            pending.append((str(pr["merged_at"]), pr["number"]))
    pending.sort()
    return [number for _, number in pending]


def release_queue_through(values: list, changelog: str, pr_number: int) -> list[int]:
    target = next(
        (
            normalize_pull_request(value)
            for value in values
            if isinstance(value, dict) and value.get("number") == pr_number
        ),
        None,
    )
    if target is None:
        raise ReleaseError(f"pull request #{pr_number} is not in the merged queue")
    policy = check_policy(target, require_merged=True)
    if not policy["eligible"]:
        return []
    queue = release_queue(values, changelog)
    if pr_number in queue:
        return queue[: queue.index(pr_number) + 1]
    if existing_release(changelog, pr_number):
        return [pr_number]
    raise ReleaseError(f"pull request #{pr_number} is neither pending nor recorded")


def update_changelog(
    text: str,
    version: str,
    date: str,
    section: str,
    entry: str,
) -> str:
    unreleased = re.search(r"(?m)^## \[Unreleased\]\s*$", text)
    if not unreleased:
        raise ReleaseError("CHANGELOG.md: missing [Unreleased] heading")
    following = re.search(r"(?m)^## \[[^]]+\](?: - .*)?\s*$", text[unreleased.end() :])
    tail_start = unreleased.end() + following.start() if following else len(text)
    body = text[unreleased.end() : tail_start].strip()
    body = add_entry(body, section, entry)
    tail = text[tail_start:].lstrip()
    result = f"{text[:unreleased.end()].rstrip()}\n\n## [{version}] - {date}\n\n{body.rstrip()}\n"
    if tail:
        result += f"\n{tail.rstrip()}\n"
    return result


def prepare_release(root: Path, payload: dict, date: str | None = None) -> dict:
    policy = check_policy(payload, require_merged=True)
    if not policy["eligible"]:
        return policy
    pr = pull_request(payload)
    changelog_path = root / "CHANGELOG.md"
    changelog = changelog_path.read_text()
    existing = existing_release(changelog, pr["number"])
    if existing:
        return {**policy, "version": existing, "existing": True}

    current = verify_versions(root)
    version = bump_version(current, policy["release"])
    title = sanitize_title(str(pr.get("title", "")))
    url = pr.get("html_url")
    expected_suffix = f"/pull/{pr['number']}"
    if (
        not isinstance(url, str)
        or not url.startswith("https://github.com/")
        or not url.endswith(expected_suffix)
    ):
        raise ReleaseError("pull request URL must be a public GitHub URL")
    entry = f"{title} ([#{pr['number']}]({url}))"
    release_date = date or dt.date.today().isoformat()
    changelog = update_changelog(
        changelog,
        version,
        release_date,
        CHANGE_SECTIONS[policy["change"]],
        entry,
    )
    changelog_path.write_text(changelog)
    update_versions(root, version)
    return {**policy, "version": version, "existing": False}


def release_notes(changelog: str, version: str) -> str:
    start = re.search(rf"(?m)^## \[{re.escape(version)}\] - .+$", changelog)
    if not start:
        raise ReleaseError(f"CHANGELOG.md: release {version} not found")
    following = re.search(r"(?m)^## \[", changelog[start.end() :])
    end = start.end() + following.start() if following else len(changelog)
    return changelog[start.start() : end].strip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "command", choices=("check-pr", "prepare", "queue", "notes", "verify-versions")
    )
    parser.add_argument("--event", type=Path)
    parser.add_argument("--prs", type=Path)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--date")
    parser.add_argument("--version")
    parser.add_argument("--through", type=int)
    parser.add_argument("--require-merged", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.command == "verify-versions":
            print(verify_versions(args.root))
            return 0
        if args.command == "notes":
            if not args.version:
                raise ReleaseError("notes requires --version")
            print(release_notes((args.root / "CHANGELOG.md").read_text(), args.version), end="")
            return 0
        if args.command == "queue":
            if not args.prs:
                raise ReleaseError("queue requires --prs")
            values = json.loads(args.prs.read_text())
            if not isinstance(values, list):
                raise ReleaseError("queue input must be a JSON array")
            changelog = (args.root / "CHANGELOG.md").read_text()
            queue = (
                release_queue_through(values, changelog, args.through)
                if args.through is not None
                else release_queue(values, changelog)
            )
            print(json.dumps(queue, separators=(",", ":")))
            return 0
        if not args.event:
            raise ReleaseError(f"{args.command} requires --event")
        payload = load_json(args.event)
        result = (
            check_policy(payload, require_merged=args.require_merged)
            if args.command == "check-pr"
            else prepare_release(args.root, payload, args.date)
        )
        print(json.dumps(result, separators=(",", ":")))
        return 0
    except (OSError, json.JSONDecodeError, ReleaseError) as exc:
        print(f"release error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
