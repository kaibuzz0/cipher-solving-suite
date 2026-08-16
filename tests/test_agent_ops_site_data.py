from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def build_snapshot() -> dict:
    result = subprocess.run(
        [sys.executable, "scripts/build_agent_ops.py"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    return json.loads((ROOT / "site-data" / "agent-ops.json").read_text(encoding="utf-8"))


def test_agent_ops_snapshot_parses_priority_queue_and_current_state():
    payload = build_snapshot()
    assert payload["summary"]["queue_total"] >= 1
    assert payload["summary"]["queue_p1"] >= 1
    assert payload["queue"]["items"][0]["priority"].startswith("P")
    assert payload["current_state"]["default_branch"] == "main"
    assert payload["current_state"]["priorities"]
    assert payload["current_state"]["next_handoff"]


def test_agent_ops_snapshot_parses_handoffs_and_integration_queue():
    payload = build_snapshot()
    assert payload["recent_handoffs"]
    latest = payload["recent_handoffs"][0]
    assert latest["timestamp"]
    assert latest["agent"]
    assert latest["task"]
    assert "items" in payload["integration_queue"]
