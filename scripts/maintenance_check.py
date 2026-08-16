#!/usr/bin/env python3
"""Cheap, deterministic repository hygiene checks for CI and AI agents."""

from __future__ import annotations

import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "artifacts" / "maintenance-report.json"

REQUIRED = [
    ROOT / "AGENTS.md",
    ROOT / "docs" / "AGENT_HANDOFF.md",
    ROOT / "docs" / "REPO_MAINTENANCE.md",
    ROOT / "README.md",
    ROOT / "suite.py",
]

GENERATED_ROOT_SUFFIXES = {".bin", ".png", ".jpg", ".jpeg", ".gif", ".log", ".csv"}
SECRET_NAME_RE = re.compile(r"(^|[._-])(secret|token|apikey|api_key|private[_-]?key|seed)([._-]|$)", re.I)
VERSION_RE = re.compile(r"\b(?:v|version\s*)?(\d+\.\d+(?:\.\d+)?)\b", re.I)


def compile_python(path: Path) -> dict[str, object]:
    proc = subprocess.run(
        ["python", "-m", "py_compile", str(path)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    return {
        "path": str(path.relative_to(ROOT)),
        "ok": proc.returncode == 0,
        "stderr": proc.stderr.strip(),
    }


def extract_versions(path: Path) -> list[str]:
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8", errors="replace")
    return sorted(set(VERSION_RE.findall(text)))


def main() -> int:
    missing = [str(p.relative_to(ROOT)) for p in REQUIRED if not p.exists()]

    compile_targets = [ROOT / "suite.py"]
    for candidate in [
        ROOT / "tools" / "opportunity_finder.py",
        ROOT / "tools" / "earnings_tracker.py",
        ROOT / "tools" / "scanning" / "opportunity_scanner.py",
    ]:
        if candidate.exists():
            compile_targets.append(candidate)
    compile_results = [compile_python(p) for p in compile_targets]

    root_generated = sorted(
        p.name
        for p in ROOT.iterdir()
        if p.is_file() and p.suffix.lower() in GENERATED_ROOT_SUFFIXES
    )

    suspicious_names = sorted(
        str(p.relative_to(ROOT))
        for p in ROOT.rglob("*")
        if p.is_file() and SECRET_NAME_RE.search(p.name)
    )

    readme_versions = extract_versions(ROOT / "README.md")
    suite_versions = extract_versions(ROOT / "suite.py")
    shared_versions = sorted(set(readme_versions).intersection(suite_versions))

    findings = []
    if missing:
        findings.append({"severity": "error", "kind": "missing_required_files", "items": missing})
    failed_compile = [r for r in compile_results if not r["ok"]]
    if failed_compile:
        findings.append({"severity": "error", "kind": "python_compile_failure", "items": failed_compile})
    if readme_versions and suite_versions and not shared_versions:
        findings.append({
            "severity": "warning",
            "kind": "version_drift",
            "readme_versions": readme_versions,
            "suite_versions": suite_versions,
        })
    if root_generated:
        findings.append({"severity": "warning", "kind": "generated_files_at_repo_root", "items": root_generated})
    if suspicious_names:
        findings.append({"severity": "warning", "kind": "secret_like_filenames", "items": suspicious_names})

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "error" if any(f["severity"] == "error" for f in findings) else "ok",
        "compile": compile_results,
        "findings": findings,
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(payload, indent=2))
    return 1 if payload["status"] == "error" else 0


if __name__ == "__main__":
    raise SystemExit(main())
