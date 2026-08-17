#!/usr/bin/env python3
"""Inventory and optionally verify HTTPS links in canonical repository catalogs.

Default mode is deterministic and network-free: it inventories URLs and validates
basic URL shape. ``check`` performs bounded live requests and reports redirects,
HTTP failures, and likely source migrations without mutating canonical data.
``replay`` consumes a fixture response map for deterministic CI verification.
"""
from __future__ import annotations

import argparse
import json
import urllib.error
import urllib.request
from dataclasses import dataclass, asdict
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUTS = (
    ROOT / "data" / "intelligence_sources.json",
    ROOT / "data" / "intelligence.json",
    ROOT / "data" / "opportunities.json",
)


@dataclass(frozen=True)
class LinkRef:
    source_file: str
    json_path: str
    url: str


def source_label(source_file: Path) -> str:
    """Use repo-relative paths for canonical files and stable absolute paths for external fixtures."""
    try:
        return str(source_file.relative_to(ROOT))
    except ValueError:
        return str(source_file)


def _walk(value, source_file: Path, path: str = "$") -> list[LinkRef]:
    refs: list[LinkRef] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if isinstance(child, str) and key.lower().endswith(("url", "uri", "link")):
                refs.append(LinkRef(source_label(source_file), child_path, child))
            refs.extend(_walk(child, source_file, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            refs.extend(_walk(child, source_file, f"{path}[{index}]"))
    return refs


def inventory(paths: list[Path]) -> list[LinkRef]:
    refs: list[LinkRef] = []
    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        refs.extend(_walk(data, path))
    unique: dict[tuple[str, str, str], LinkRef] = {}
    for ref in refs:
        unique[(ref.source_file, ref.json_path, ref.url)] = ref
    return sorted(unique.values(), key=lambda item: (item.source_file, item.json_path, item.url))


def classify_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme != "https" or not parsed.netloc:
        return "invalid"
    return "valid"


def live_probe(url: str, timeout: float) -> dict:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "cipher-solving-suite-link-health/1"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            final = response.geturl()
            status = int(getattr(response, "status", 200))
            return {"status": status, "final_url": final, "error": None}
    except urllib.error.HTTPError as exc:
        return {"status": int(exc.code), "final_url": exc.geturl() or url, "error": f"HTTP {exc.code}"}
    except Exception as exc:  # network/DNS/TLS failures are report data, not crashes
        return {"status": None, "final_url": url, "error": f"{type(exc).__name__}: {exc}"}


def result_for(ref: LinkRef, probe: dict | None = None) -> dict:
    shape = classify_url(ref.url)
    row = {**asdict(ref), "shape": shape, "status": None, "final_url": ref.url, "state": shape, "error": None}
    if shape == "invalid" or probe is None:
        return row
    row["status"] = probe.get("status")
    row["final_url"] = probe.get("final_url") or ref.url
    row["error"] = probe.get("error")
    status = row["status"]
    if row["final_url"] != ref.url and status is not None and 200 <= status < 400:
        row["state"] = "migrated"
    elif status is not None and 200 <= status < 400:
        row["state"] = "healthy"
    elif status is not None:
        row["state"] = "http-error"
    else:
        row["state"] = "network-error"
    return row


def summary(rows: list[dict]) -> dict:
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["state"]] = counts.get(row["state"], 0) + 1
    return {"total": len(rows), "states": dict(sorted(counts.items()))}


def write_report(rows: list[dict], output: Path | None) -> dict:
    report = {"schema_version": 1, "summary": summary(rows), "items": rows}
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", nargs="?", choices=("inventory", "check", "replay"), default="inventory")
    parser.add_argument("--input", action="append", dest="inputs", help="JSON catalog path; repeatable")
    parser.add_argument("--fixture-map", help="Replay map keyed by URL with status/final_url/error fields")
    parser.add_argument("--output", help="Optional JSON report path")
    parser.add_argument("--max-urls", type=int, default=100, help="Bound live/replay checks (default: 100)")
    parser.add_argument("--timeout", type=float, default=8.0, help="Per-request live timeout seconds")
    args = parser.parse_args(argv)

    paths = [Path(p).resolve() for p in args.inputs] if args.inputs else list(DEFAULT_INPUTS)
    refs = inventory(paths)
    probes: dict[str, dict] = {}
    if args.mode == "replay":
        if not args.fixture_map:
            parser.error("replay requires --fixture-map")
        probes = json.loads(Path(args.fixture_map).read_text(encoding="utf-8"))
    elif args.mode == "check":
        for ref in refs[: max(args.max_urls, 0)]:
            if classify_url(ref.url) == "valid" and ref.url not in probes:
                probes[ref.url] = live_probe(ref.url, max(args.timeout, 0.1))

    rows = []
    checked = set(ref.url for ref in refs[: max(args.max_urls, 0)]) if args.mode != "inventory" else set()
    for ref in refs:
        probe = probes.get(ref.url) if ref.url in checked else None
        rows.append(result_for(ref, probe))

    report = write_report(rows, Path(args.output) if args.output else None)
    print(json.dumps(report["summary"], indent=2))
    return 1 if report["summary"]["states"].get("invalid", 0) else 0


if __name__ == "__main__":
    raise SystemExit(main())
