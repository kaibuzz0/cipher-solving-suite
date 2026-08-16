#!/usr/bin/env python3
"""Manage the repository's timestamped News / Intelligence feed."""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FEED = ROOT / "data" / "intelligence.json"
ALLOWED_CATEGORIES = {"puzzle", "ctf", "bug-bounty", "hackathon", "crypto", "github", "research", "opportunity", "tool", "other"}
ALLOWED_CONFIDENCE = {"low", "medium", "high"}
ALLOWED_RELEVANCE = {"watch", "useful", "high", "urgent"}


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def slugify(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return value or "intel"


def load_feed(path: Path = FEED) -> dict:
    if not path.exists():
        return {"schema_version": 1, "updated_at": now_iso(), "items": []}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data.get("items"), list):
        raise ValueError("intelligence feed must contain an items list")
    return data


def validate_item(item: dict) -> list[str]:
    errors = []
    required = ["id", "title", "summary", "category", "source_name", "source_url", "published_at", "checked_at", "confidence", "relevance"]
    for field in required:
        if not item.get(field):
            errors.append(f"missing {field}")
    if item.get("category") not in ALLOWED_CATEGORIES:
        errors.append("invalid category")
    if item.get("confidence") not in ALLOWED_CONFIDENCE:
        errors.append("invalid confidence")
    if item.get("relevance") not in ALLOWED_RELEVANCE:
        errors.append("invalid relevance")
    if item.get("source_url") and not str(item["source_url"]).startswith("https://"):
        errors.append("source_url must use https")
    return errors


def validate_feed(data: dict) -> list[str]:
    errors = []
    seen = set()
    for index, item in enumerate(data.get("items", [])):
        for error in validate_item(item):
            errors.append(f"item[{index}] {error}")
        if item.get("id") in seen:
            errors.append(f"duplicate id: {item.get('id')}")
        seen.add(item.get("id"))
    return errors


def add_item(args: argparse.Namespace, path: Path = FEED) -> dict:
    data = load_feed(path)
    checked_at = now_iso()
    base_id = f"{checked_at[:10]}-{slugify(args.title)}"
    existing = {item.get("id") for item in data["items"]}
    item_id = base_id
    counter = 2
    while item_id in existing:
        item_id = f"{base_id}-{counter}"
        counter += 1
    item = {
        "id": item_id,
        "title": args.title,
        "summary": args.summary,
        "category": args.category,
        "source_name": args.source_name,
        "source_url": args.source_url,
        "published_at": args.published_at,
        "checked_at": checked_at,
        "confidence": args.confidence,
        "relevance": args.relevance,
        "agent_notes": args.notes or "",
        "related_case": args.related_case or "",
        "tags": args.tags or [],
    }
    errors = validate_item(item)
    if errors:
        raise ValueError("; ".join(errors))
    data["items"].append(item)
    data["items"].sort(key=lambda x: (x.get("published_at", ""), x.get("checked_at", "")), reverse=True)
    data["updated_at"] = checked_at
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return item


def list_items(data: dict, category: str | None = None) -> None:
    items = data.get("items", [])
    if category:
        items = [item for item in items if item.get("category") == category]
    if not items:
        print("No intelligence entries.")
        return
    for item in items:
        print(f"[{item['published_at']}] {item['category']} / {item['relevance']} / {item['confidence']}")
        print(f"  {item['title']}")
        print(f"  {item['summary']}")
        print(f"  {item['source_name']}: {item['source_url']}")


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Manage timestamped repository intelligence")
    sub = p.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    ls = sub.add_parser("list")
    ls.add_argument("--category", choices=sorted(ALLOWED_CATEGORIES))
    add = sub.add_parser("add")
    add.add_argument("--title", required=True)
    add.add_argument("--summary", required=True)
    add.add_argument("--category", required=True, choices=sorted(ALLOWED_CATEGORIES))
    add.add_argument("--source-name", required=True)
    add.add_argument("--source-url", required=True)
    add.add_argument("--published-at", required=True, help="Source publication/event timestamp, preferably ISO-8601")
    add.add_argument("--confidence", choices=sorted(ALLOWED_CONFIDENCE), default="medium")
    add.add_argument("--relevance", choices=sorted(ALLOWED_RELEVANCE), default="useful")
    add.add_argument("--notes")
    add.add_argument("--related-case")
    add.add_argument("--tags", nargs="*")
    return p


def main() -> int:
    args = parser().parse_args()
    if args.command == "add":
        item = add_item(args)
        print(f"Added intelligence item: {item['id']}")
        return 0
    data = load_feed()
    if args.command == "validate":
        errors = validate_feed(data)
        if errors:
            print("\n".join(errors))
            return 1
        print(f"Intelligence feed valid: {len(data.get('items', []))} items")
        return 0
    list_items(data, args.category)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
