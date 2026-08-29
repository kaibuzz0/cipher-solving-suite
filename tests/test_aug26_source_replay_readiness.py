from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

from scripts.source_check_history import replay_snapshot

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / "intelligence" / "feeds" / "2026-08-26-source-health.json"
HISTORY = ROOT / "data" / "source_check_history.json"
REGISTRY = ROOT / "data" / "intelligence_sources.json"
SCRIPT = ROOT / "scripts" / "source_check_history.py"

EXPECTED_PREDECESSORS = {
    "challenge-gov": "756f0ba6b3d9b0e5f37d97dd44f1764cfd5e2d370f560411017086628795c85d",
    "sherlock-bounties": "b50b89eca829c002003f350b0648e7852d0d7b330fa19f5380d84cadcf27c67a",
    "arxiv-cryptography": "68147c9ac8991c6742911d99c927bf5b4610961df1263a281ed54dd5a284697f",
    "ctftime-upcoming": "26679909f0f486874d44e2574329c21a18974bc8b532d8f6795272f008668964",
    "ethglobal-events": "b20807c6f1f3ac021a0111c72f2ea6dd211f64714728951fcf7769b2bdfa2648",
}


def _temp_canonical_files(tmp_path: Path) -> tuple[Path, Path]:
    history = tmp_path / "source_check_history.json"
    registry = tmp_path / "intelligence_sources.json"
    shutil.copy2(HISTORY, history)
    shutil.copy2(REGISTRY, registry)
    return history, registry


def test_aug26_snapshot_hashes_and_predecessors_are_replay_ready(tmp_path):
    snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    assert snapshot["checked_at"] == "2026-08-26T07:39:05Z"
    assert len(snapshot["observations"]) == 5

    for observation in snapshot["observations"]:
        actual = hashlib.sha256(observation["observed"].strip().lower().encode("utf-8")).hexdigest()
        assert actual == observation["sha256"]

    history_path, registry_path = _temp_canonical_files(tmp_path)
    before_history = history_path.read_bytes()
    before_registry = registry_path.read_bytes()

    result = replay_snapshot(
        SNAPSHOT,
        history_path=history_path,
        registry_path=registry_path,
        write=False,
    )

    assert result["checked_at"] == "2026-08-26T07:39:05Z"
    assert result["validated_observations"] == 5
    assert result["skipped_idempotent"] == []
    assert result["wrote_files"] is False
    assert len(result["replayed"]) == 5

    replayed = {entry["source_id"]: entry for entry in result["replayed"]}
    assert set(replayed) == set(EXPECTED_PREDECESSORS)
    for source_id, predecessor in EXPECTED_PREDECESSORS.items():
        assert replayed[source_id]["previous_fingerprint"] == predecessor
        assert replayed[source_id]["change_state"] == "changed"

    assert history_path.read_bytes() == before_history
    assert registry_path.read_bytes() == before_registry


def test_aug26_direct_script_dry_run_is_non_mutating(tmp_path):
    history_path, registry_path = _temp_canonical_files(tmp_path)
    before_history = history_path.read_bytes()
    before_registry = registry_path.read_bytes()

    completed = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "replay-snapshot",
            str(SNAPSHOT),
            "--history",
            str(history_path),
            "--registry",
            str(registry_path),
            "--dry-run",
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode == 0, completed.stderr
    result = json.loads(completed.stdout)
    assert result["validated_observations"] == 5
    assert len(result["replayed"]) == 5
    assert result["wrote_files"] is False
    assert history_path.read_bytes() == before_history
    assert registry_path.read_bytes() == before_registry
