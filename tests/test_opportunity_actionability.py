import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "opportunity_actionability.py"
FIXTURE = ROOT / "tests" / "fixtures" / "opportunity_actionability.json"


def run_fixture(tmp_path: Path):
    report = tmp_path / "report.json"
    run = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--input",
            str(FIXTURE),
            "--as-of",
            "2026-08-18T08:00:00Z",
            "--output",
            str(report),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return run, json.loads(report.read_text(encoding="utf-8")) if report.exists() else None


def test_direct_script_separates_lifecycle_from_submission_phase(tmp_path):
    run, data = run_fixture(tmp_path)
    assert run.returncode == 0, run.stderr
    assert data["summary"] == {
        "total": 4,
        "states": {"closed": 1, "open": 1, "upcoming": 1, "verify": 1},
    }
    rows = {item["id"]: item for item in data["items"]}
    assert rows["surface-fuels-prize"]["state"] == "closed"
    assert rows["surface-fuels-prize"]["actionable"] is False
    assert rows["verified-open-example"]["state"] == "open"
    assert rows["verified-open-example"]["actionable"] is True
    assert rows["active-lifecycle-only"]["state"] == "verify"
    assert rows["active-lifecycle-only"]["actionable"] is False


def test_passed_deadline_closes_even_when_status_says_open(tmp_path):
    fixture = tmp_path / "input.json"
    fixture.write_text(json.dumps({"items": [{
        "id": "expired-open-label",
        "lifecycle_status": "active",
        "submission_status": "open",
        "submission_deadline": "2026-08-01T00:00:00Z",
    }]}), encoding="utf-8")
    report = tmp_path / "report.json"
    run = subprocess.run(
        [sys.executable, str(SCRIPT), "--input", str(fixture), "--as-of", "2026-08-18T08:00:00Z", "--output", str(report)],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    assert run.returncode == 0, run.stderr
    item = json.loads(report.read_text(encoding="utf-8"))["items"][0]
    assert item["state"] == "closed"
    assert item["reason"] == "submission deadline has passed"


def test_as_of_requires_timezone(tmp_path):
    run = subprocess.run(
        [sys.executable, str(SCRIPT), "--input", str(FIXTURE), "--as-of", "2026-08-18T08:00:00"],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    assert run.returncode != 0
    assert "timezone" in run.stderr.lower()
