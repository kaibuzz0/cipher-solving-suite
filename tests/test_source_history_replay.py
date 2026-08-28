import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.source_check_history import replay_snapshot

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "source_check_history.py"


def digest(value: str) -> str:
    return hashlib.sha256(value.strip().lower().encode("utf-8")).hexdigest()


class SourceSnapshotReplayTests(unittest.TestCase):
    def make_files(self, root: Path):
        history = root / "history.json"
        registry = root / "registry.json"
        snapshot = root / "snapshot.json"
        history.write_text(json.dumps({
            "schema_version": 1,
            "updated_at": "2026-08-24T00:00:00Z",
            "checks": [
                {
                    "source_id": "alpha",
                    "checked_at": "2026-08-24T00:00:00Z",
                    "content_fingerprint": digest("old alpha"),
                    "previous_fingerprint": None,
                    "change_state": "first-seen",
                    "note": "old",
                },
                {
                    "source_id": "beta",
                    "checked_at": "2026-08-24T00:00:00Z",
                    "content_fingerprint": digest("same beta"),
                    "previous_fingerprint": None,
                    "change_state": "first-seen",
                    "note": "old",
                },
            ],
        }, indent=2) + "\n", encoding="utf-8")
        registry.write_text(json.dumps({
            "schema_version": 1,
            "updated_at": "2026-08-24T00:00:00Z",
            "sources": [
                {"id": "alpha", "name": "Alpha", "source_type": "official", "url": "https://example.com/a", "categories": ["research"], "tier": "primary", "freshness_hours": 24, "last_checked_at": "2026-08-24T00:00:00Z", "assigned_agent": "test", "enabled": True, "publish_default_confidence": "high"},
                {"id": "beta", "name": "Beta", "source_type": "official", "url": "https://example.com/b", "categories": ["research"], "tier": "primary", "freshness_hours": 24, "last_checked_at": "2026-08-24T00:00:00Z", "assigned_agent": "test", "enabled": True, "publish_default_confidence": "high"},
            ],
        }, indent=2) + "\n", encoding="utf-8")
        snapshot.write_text(json.dumps({
            "schema_version": 1,
            "checked_at": "2026-08-25T00:00:00Z",
            "observations": [
                {"source_id": "alpha", "observed": "new alpha", "sha256": digest("new alpha"), "note": "changed"},
                {"source_id": "beta", "observed": "same beta", "sha256": digest("same beta"), "note": "unchanged"},
            ],
        }, indent=2) + "\n", encoding="utf-8")
        return history, registry, snapshot

    def test_replay_preserves_predecessors_and_updates_only_observed_sources(self):
        with tempfile.TemporaryDirectory() as tmp:
            history_path, registry_path, snapshot_path = self.make_files(Path(tmp))
            result = replay_snapshot(snapshot_path, history_path, registry_path)
            self.assertEqual(result["validated_observations"], 2)
            self.assertEqual([entry["source_id"] for entry in result["replayed"]], ["alpha", "beta"])
            history = json.loads(history_path.read_text(encoding="utf-8"))
            alpha = next(c for c in history["checks"] if c["source_id"] == "alpha" and c["checked_at"] == "2026-08-25T00:00:00Z")
            beta = next(c for c in history["checks"] if c["source_id"] == "beta" and c["checked_at"] == "2026-08-25T00:00:00Z")
            self.assertEqual(alpha["previous_fingerprint"], digest("old alpha"))
            self.assertEqual(alpha["change_state"], "changed")
            self.assertEqual(beta["previous_fingerprint"], digest("same beta"))
            self.assertEqual(beta["change_state"], "unchanged")
            registry = json.loads(registry_path.read_text(encoding="utf-8"))
            self.assertTrue(all(s["last_checked_at"] == "2026-08-25T00:00:00Z" for s in registry["sources"]))

    def test_hash_mismatch_fails_without_mutating_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            history_path, registry_path, snapshot_path = self.make_files(Path(tmp))
            snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
            snapshot["observations"][0]["sha256"] = "0" * 64
            snapshot_path.write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
            before_history = history_path.read_bytes()
            before_registry = registry_path.read_bytes()
            with self.assertRaisesRegex(ValueError, "fingerprint mismatch"):
                replay_snapshot(snapshot_path, history_path, registry_path)
            self.assertEqual(history_path.read_bytes(), before_history)
            self.assertEqual(registry_path.read_bytes(), before_registry)

    def test_newer_canonical_history_blocks_out_of_order_replay(self):
        with tempfile.TemporaryDirectory() as tmp:
            history_path, registry_path, snapshot_path = self.make_files(Path(tmp))
            history = json.loads(history_path.read_text(encoding="utf-8"))
            history["checks"].insert(0, {
                "source_id": "alpha",
                "checked_at": "2026-08-26T00:00:00Z",
                "content_fingerprint": digest("future alpha"),
                "previous_fingerprint": digest("old alpha"),
                "change_state": "changed",
                "note": "future",
            })
            history_path.write_text(json.dumps(history, indent=2) + "\n", encoding="utf-8")
            before = history_path.read_bytes()
            with self.assertRaisesRegex(ValueError, "chronology violation"):
                replay_snapshot(snapshot_path, history_path, registry_path)
            self.assertEqual(history_path.read_bytes(), before)

    def test_idempotent_replay_skips_existing_exact_records(self):
        with tempfile.TemporaryDirectory() as tmp:
            history_path, registry_path, snapshot_path = self.make_files(Path(tmp))
            first = replay_snapshot(snapshot_path, history_path, registry_path)
            self.assertEqual(len(first["replayed"]), 2)
            before_history = history_path.read_bytes()
            before_registry = registry_path.read_bytes()
            second = replay_snapshot(snapshot_path, history_path, registry_path)
            self.assertEqual(second["replayed"], [])
            self.assertEqual(second["skipped_idempotent"], ["alpha", "beta"])
            self.assertFalse(second["wrote_files"])
            self.assertEqual(history_path.read_bytes(), before_history)
            self.assertEqual(registry_path.read_bytes(), before_registry)

    def test_direct_script_dry_run_is_non_destructive(self):
        with tempfile.TemporaryDirectory() as tmp:
            history_path, registry_path, snapshot_path = self.make_files(Path(tmp))
            before_history = history_path.read_bytes()
            before_registry = registry_path.read_bytes()
            proc = subprocess.run(
                [sys.executable, str(SCRIPT), "replay-snapshot", str(snapshot_path), "--history", str(history_path), "--registry", str(registry_path), "--dry-run"],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)
            payload = json.loads(proc.stdout)
            self.assertEqual(payload["validated_observations"], 2)
            self.assertFalse(payload["wrote_files"])
            self.assertEqual(history_path.read_bytes(), before_history)
            self.assertEqual(registry_path.read_bytes(), before_registry)

    def test_repository_aug25_snapshot_is_replay_ready_against_aug24_canonical_state(self):
        snapshot_path = ROOT / "intelligence" / "feeds" / "2026-08-25-source-health.json"
        self.assertTrue(snapshot_path.exists())
        expected = {
            "ctftime-upcoming": ("26679909f0f486874d44e2574329c21a18974bc8b532d8f6795272f008668964", "a96cc699e3f8a7f727dd097f6b716986c2673381f78d6a093531259feec10c22"),
            "sherlock-bounties": ("b50b89eca829c002003f350b0648e7852d0d7b330fa19f5380d84cadcf27c67a", "13c29e51e7cfabbf62a22338a5db82e72455b78d14e76ff2dfeb4bdb56ab9dd6"),
            "arxiv-cryptography": ("68147c9ac8991c6742911d99c927bf5b4610961df1263a281ed54dd5a284697f", "8fb2b94561566e6c143eac47473075dfb0c914a024b12e88052a53e851faa82d"),
            "ethglobal-events": ("b20807c6f1f3ac021a0111c72f2ea6dd211f64714728951fcf7769b2bdfa2648", "a1954da1fd67d5f200745c9b5c5cd7f2053eb930571d9e1ac28f7c0b7def8cd9"),
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            history_path = root / "source_check_history.json"
            registry_path = root / "intelligence_sources.json"
            shutil.copyfile(ROOT / "data" / "source_check_history.json", history_path)
            shutil.copyfile(ROOT / "data" / "intelligence_sources.json", registry_path)
            before_history = history_path.read_bytes()
            before_registry = registry_path.read_bytes()
            result = replay_snapshot(snapshot_path, history_path, registry_path, write=False)
            self.assertEqual(result["checked_at"], "2026-08-25T19:42:47Z")
            self.assertEqual(result["validated_observations"], 4)
            self.assertFalse(result["wrote_files"])
            replayed = {entry["source_id"]: entry for entry in result["replayed"]}
            self.assertEqual(set(replayed), set(expected))
            for source_id, (fingerprint, predecessor) in expected.items():
                self.assertEqual(replayed[source_id]["content_fingerprint"], fingerprint)
                self.assertEqual(replayed[source_id]["previous_fingerprint"], predecessor)
                self.assertEqual(replayed[source_id]["change_state"], "changed")
            self.assertEqual(history_path.read_bytes(), before_history)
            self.assertEqual(registry_path.read_bytes(), before_registry)


if __name__ == "__main__":
    unittest.main()
