import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "opportunity_evidence.py"
ACTIONABILITY = ROOT / "tools" / "opportunity_actionability.py"
FIXTURE = ROOT / "tests" / "fixtures" / "opportunity_status_evidence.json"


def test_direct_script_preserves_provenance_and_selects_latest(tmp_path):
    output = tmp_path / "normalized.json"
    run = subprocess.run(
        [sys.executable, str(SCRIPT), "--input", str(FIXTURE), "--output", str(output)],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    assert run.returncode == 0, run.stderr
    data = json.loads(output.read_text(encoding="utf-8"))
    assert data["summary"] == {"items": 2, "evidence_records": 6}
    rows = {item["id"]: item for item in data["items"]}
    assert rows["surface-fuels-prize"]["lifecycle_status"] == "active"
    assert rows["surface-fuels-prize"]["submission_status"] == "closed"
    assert len(rows["surface-fuels-prize"]["evidence"]) == 3
    assert rows["verified-open-example"]["submission_status"] == "open"
    selected = rows["verified-open-example"]["selected_evidence"]["submission_status"]
    assert any(row["evidence_sha256"] == selected and row["value"] == "open" for row in rows["verified-open-example"]["evidence"])


def test_normalized_output_feeds_actionability_evaluator(tmp_path):
    normalized = tmp_path / "normalized.json"
    first = subprocess.run(
        [sys.executable, str(SCRIPT), "--input", str(FIXTURE), "--output", str(normalized)],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    assert first.returncode == 0, first.stderr
    report = tmp_path / "actionability.json"
    second = subprocess.run(
        [sys.executable, str(ACTIONABILITY), "--input", str(normalized), "--as-of", "2026-08-19T12:00:00Z", "--output", str(report)],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    assert second.returncode == 0, second.stderr
    rows = {item["id"]: item for item in json.loads(report.read_text(encoding="utf-8"))["items"]}
    assert rows["surface-fuels-prize"]["state"] == "closed"
    assert rows["verified-open-example"]["state"] == "open"


def test_conflicting_newest_evidence_is_rejected(tmp_path):
    fixture = tmp_path / "conflict.json"
    fixture.write_text(json.dumps({"items": [{"id": "conflict", "evidence": [
        {"field": "submission_status", "value": "open", "source_url": "https://example.com/a", "observed_at": "2026-08-19T12:00:00Z", "excerpt": "Open."},
        {"field": "submission_status", "value": "closed", "source_url": "https://example.com/b", "observed_at": "2026-08-19T12:00:00Z", "excerpt": "Closed."}
    ]}]}), encoding="utf-8")
    run = subprocess.run(
        [sys.executable, str(SCRIPT), "--input", str(fixture)],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    assert run.returncode != 0
    assert "conflicting newest evidence" in run.stderr


def test_evidence_requires_https_timezone_and_excerpt(tmp_path):
    fixture = tmp_path / "invalid.json"
    fixture.write_text(json.dumps({"items": [{"id": "invalid", "evidence": [
        {"field": "submission_status", "value": "open", "source_url": "http://example.com", "observed_at": "2026-08-19T12:00:00", "excerpt": ""}
    ]}]}), encoding="utf-8")
    run = subprocess.run(
        [sys.executable, str(SCRIPT), "--input", str(fixture)],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    assert run.returncode != 0
    assert "timezone" in run.stderr.lower() or "https" in run.stderr.lower() or "excerpt" in run.stderr.lower()
