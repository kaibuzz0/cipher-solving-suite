from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from scripts.source_check_history import replay_snapshot

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL = ROOT / "intelligence" / "feeds" / "2026-08-28-source-health.json"
RECONCILED = ROOT / "intelligence" / "feeds" / "2026-08-28-source-health-reconciled.json"
HISTORY = ROOT / "data" / "source_check_history.json"
REGISTRY = ROOT / "data" / "intelligence_sources.json"
SCRIPT = ROOT / "scripts" / "source_check_history.py"
STAMP = "2026-08-28T07:40:27Z"

EXPECTED = {
    "challenge-gov": (
        "d3b363da64284c57f7979e54b4744e9b33a6ed2594c0c7d82e62d495e7ec9457",
        "1d4ecd2dfb8dedb600589fa4980dfaa1ce96d71a63dd54201821af7fbfc32aed",
        "c0e125df5360a452d731c08f76412c7d62381054fca56e6fcb4e2184575d12cf",
    ),
    "ctftime-upcoming": (
        "603fd2ec4fb8f44f8509b1736d763250216f449ac02b640445c4a573bce17cd7",
        "ab0660900275cf3767cd9b2f49f4bd08c2c0e2f68fa6f074ae1f2f55e66b380f",
        "ef2d96986e610ccbfbb877ba67ddc2c5f975182de29629b4401a34a81e0d4add",
    ),
    "sherlock-bounties": (
        "d8decc8eda696d2fb172d69e0bb05f903073838aeaa7729901da7cb0ef303690",
        "e86ebfff5d52fc612e515a6bb6a6b771131938816faceed5e1782d14957860c9",
        "67f240a38ead70926e9776f3e5aa3afb6dc25920b3f7c555f34c7b9dbe262b05",
    ),
    "arxiv-cryptography": (
        "67865b863b0f73b671cf8fd86b3991462bc4e64385de92b54dc1cdf5da40d86d",
        "b8cd96dfef25b74134fe858391b0aa4447f5b779bc46503443aaa8e23a00ef2c",
        "d126279a1ebded4a02bb4dca40b381c8cf72484831d9913bf924ae5ebfc2b1c9",
    ),
    "ethglobal-events": (
        "c908d7693ae229b80276b92560a5973840336fb47d96c0d3ca1f62ce2191defe",
        "8ae70a5efe8985d347d6fa3d8da1ee68767475a612395c3d1c9b150217fe6a24",
        "9f0a188daf173966ee324470229a9bfbf2e864807b8f46200ea17f6bca9741dc",
    ),
}


def _as_datetime(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _temp_canonical_files(tmp_path: Path) -> tuple[Path, Path]:
    history = tmp_path / "source_check_history.json"
    registry = tmp_path / "intelligence_sources.json"
    shutil.copy2(HISTORY, history)
    shutil.copy2(REGISTRY, registry)
    return history, registry


def test_aug28_reconciliation_preserves_raw_provenance_and_is_canonical(tmp_path):
    original = json.loads(ORIGINAL.read_text(encoding="utf-8"))
    reconciled = json.loads(RECONCILED.read_text(encoding="utf-8"))
    history = json.loads(HISTORY.read_text(encoding="utf-8"))
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))

    assert original["checked_at"] == reconciled["checked_at"] == STAMP
    assert reconciled["reconciliation"]["original_commit"] == "d5ff98508d08a4d29633735e44fc5d0eec41c6e2"
    assert reconciled["reconciliation"]["merged_commit"] == "b14f45920b9557cb95142b8da64ad90f98f35c8b"
    assert _as_datetime(history["updated_at"]) >= _as_datetime(STAMP)
    assert _as_datetime(registry["updated_at"]) >= _as_datetime(STAMP)

    original_by_id = {item["source_id"]: item for item in original["observations"]}
    reconciled_by_id = {item["source_id"]: item for item in reconciled["observations"]}
    registry_by_id = {item["id"]: item for item in registry["sources"]}
    assert set(original_by_id) == set(reconciled_by_id) == set(EXPECTED)

    for source_id, (bad_hash, corrected_hash, predecessor) in EXPECTED.items():
        original_item = original_by_id[source_id]
        corrected_item = reconciled_by_id[source_id]
        assert original_item["observed"] == corrected_item["observed"]
        assert original_item["sha256"] == bad_hash
        assert reconciled["reconciliation"]["original_hashes"][source_id] == bad_hash
        actual = hashlib.sha256(corrected_item["observed"].strip().lower().encode("utf-8")).hexdigest()
        assert actual == corrected_hash
        assert corrected_item["sha256"] == corrected_hash

        canonical = [
            item for item in history["checks"]
            if item["source_id"] == source_id and item["checked_at"] == STAMP
        ]
        assert len(canonical) == 1
        assert canonical[0]["content_fingerprint"] == corrected_hash
        assert canonical[0]["previous_fingerprint"] == predecessor
        assert canonical[0]["change_state"] == "changed"
        assert _as_datetime(registry_by_id[source_id]["last_checked_at"]) >= _as_datetime(STAMP)

    history_path, registry_path = _temp_canonical_files(tmp_path)
    before_history = history_path.read_bytes()
    before_registry = registry_path.read_bytes()
    result = replay_snapshot(
        RECONCILED,
        history_path=history_path,
        registry_path=registry_path,
        write=False,
    )

    assert result["validated_observations"] == 5
    assert result["replayed"] == []
    assert set(result["skipped_idempotent"]) == set(EXPECTED)
    assert result["wrote_files"] is False
    assert history_path.read_bytes() == before_history
    assert registry_path.read_bytes() == before_registry


def test_aug28_reconciled_direct_script_replay_is_idempotent(tmp_path):
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
    assert result["validated_observations"] == 5
    assert result["replayed"] == []
    assert set(result["skipped_idempotent"]) == set(EXPECTED)
    assert result["wrote_files"] is False
    assert history_path.read_bytes() == before_history
    assert registry_path.read_bytes() == before_registry
