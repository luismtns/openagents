from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SPEC = importlib.util.spec_from_file_location(
    "openagents_release", Path(__file__).parents[1] / "scripts/release.py"
)
release = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(release)


def payload(*labels: str, number: int = 42, title: str = "Add portable handoff") -> dict:
    return {
        "pull_request": {
            "number": number,
            "title": title,
            "html_url": f"https://github.com/luismtns/openagents/pull/{number}",
            "merged_at": "2026-07-15T12:00:00Z",
            "base": {"ref": "main"},
            "labels": [{"name": label} for label in labels],
        }
    }


def write_fixture(root: Path, version: str = "1.12.0", unreleased: str = "") -> None:
    (root / "skills").mkdir()
    for skill in release.SKILLS:
        path = root / "skills" / skill
        path.mkdir()
        (path / "SKILL.md").write_text(f"---\nname: {skill}\nversion: {version}\n---\n")
    (root / "claude-plugin/.claude-plugin").mkdir(parents=True)
    (root / ".claude-plugin").mkdir()
    (root / "package.json").write_text(json.dumps({"version": version}, indent=2) + "\n")
    (root / "claude-plugin/.claude-plugin/plugin.json").write_text(
        json.dumps({"version": version}, indent=2) + "\n"
    )
    (root / ".claude-plugin/marketplace.json").write_text(
        json.dumps({"plugins": [{"version": version}]}, indent=2) + "\n"
    )
    (root / "CHANGELOG.md").write_text(
        f"# Changelog\n\n## [Unreleased]\n\n{unreleased}\n\n## [1.12.0] - 2026-07-08\n\nOld.\n"
    )


class PolicyTests(unittest.TestCase):
    def test_release_none_needs_no_change_label(self) -> None:
        self.assertFalse(release.check_policy(payload("release:none"))["eligible"])

    def test_release_none_rejects_change_label(self) -> None:
        with self.assertRaises(release.ReleaseError):
            release.check_policy(payload("release:none", "change:changed"))

    def test_eligible_release_requires_one_label_of_each_kind(self) -> None:
        result = release.check_policy(payload("release:minor", "change:added"))
        self.assertTrue(result["eligible"])
        with self.assertRaises(release.ReleaseError):
            release.check_policy(payload("release:minor"))
        with self.assertRaises(release.ReleaseError):
            release.check_policy(payload("release:minor", "release:patch", "change:added"))

    def test_unknown_prefixed_label_is_rejected(self) -> None:
        with self.assertRaises(release.ReleaseError):
            release.check_policy(payload("release:patch", "release:banana", "change:fixed"))


class VersionTests(unittest.TestCase):
    def test_semver_bumps(self) -> None:
        self.assertEqual(release.bump_version("1.12.3", "release:major"), "2.0.0")
        self.assertEqual(release.bump_version("1.12.3", "release:minor"), "1.13.0")
        self.assertEqual(release.bump_version("1.12.3", "release:patch"), "1.12.4")

    def test_rejects_non_semver(self) -> None:
        with self.assertRaises(release.ReleaseError):
            release.parse_version("v1.2.3")


class PrepareTests(unittest.TestCase):
    def test_prepares_release_and_updates_every_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, unreleased="### Security\n\n- Existing detail.")
            result = release.prepare_release(
                root,
                payload("release:major", "change:changed"),
                "2026-07-15",
            )
            self.assertEqual(result["version"], "2.0.0")
            self.assertEqual(set(release.version_inventory(root).values()), {"2.0.0"})
            changelog = (root / "CHANGELOG.md").read_text()
            self.assertIn("## [2.0.0] - 2026-07-15", changelog)
            self.assertIn("### Security\n\n- Existing detail.", changelog)
            self.assertIn("### Changed", changelog)
            self.assertIn("[#42]", changelog)

    def test_rerun_returns_existing_version_without_second_bump(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root)
            event = payload("release:patch", "change:fixed")
            first = release.prepare_release(root, event, "2026-07-15")
            second = release.prepare_release(root, event, "2026-07-15")
            self.assertEqual(first["version"], "1.12.1")
            self.assertEqual(second["version"], "1.12.1")
            self.assertTrue(second["existing"])

    def test_historical_rerun_survives_newer_manifest_version(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root)
            event = payload("release:patch", "change:fixed")
            release.prepare_release(root, event, "2026-07-15")
            package = json.loads((root / "package.json").read_text())
            package["version"] = "9.9.9"
            (root / "package.json").write_text(json.dumps(package) + "\n")
            result = release.prepare_release(root, event, "2026-07-15")
            self.assertEqual(result["version"], "1.12.1")
            self.assertTrue(result["existing"])

    def test_sanitizes_markdown_title(self) -> None:
        value = release.sanitize_title("Fix [link] <script>  now")
        self.assertEqual(value, "Fix \\[link\\] &lt;script&gt; now")

    def test_release_notes_extract_one_section(self) -> None:
        text = "# C\n\n## [Unreleased]\n\n## [2.0.0] - 2026-07-15\n\nNotes\n\n## [1.0.0] - 2026-01-01\n"
        notes = release.release_notes(text, "2.0.0")
        self.assertIn("Notes", notes)
        self.assertNotIn("1.0.0", notes)

    def test_queue_uses_merge_order_and_skips_processed_prs(self) -> None:
        first = payload("release:minor", "change:added", number=10)["pull_request"]
        second = payload("release:patch", "change:fixed", number=11)["pull_request"]
        first["merged_at"] = "2026-07-15T10:00:00Z"
        second["merged_at"] = "2026-07-15T11:00:00Z"
        self.assertEqual(release.release_queue([second, first], "## [Unreleased]\n"), [10, 11])
        changelog = "## [Unreleased]\n\n## [1.13.0] - 2026-07-15\n\n- Done ([#10](https://x))\n"
        self.assertEqual(release.release_queue([second, first], changelog), [11])

    def test_dispatch_processes_older_pending_releases_first(self) -> None:
        first = payload("release:minor", "change:added", number=10)["pull_request"]
        second = payload("release:patch", "change:fixed", number=11)["pull_request"]
        first["merged_at"] = "2026-07-15T10:00:00Z"
        second["merged_at"] = "2026-07-15T11:00:00Z"
        queue = release.release_queue_through([second, first], "## [Unreleased]\n", 11)
        self.assertEqual(queue, [10, 11])

    def test_dispatch_release_none_is_noop(self) -> None:
        value = payload("release:none", number=12)["pull_request"]
        self.assertEqual(
            release.release_queue_through([value], "## [Unreleased]\n", 12), []
        )

    def test_mixed_bumps_follow_merge_order(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root)
            minor = payload("release:minor", "change:added", number=10)
            patch = payload("release:patch", "change:fixed", number=11)
            first = release.prepare_release(root, minor, "2026-07-15")
            second = release.prepare_release(root, patch, "2026-07-15")
            self.assertEqual(first["version"], "1.13.0")
            self.assertEqual(second["version"], "1.13.1")


if __name__ == "__main__":
    unittest.main()
