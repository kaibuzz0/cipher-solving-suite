from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

from scripts.source_check_history import replay_snapshot

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL = ROOT / "intelligence" / "feeds" / "2026-08-27-source-health.json"
RECONCILED = ROOT / "intelligence" / "feeds" / "2026-08-27-source-health-reconciled.json"
HISTORY = ROOT / "data" / "source_check_history.json"
REGISTRY = ROOT / "data" / "intelligence_sources.json"
SCRIPT = ROOT / "scripts" / "source_check_history.py"
STAMP = "2026-08-27T19:39:25Z"

EXPECTED = {
    "challenge-gov": (
        "d2c287ebc5ba6e4f439201efc1d1f3b6c3769300d20157bfef4c8c1a0a8b8609",
        "c0e125df5360a452d731c08f76412c7d62381054fca56e6fcb4e2184575d12cf",
        "eb797b905124aa7ca06577aa2eac6f98734601a851ecad7ad53c4e0628b9fc87",
    ),
    "ctftime-upcoming": (
        "fce07b15b6831c7c6a33f01fbb38d5ec4426d2cdd1d78e6cafd87fea49f03b3e",
        "ef2d96986e610ccbfbb877ba67ddc2c5f975182de29629b4401a34a81e0d4add",
        "111f238ab58ed2167d6e1e9ab0072516d8e0777b1c35ba1adc327c51f497afc2",
    ),
    "sherlock-bounties": (
        "09762fbabc3e28722247843901be7ca04a403b5c33c4380a8aadfbd7c55c19fa",
        "67f240a38ead70926e9776f3e5aa3afb6dc25920b3f7c555f34c7b9dbe262b05",
        "c8a1e59f595a1d8d788ca5cfc22f3d4cb6ee782b741a443911347ea0cf935665",
    ),
    "arxiv-cryptography": (
        "2eae08782a5fc7f1ba9aa2a59bfd98a379d504fbef7c163c7f0ed31a72a9c629",
        "d126279a1ebded4a02bb4dca40b381c8cf72484831d9913bf924ae5ebfc2b1c9",
        "f58d8d0792b943fde0bab2a867d452c40ff006d243e8d812e984829009890ab9",
    ),
    "ethglobal-events": (
        "b29a7c1243b4c41422fbc7dbc9cf773aefbbfde18caeef085e56f82eaecc7ec0",
        "9f0a188daf173966ee324470229a9bfbf2e864807b8f46200ea17f6bca9741dc",
        "b9291f5dc88d437f71898fb71674a69535f7083429172423a2422c3e495645d0",
    ),
}


def _temp_canonical_files(tmp_path: Path) -> tuple[Path, Path]:
    history = tmp_path / "source_check_history.json"
    registry = tmp_path / "intelligence_sources.json"
    shutil.copy2(HISTORY, history)
    shutil.copy2(REGISTRY, registry)
    return history, registry


def test_aug27_reconciliation_preserves_provenance_and_is_canonical(tmp_path):
    original = json.loads(ORIGINAL.read_text(encoding="utf-8"))
    reconciled = json.loads(RECONCILED.read_text(encoding="utf-8"))
    history = json.loads(HISTORY.read_text(encoding="utf-8"))
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))

    assert original["checked_at"] == reconciled["checked_at"] == STAMP
    assert reconciled["reconciliation"]["original_commit"] == "3fd83de69a0ec626a6f03143f3207a5c52ec7ade"
    assert reconciled["reconciliation"]["merged_commit"] == "c57aebc027d37df002224199b8da79bab16b1e59"
    assert history["updated_at"] == STAMP
    # Registry-level updated_at was already newer than the replay and must not rewind.
    assert registry["updated_at"] == "2026-08-27T20:02:00Z"

    original_by_id = {item["source_id"]: item for item in original["observations"]}
    reconciled_by_id = {item["source_id"]: item for item in reconciled["observations"]}
    registry_by_id = {item["id"]: item for item in registry["sources"]}
    assert set(original_by_id) == set(reconciled_by_id) == set(EXPECTED)

    for source_id, (bad_hash, corrected_hash, predecessor) in EXPECTED.items():
        original_item = original_by_id[source_id]
        corrected_item = reconciled_by_id[source_id]
        assert original_item["observed"] == corrected_item["observed"]
        assert original_item["sha256"] == bad_hash
        actual = hashlib.sha256(corrected_item["observed"].strip().lower().encode("utf-8")).hexdigest()
        assert actual == corrected_hash
        assert corrected_item["sha256"] == corrected_hash
        assert reconciled["reconciliation"]["original_hashes"][source_id] == bad_hash

        canonical = [
            item for item in history["checks"]
            if item["source_id"] == source_id and item["checked_at"] == STAMP
        ]
        assert len(canonical) == 1
        assert canonical[0]["content_fingerprint"] == corrected_hash
        assert canonical[0]["previous_fingerprint"] == predecessor
        assert canonical[0]["change_state"] == "changed"
        assert registry_by_id[source_id]["last_checked_at"] == STAMP

    history_path, registry_path = _temp_canonical_files(tmp_path)
    before_history = history_path.read_bytes()
    before_registry = registry_path.read_bytes()
    result = replay_snapshot(
        RECONCILED,
        history_path=history_path,
        registry_path=registry_path,
        write=True,
    )

    assert result["validated_observations"] == 5
    assert result["replayed"] == []
    assert set(result["skipped_idempotent"]) == set(EXPECTED)
    assert result["wrote_files"] is False
    assert history_path.read_bytes() == before_history
    assert registry_path.read_bytes() == before_registry


def test_aug27_reconciled_direct_script_replay_is_idempotent(tmp_path):
    history_path, registry_path = _temp_canonical_files(tmp_path)
    before_history = history_path.read_bytes()
    before_registry = registry_path.read_bytes()

    completed = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "replay-snapshot",
            str(RECONCILED),
            "--history",
            str(history_path),
            "--registry",
            str(registry_path),
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
    assert set(result["skipped_idempotent"]) == set(EXPECTED)
    assert result["wrote_files"] is False
    assert history_path.read_bytes() == before_history
    assert registry_path.read_bytes() == before_registry
