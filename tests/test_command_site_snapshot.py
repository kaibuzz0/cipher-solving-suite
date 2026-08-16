import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_command_site_snapshot_export(tmp_path):
    output = tmp_path / "repo-snapshot.json"
    proc = subprocess.run(
        [sys.executable, "scripts/export_command_site_snapshot.py", "--output", str(output)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    data = json.loads(output.read_text(encoding="utf-8"))
    assert data["schema_version"] == 1
    assert data["repo"]["id"] == "cipher-solving-suite"
    assert data["repo"]["full_name"] == "kaibuzz0/cipher-solving-suite"
    assert data["repo"]["url"].startswith("https://")
    assert data["source_commit"]
    for key in (
        "tools",
        "toolsets",
        "cases",
        "opportunities",
        "intelligence",
        "sources",
        "prompts",
        "evidence",
        "activity",
        "links",
    ):
        assert isinstance(data[key], list)
    assert isinstance(data["agent_ops"], dict)
    assert isinstance(data["stats"], dict)


def test_command_site_snapshot_is_bounded_metadata_only():
    text = (ROOT / "scripts/export_command_site_snapshot.py").read_text(encoding="utf-8")
    assert "private key" not in text.lower()
    assert "wallet seed" not in text.lower()
    assert "repo-snapshot.json" in text
