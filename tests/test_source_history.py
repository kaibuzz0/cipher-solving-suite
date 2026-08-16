import json
import tempfile
from pathlib import Path

import scripts.source_check_history as history


def test_repository_history_is_valid():
    assert history.validate_history(history.load_history()) == []


def test_fingerprint_is_deterministic():
    assert history.normalize_fingerprint(" Example State ") == history.normalize_fingerprint("example state")


def test_record_check_detects_first_unchanged_and_changed():
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "history.json"
        first = history.record_check(
            "ethglobal-events",
            "event-a,event-b",
            checked_at="2026-08-16T10:00:00Z",
            history_path=path,
            update_registry=False,
        )
        same = history.record_check(
            "ethglobal-events",
            "EVENT-A,EVENT-B",
            checked_at="2026-08-16T11:00:00Z",
            history_path=path,
            update_registry=False,
        )
        changed = history.record_check(
            "ethglobal-events",
            "event-a,event-b,event-c",
            checked_at="2026-08-16T12:00:00Z",
            history_path=path,
            update_registry=False,
        )
        assert first["change_state"] == "first-seen"
        assert same["change_state"] == "unchanged"
        assert changed["change_state"] == "changed"
        saved = json.loads(path.read_text(encoding="utf-8"))
        assert len(saved["checks"]) == 3
        assert history.validate_history(saved) == []


def test_latest_check_returns_newest_entry():
    data = {
        "checks": [
            {"source_id": "ctftime-upcoming", "checked_at": "2026-08-16T10:00:00Z"},
            {"source_id": "ctftime-upcoming", "checked_at": "2026-08-16T12:00:00Z"},
        ]
    }
    assert history.latest_check(data, "ctftime-upcoming")["checked_at"] == "2026-08-16T12:00:00Z"
