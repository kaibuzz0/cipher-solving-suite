from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_build_site_data_discovers_repo_factory_toolset():
    result = subprocess.run(
        [sys.executable, "scripts/build_site_data.py"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr

    payload = json.loads((ROOT / "site-data" / "toolsets.json").read_text(encoding="utf-8"))
    items = {item["id"]: item for item in payload["items"]}

    assert "repo-factory" in items
    repo_factory = items["repo-factory"]
    assert repo_factory["registered"] is True
    assert repo_factory["health"] == "ok"
    assert repo_factory["manifest_path"] == "toolsets/repo-factory/toolset.json"
    assert repo_factory["readme_path"] == "toolsets/repo-factory/README.md"
    assert payload["summary"]["total"] >= 1


def test_status_includes_toolset_counts():
    subprocess.run([sys.executable, "scripts/build_site_data.py"], cwd=ROOT, check=True)
    status = json.loads((ROOT / "site-data" / "status.json").read_text(encoding="utf-8"))
    toolsets = json.loads((ROOT / "site-data" / "toolsets.json").read_text(encoding="utf-8"))

    assert status["toolsets"] == toolsets["summary"]["total"]
    assert status["toolsets_needing_attention"] == toolsets["summary"]["needs_attention"]
