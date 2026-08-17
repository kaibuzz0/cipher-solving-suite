import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "catalog_link_health.py"


def write_catalog(path: Path) -> None:
    path.write_text(json.dumps({"items": [
        {"id": "a", "source_url": "https://example.com/old"},
        {"id": "b", "url": "https://example.org/current"},
    ]}), encoding="utf-8")


def test_direct_script_inventory_is_deterministic(tmp_path):
    catalog = tmp_path / "catalog.json"
    report = tmp_path / "report.json"
    write_catalog(catalog)
    run = subprocess.run(
        [sys.executable, str(SCRIPT), "inventory", "--input", str(catalog), "--output", str(report)],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    assert run.returncode == 0, run.stderr
    data = json.loads(report.read_text(encoding="utf-8"))
    assert data["summary"] == {"total": 2, "states": {"valid": 2}}
    assert [x["url"] for x in data["items"]] == ["https://example.com/old", "https://example.org/current"]


def test_replay_detects_migration_and_http_error(tmp_path):
    catalog = tmp_path / "catalog.json"
    fixtures = tmp_path / "fixtures.json"
    report = tmp_path / "report.json"
    write_catalog(catalog)
    fixtures.write_text(json.dumps({
        "https://example.com/old": {"status": 200, "final_url": "https://example.com/new", "error": None},
        "https://example.org/current": {"status": 404, "final_url": "https://example.org/current", "error": "HTTP 404"},
    }), encoding="utf-8")
    run = subprocess.run(
        [sys.executable, str(SCRIPT), "replay", "--input", str(catalog), "--fixture-map", str(fixtures), "--output", str(report)],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    assert run.returncode == 0, run.stderr
    data = json.loads(report.read_text(encoding="utf-8"))
    assert data["summary"]["states"] == {"http-error": 1, "migrated": 1}
    migrated = next(x for x in data["items"] if x["state"] == "migrated")
    assert migrated["final_url"] == "https://example.com/new"


def test_invalid_non_https_url_fails_validation(tmp_path):
    catalog = tmp_path / "catalog.json"
    catalog.write_text(json.dumps({"source_url": "http://example.com"}), encoding="utf-8")
    run = subprocess.run(
        [sys.executable, str(SCRIPT), "inventory", "--input", str(catalog)],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    assert run.returncode == 1
    assert '"invalid": 1' in run.stdout
