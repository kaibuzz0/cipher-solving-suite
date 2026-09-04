import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_PATH = ROOT / "intelligence" / "feeds" / "2026-08-29-source-health.json"
HISTORY_PATH = ROOT / "data" / "source_check_history.json"
REGISTRY_PATH = ROOT / "data" / "intelligence_sources.json"
CHECKED_AT = "2026-08-29T07:38:35Z"

EXPECTED = {
    "challenge-gov": {
        "fingerprint": "9e063815d1081f098c97ab5981f71b4c2e94d00edba6ca61198d1d9b2e762045",
        "predecessor": "1d4ecd2dfb8dedb600589fa4980dfaa1ce96d71a63dd54201821af7fbfc32aed",
        "predecessor_checked_at": "2026-08-28T07:40:27Z",
    },
    "ctftime-upcoming": {
        "fingerprint": "33b5c83409f9f2704f19483a69440ce82525b23c05a7f5ef2d401ac816c0f2ce",
        "predecessor": "8ab1541b75153d193963da65855a7c07f99bf9a26bf701b45b1fbc754272a19b",
        "predecessor_checked_at": "2026-08-28T19:37:39Z",
    },
    "sherlock-bounties": {
        "fingerprint": "6aaa4c2de88200e0be6144cb024734167d513c9c79a1b11d6f283958bbd2b19f",
        "predecessor": "e86ebfff5d52fc612e515a6bb6a6b771131938816faceed5e1782d14957860c9",
        "predecessor_checked_at": "2026-08-28T07:40:27Z",
    },
    "arxiv-cryptography": {
        "fingerprint": "246032d40532baab6948400a0678b2421b6342024d13ae16258ac80583bb26c3",
        "predecessor": "b8cd96dfef25b74134fe858391b0aa4447f5b779bc46503443aaa8e23a00ef2c",
        "predecessor_checked_at": "2026-08-28T07:40:27Z",
    },
    "ethglobal-events": {
        "fingerprint": "5b270d1af189b17c8508993b6c5ed10d6794acec5e254eee7dc77f2c2f84925c",
        "predecessor": "8ae70a5efe8985d347d6fa3d8da1ee68767475a612395c3d1c9b150217fe6a24",
        "predecessor_checked_at": "2026-08-28T07:40:27Z",
    },
}


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


def test_aug29_snapshot_hashes_and_predecessors_are_replay_safe():
    snapshot = _load(SNAPSHOT_PATH)
    history = _load(HISTORY_PATH)

    assert snapshot["checked_at"] == CHECKED_AT
    observations = snapshot["observations"]
    assert {item["source_id"] for item in observations} == set(EXPECTED)

    for observation in observations:
        source_id = observation["source_id"]
        expected = EXPECTED[source_id]
        assert _canonical_hash(observation["observed"]) == observation["sha256"]
        assert observation["sha256"] == expected["fingerprint"]

        predecessor = _latest_before(history["checks"], source_id, CHECKED_AT)
        assert predecessor["content_fingerprint"] == expected["predecessor"]
        assert predecessor["checked_at"] == expected["predecessor_checked_at"]


def test_aug29_canonical_state_is_absent_or_exact_and_idempotent():
    history = _load(HISTORY_PATH)
    registry = _load(REGISTRY_PATH)
    registry_by_id = {source["id"]: source for source in registry["sources"]}

    for source_id, expected in EXPECTED.items():
        matching = [
            record
            for record in history["checks"]
            if record["source_id"] == source_id and record["checked_at"] == CHECKED_AT
        ]
        assert len(matching) <= 1, f"duplicate canonical Aug. 29 record for {source_id}"

        if matching:
            record = matching[0]
            assert record["content_fingerprint"] == expected["fingerprint"]
            assert record["previous_fingerprint"] == expected["predecessor"]
            assert registry_by_id[source_id]["last_checked_at"] == CHECKED_AT
        else:
            assert registry_by_id[source_id]["last_checked_at"] == expected["predecessor_checked_at"]
