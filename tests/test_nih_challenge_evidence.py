import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "nih_challenge_evidence.py"
NORMALIZER = ROOT / "tools" / "opportunity_evidence.py"
FIXTURE = ROOT / "tests" / "fixtures" / "nih_challenges.html"


def run_adapter(tmp_path, title, item_id):
    output = tmp_path / "evidence.json"
    run = subprocess.run(
        [
            sys.executable, str(SCRIPT),
            "--title", title,
            "--id", item_id,
            "--observed-at", "2026-08-20T19:55:00Z",
            "--input-html", str(FIXTURE),
            "--output", str(output),
        ],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    assert run.returncode == 0, run.stderr
    return output, json.loads(output.read_text(encoding="utf-8"))


def test_nci_date_only_status_emits_open_evidence_without_invented_deadline(tmp_path):
    _, data = run_adapter(tmp_path, "NCI Office of Data Sharing Impact Prize", "nci-ods-impact-prize")
    evidence = data["items"][0]["evidence"]
    fields = {row["field"]: row for row in evidence}
    assert fields["lifecycle_status"]["value"] == "active"
    assert fields["submission_status"]["value"] == "open"
    assert "submission_deadline" not in fields
    assert fields["submission_status"]["source_url"] == "https://www.nih.gov/challenges"
    assert "Open 08/03/2026 to 10/05/2026" in fields["submission_status"]["excerpt"]


def test_exact_et_deadline_is_timezone_aware_and_feeds_normalizer(tmp_path):
    evidence_path, data = run_adapter(tmp_path, "LymeX Healthathon", "lymex-healthathon")
    rows = {row["field"]: row for row in data["items"][0]["evidence"]}
    assert rows["submission_deadline"]["value"] == "2026-08-21T23:59:00-04:00"

    normalized = tmp_path / "normalized.json"
    run = subprocess.run(
        [sys.executable, str(NORMALIZER), "--input", str(evidence_path), "--output", str(normalized)],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    assert run.returncode == 0, run.stderr
    item = json.loads(normalized.read_text(encoding="utf-8"))["items"][0]
    assert item["submission_status"] == "open"
    assert item["submission_deadline"] == "2026-08-21T23:59:00-04:00"
    assert item["selected_evidence"]["submission_deadline"]


def test_open_data_description_does_not_shadow_phase_status(tmp_path):
    _, data = run_adapter(
        tmp_path,
        "TOPx HHS Tech Sprint for AI and Invisible Illness",
        "topx-hhs-tech-sprint",
    )
    rows = {row["field"]: row for row in data["items"][0]["evidence"]}
    assert rows["submission_status"]["value"] == "open"
    assert rows["submission_status"]["excerpt"].startswith("Phase 2 open 07/29/26")
    assert "Open Data" not in rows["submission_status"]["excerpt"]
    assert rows["submission_deadline"]["value"] == "2026-10-15T23:59:00-04:00"


def test_missing_title_fails_without_writing_output(tmp_path):
    output = tmp_path / "evidence.json"
    run = subprocess.run(
        [
            sys.executable, str(SCRIPT),
            "--title", "Missing Challenge",
            "--id", "missing",
            "--observed-at", "2026-08-20T19:55:00Z",
            "--input-html", str(FIXTURE),
            "--output", str(output),
        ],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    assert run.returncode != 0
    assert not output.exists()
    assert "expected exactly one NIH challenge card" in run.stderr


def test_observed_at_requires_timezone(tmp_path):
    output = tmp_path / "evidence.json"
    run = subprocess.run(
        [
            sys.executable, str(SCRIPT),
            "--title", "LymeX Healthathon",
            "--id", "lymex-healthathon",
            "--observed-at", "2026-08-20T19:55:00",
            "--input-html", str(FIXTURE),
            "--output", str(output),
        ],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    assert run.returncode != 0
    assert not output.exists()
    assert "timezone" in run.stderr.lower()
