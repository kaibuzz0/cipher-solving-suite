from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

from scripts.source_check_history import replay_snapshot

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL = ROOT / "intelligence" / "feeds" / "2026-08-28-afternoon-source-health.json"
RECONCILED = ROOT / "intelligence" / "feeds" / "2026-08-28-afternoon-source-health-reconciled.json"
HISTORY = ROOT / "data" / "source_check_history.json"
REGISTRY = ROOT / "data" / "intelligence_sources.json"
SCRIPT = ROOT / "scripts" / "source_check_history.py"
STAMP = "2026-08-28T19:37:39Z"

EXPECTED = {
    "ctftime-upcoming": (
        "78ef14e4f60d3e23981176686b6ca9d6b26cd23a222fdd1bf0773e4037613ae8",
        "8ab1541b75153d193963da65855a7c07f99bf9a26bf701b45b1fbc754272a19b",
        "ab0660900275cf3767cd9b2f49f4bd08c2c0e2f68fa6f074ae1f2f55e66b380f",
    ),
    "github-search": (
        "7ea7f35a0c4f8f8d194af4c8004836769e3a8752193c2a3099180124fbd01c0e",
        "db0ecb913bc55b1de3b637f97325c14ac439c4531e7494144a8db792c457622b",
        "993f3601dafc2f452f9267c79a861f1e4de5e33e0065e7be100191cdd95dcca9",
    ),
}


def _temp_canonical_files(tmp_path: Path) -> tuple[Path, Path]:
    history = tmp_path / "source_check_history.json"
    registry = tmp_path / "intelligence_sources.json"
    shutil.copy2(HISTORY, history)
    shutil.copy2(REGISTRY, registry)
    return history, registry


def test_aug28_afternoon_reconciliation_preserves_raw_provenance_and_predecessors(tmp_path):
    original = json.loads(ORIGINAL.read_text(encoding="utf-8"))
    reconciled = json.loads(RECONCILED.read_text(encoding="utf-8"))
    history = json.loads(HISTORY.read_text(encoding="utf-8"))

    assert original["checked_at"] == reconciled["checked_at"] == STAMP
    assert reconciled["reconciliation"]["original_commit"] == "cc9176a943980bc48d02247887a5196702cc026e"
    assert reconciled["reconciliation"]["merged_commit"] == "b14f45920b9557cb95142b8da64ad90f98f35c8b"

    original_by_id = {item["source_id"]: item for item in original["observations"]}
    reconciled_by_id = {item["source_id"]: item for item in reconciled["observations"]}
    assert set(original_by_id) == set(reconciled_by_id) == set(EXPECTED)

    for source_id, (bad_hash, corrected_hash, predecessor) in EXPECTED.items():
        raw_item = original_by_id[source_id]
        corrected_item = reconciled_by_id[source_id]
        assert raw_item["observed"] == corrected_item["observed"]
        assert raw_item["sha256"] == bad_hash
        assert reconciled["reconciliation"]["original_hashes"][source_id] == bad_hash
        actual = hashlib.sha256(corrected_item["observed"].strip().lower().encode("utf-8")).hexdigest()
        assert actual == corrected_hash
        assert corrected_item["sha256"] == corrected_hash

        latest = next(item for item in history["checks"] if item["source_id"] == source_id)
        assert latest["content_fingerprint"] == predecessor
        assert not any(
            item["source_id"] == source_id and item["checked_at"] == STAMP
            for item in history["checks"]
        )

    history_path, registry_path = _temp_canonical_files(tmp_path)
    before_history = history_path.read_bytes()
    before_registry = registry_path.read_bytes()
    result = replay_snapshot(
        RECONCILED,
        history_path=history_path,
        registry_path=registry_path,
        write=False,
    )

    assert result["validated_observations"] == 2
    assert set(result["replayed"]) == set(EXPECTED)
    assert result["skipped_idempotent"] == []
    assert result["wrote_files"] is False
    assert history_path.read_bytes() == before_history
    assert registry_path.read_bytes() == before_registry


def test_aug28_afternoon_reconciled_direct_script_dry_run(tmp_path):
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
            "--dry-run",
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode == 0, completed.stderr
    result = json.loads(completed.stdout)
    assert result["validated_observations"] == 2
    assert set(result["replayed"]) == set(EXPECTED)
    assert result["skipped_idempotent"] == []
    assert result["wrote_files"] is False
    assert history_path.read_bytes() == before_history
    assert registry_path.read_bytes() == before_registry
