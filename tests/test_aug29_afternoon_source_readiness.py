import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_PATH = ROOT / "intelligence" / "feeds" / "2026-08-29-afternoon-source-health.json"
HISTORY_PATH = ROOT / "data" / "source_check_history.json"
REGISTRY_PATH = ROOT / "data" / "intelligence_sources.json"
CHECKED_AT = "2026-08-29T19:40:52Z"
SOURCE_ID = "ethglobal-events"
EXPECTED_FINGERPRINT = "361c6c0ce2988ea281442a7b6b6ac8ca94574cda8074242b2d7966fed9037179"
EXPECTED_PREDECESSOR = "5b270d1af189b17c8508993b6c5ed10d6794acec5e254eee7dc77f2c2f84925c"
EXPECTED_PREDECESSOR_CHECKED_AT = "2026-08-29T07:38:35Z"


def _load(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _canonical_hash(observed: str) -> str:
    return hashlib.sha256(observed.strip().lower().encode("utf-8")).hexdigest()


def _latest_before(checks, source_id: str, checked_at: str):
    candidates = [
        record
        for record in checks
        if record["source_id"] == source_id and record["checked_at"] < checked_at
    ]
    assert candidates, f"missing predecessor history for {source_id}"
    return max(candidates, key=lambda record: record["checked_at"])


def test_aug29_afternoon_snapshot_hash_and_predecessor_are_replay_safe():
    snapshot = _load(SNAPSHOT_PATH)
    history = _load(HISTORY_PATH)

    assert snapshot["checked_at"] == CHECKED_AT
    observations = snapshot["observations"]
    assert len(observations) == 1

    observation = observations[0]
    assert observation["source_id"] == SOURCE_ID
    assert _canonical_hash(observation["observed"]) == observation["sha256"]
    assert observation["sha256"] == EXPECTED_FINGERPRINT

    predecessor = _latest_before(history["checks"], SOURCE_ID, CHECKED_AT)
    assert predecessor["content_fingerprint"] == EXPECTED_PREDECESSOR
    assert predecessor["checked_at"] == EXPECTED_PREDECESSOR_CHECKED_AT


def test_aug29_afternoon_canonical_state_is_absent_or_exact_and_idempotent():
    history = _load(HISTORY_PATH)
    registry = _load(REGISTRY_PATH)
    registry_by_id = {source["id"]: source for source in registry["sources"]}

    matching = [
        record
        for record in history["checks"]
        if record["source_id"] == SOURCE_ID and record["checked_at"] == CHECKED_AT
    ]
    assert len(matching) <= 1, "duplicate canonical Aug. 29 afternoon ETHGlobal record"

    if matching:
        record = matching[0]
        assert record["content_fingerprint"] == EXPECTED_FINGERPRINT
        assert record["previous_fingerprint"] == EXPECTED_PREDECESSOR
        assert registry_by_id[SOURCE_ID]["last_checked_at"] >= CHECKED_AT
    else:
        assert registry_by_id[SOURCE_ID]["last_checked_at"] == EXPECTED_PREDECESSOR_CHECKED_AT
