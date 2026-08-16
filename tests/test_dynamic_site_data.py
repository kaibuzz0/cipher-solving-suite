from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def build_site_data() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/build_site_data.py"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_build_site_data_discovers_repo_factory_toolset():
    build_site_data()
    payload = json.loads((ROOT / "site-data" / "toolsets.json").read_text(encoding="utf-8"))
    items = {item["id"]: item for item in payload["items"]}

    assert "repo-factory" in items
    repo_factory = items["repo-factory"]
    assert repo_factory["registered"] is True
    assert repo_factory["health"] == "ok"
    assert repo_factory["manifest_path"] == "toolsets/repo-factory/toolset.json"
    assert repo_factory["readme_path"] == "toolsets/repo-factory/README.md"
    assert "toolsets/repo-factory/export_toolset.py" in repo_factory["files"]
    assert any(tool["id"] == "repo-factory-exporter" for tool in repo_factory["tools"])
    assert payload["summary"]["total"] >= 1


def test_repository_browser_indexes_bounded_safe_text_previews():
    build_site_data()
    payload = json.loads((ROOT / "site-data" / "repository.json").read_text(encoding="utf-8"))
    files = {item["path"]: item for item in payload["files"]}

    assert "toolsets/repo-factory/README.md" in files
    assert "toolsets/repo-factory/export_toolset.py" in files
    assert files["toolsets/repo-factory/README.md"]["previewable"] is True
    assert "Repo Factory" in files["toolsets/repo-factory/README.md"]["preview"]
    assert files["toolsets/repo-factory/export_toolset.py"]["previewable"] is True
    assert payload["summary"]["files"] >= payload["summary"]["previewable"] >= 1
    assert "toolsets" in payload["roots"]
    assert "tools" in payload["roots"]


def test_status_includes_toolset_and_repository_counts():
    build_site_data()
    status = json.loads((ROOT / "site-data" / "status.json").read_text(encoding="utf-8"))
    toolsets = json.loads((ROOT / "site-data" / "toolsets.json").read_text(encoding="utf-8"))
    repository = json.loads((ROOT / "site-data" / "repository.json").read_text(encoding="utf-8"))

    assert status["toolsets"] == toolsets["summary"]["total"]
    assert status["toolsets_needing_attention"] == toolsets["summary"]["needs_attention"]
    assert status["repository_files"] == repository["summary"]["files"]
    assert status["previewable_files"] == repository["summary"]["previewable"]
