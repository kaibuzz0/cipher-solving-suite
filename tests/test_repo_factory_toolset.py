from __future__ import annotations
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "toolsets" / "repo-factory" / "export_toolset.py"


def test_repo_factory_dry_run_lists_expected_files(tmp_path):
    result = subprocess.run(
        [sys.executable, str(SCRIPT), str(tmp_path), "--project-name", "Demo", "--dry-run"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    assert "AGENTS.md" in result.stdout
    assert "docs/PROJECT_BLUEPRINT.md" in result.stdout
    assert ".github/workflows/diagnostic-ci.yml" in result.stdout
    assert not (tmp_path / "AGENTS.md").exists()


def test_repo_factory_exports_and_refuses_overwrite(tmp_path):
    subprocess.run([sys.executable, str(SCRIPT), str(tmp_path), "--project-name", "Demo"], cwd=ROOT, check=True)
    assert "Demo" in (tmp_path / "AGENTS.md").read_text(encoding="utf-8")
    assert (tmp_path / "data" / "integration_queue.json").exists()
    second = subprocess.run([sys.executable, str(SCRIPT), str(tmp_path), "--project-name", "Demo"], cwd=ROOT, capture_output=True, text=True)
    assert second.returncode != 0
    assert "refusing to overwrite" in (second.stdout + second.stderr)
