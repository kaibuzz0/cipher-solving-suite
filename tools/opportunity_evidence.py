#!/usr/bin/env python3
"""Normalize preserved opportunity phase/deadline evidence into evaluator-ready records.

The input is local JSON evidence captured from already-reviewed sources. This tool does
not fetch the network or mutate canonical opportunity data. It validates source URLs,
requires timezone-aware observation timestamps, retains every evidence statement, and
selects the newest non-conflicting statement per supported field. Output can be passed
directly to ``tools/opportunity_actionability.py``.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

ALLOWED_FIELDS = {"lifecycle_status", "submission_status", "submission_deadline"}


def parse_time(value: str) -> datetime:
    text = str(value).strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    dt = datetime.fromisoformat(text)
    if dt.tzinfo is None:
        raise ValueError("timestamp must include timezone information")
    return dt.astimezone(timezone.utc)


def canonical_hash(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def validate_url(value: str) -> str:
    url = str(value).strip()
    parsed = urlparse(url)
    if parsed.scheme != "https" or not parsed.netloc:
        raise ValueError("source_url must be an absolute https URL")
    return url


def normalize_record(raw: dict[str, Any]) -> dict[str, Any]:
    field = str(raw.get("field") or "").strip()
    if field not in ALLOWED_FIELDS:
        raise ValueError(f"unsupported evidence field: {field or '<empty>'}")
    value = str(raw.get("value") or "").strip()
    if not value:
        raise ValueError(f"evidence value is required for {field}")
    observed_at = str(raw.get("observed_at") or "").strip()
    observed_dt = parse_time(observed_at)
    source_url = validate_url(raw.get("source_url") or "")
    excerpt = str(raw.get("excerpt") or "").strip()
    if not excerpt:
        raise ValueError(f"excerpt is required for {field}")
    if field == "submission_deadline":
        parse_time(value)

    normalized = {
        "field": field,
        "value": value,
        "source_url": source_url,
        "observed_at": observed_dt.isoformat().replace("+00:00", "Z"),
        "excerpt": excerpt,
    }
    if raw.get("source_name"):
        normalized["source_name"] = str(raw["source_name"]).strip()
    normalized["evidence_sha256"] = canonical_hash(normalized)
    return normalized


def normalize_item(raw: dict[str, Any]) -> dict[str, Any]:
    item_id = str(raw.get("id") or "").strip()
    if not item_id:
        raise ValueError("every item requires id")
    evidence_raw = raw.get("evidence")
    if not isinstance(evidence_raw, list) or not evidence_raw:
        raise ValueError(f"{item_id}: evidence must be a non-empty list")
    if not all(isinstance(record, dict) for record in evidence_raw):
        raise ValueError(f"{item_id}: every evidence entry must be an object")

    evidence = [normalize_record(record) for record in evidence_raw]
    evidence.sort(key=lambda row: (row["field"], row["observed_at"], row["evidence_sha256"]))
    output: dict[str, Any] = {"id": item_id, "evidence": evidence, "selected_evidence": {}}

    for field in sorted(ALLOWED_FIELDS):
        candidates = [row for row in evidence if row["field"] == field]
        if not candidates:
            continue
        newest_time = max(parse_time(row["observed_at"]) for row in candidates)
        newest = [row for row in candidates if parse_time(row["observed_at"]) == newest_time]
        values = {row["value"] for row in newest}
        if len(values) != 1:
            raise ValueError(f"{item_id}: conflicting newest evidence for {field}")
        selected = sorted(newest, key=lambda row: row["evidence_sha256"])[0]
        output[field] = selected["value"]
        output["selected_evidence"][field] = selected["evidence_sha256"]

    return output


def load_bundle(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("items"), list):
        raise ValueError("input must be an object containing an items list")
    if not all(isinstance(item, dict) for item in data["items"]):
        raise ValueError("every item must be a JSON object")
    return data


def build_report(data: dict[str, Any]) -> dict[str, Any]:
    items = [normalize_item(item) for item in data["items"]]
    ids = [item["id"] for item in items]
    if len(ids) != len(set(ids)):
        raise ValueError("item ids must be unique")
    return {
        "schema_version": 1,
        "source_bundle_sha256": canonical_hash(data),
        "summary": {"items": len(items), "evidence_records": sum(len(item["evidence"]) for item in items)},
        "items": items,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Local JSON evidence bundle")
    parser.add_argument("--output", help="Optional normalized JSON output path")
    args = parser.parse_args(argv)

    try:
        report = build_report(load_bundle(Path(args.input)))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        parser.error(str(exc))

    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
