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

EXPECTED = {
    "challenge-gov": (
        "eb797b905124aa7ca06577aa2eac6f98734601a851ecad7ad53c4e0628b9fc87",
        "756f0ba6b3d9b0e5f37d97dd44f1764cfd5e2d370f560411017086628795c85d",
    ),
    "sherlock-bounties": (
        "c8a1e59f595a1d8d788ca5cfc22f3d4cb6ee782b741a443911347ea0cf935665",
        "b50b89eca829c002003f350b0648e7852d0d7b330fa19f5380d84cadcf27c67a",
    ),
    "arxiv-cryptography": (
        "f58d8d0792b943fde0bab2a867d452c40ff006d243e8d812e984829009890ab9",
        "68147c9ac8991c6742911d99c927bf5b4610961df1263a281ed54dd5a284697f",
    ),
    "ctftime-upcoming": (
        "111f238ab58ed2167d6e1e9ab0072516d8e0777b1c35ba1adc327c51f497afc2",
        "26679909f0f486874d44e2574329c21a18974bc8b532d8f6795272f008668964",
    ),
    "ethglobal-events": (
        "b9291f5dc88d437f71898fb71674a69535f7083429172423a2422c3e495645d0",
        "b20807c6f1f3ac021a0111c72f2ea6dd211f64714728951fcf7769b2bdfa2648",
    ),
}


def _temp_canonical_files(tmp_path: Path) -> tuple[Path, Path]:
    history = tmp_path / "source_check_history.json"
    registry = tmp_path / "intelligence_sources.json"
    shutil.copy2(HISTORY, history)
    shutil.copy2(REGISTRY, registry)
    return history, registry


def test_aug26_snapshot_is_canonical_with_exact_hashes_and_predecessors(tmp_path):
    snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    assert snapshot["checked_at"] == "2026-08-26T07:39:05Z"
    assert len(snapshot["observations"]) == 5

    observations = {observation["source_id"]: observation for observation in snapshot["observations"]}
    assert set(observations) == set(EXPECTED)
    for source_id, (fingerprint, _) in EXPECTED.items():
        observation = observations[source_id]
        actual = hashlib.sha256(observation["observed"].strip().lower().encode("utf-8")).hexdigest()
        assert observation["sha256"] == fingerprint
        assert actual == fingerprint

    canonical_history = json.loads(HISTORY.read_text(encoding="utf-8"))
    canonical_registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    registry_by_id = {source["id"]: source for source in canonical_registry["sources"]}

    for source_id, (fingerprint, predecessor) in EXPECTED.items():
        matches = [
            check
            for check in canonical_history["checks"]
            if check["source_id"] == source_id and check["checked_at"] == snapshot["checked_at"]
        ]
        assert len(matches) == 1
        assert matches[0]["content_fingerprint"] == fingerprint
        assert matches[0]["previous_fingerprint"] == predecessor
        assert matches[0]["change_state"] == "changed"
        assert registry_by_id[source_id]["last_checked_at"] >= snapshot["checked_at"]

    history_path, registry_path = _temp_canonical_files(tmp_path)
    before_history = history_path.read_bytes()
    before_registry = registry_path.read_bytes()
    result = replay_snapshot(
        SNAPSHOT,
        history_path=history_path,
        registry_path=registry_path,
        write=False,
    )

    assert result["checked_at"] == snapshot["checked_at"]
    assert result["validated_observations"] == 5
    assert result["replayed"] == []
    assert result["skipped_idempotent"] == [observation["source_id"] for observation in snapshot["observations"]]
    assert result["wrote_files"] is False
    assert history_path.read_bytes() == before_history
    assert registry_path.read_bytes() == before_registry


def test_aug26_direct_script_dry_run_is_idempotent_and_non_mutating(tmp_path):
    snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
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
    assert result["replayed"] == []
    assert result["skipped_idempotent"] == [observation["source_id"] for observation in snapshot["observations"]]
    assert result["wrote_files"] is False
    assert history_path.read_bytes() == before_history
    assert registry_path.read_bytes() == before_registry
