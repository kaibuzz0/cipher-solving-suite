#!/usr/bin/env python3
"""Search and open the shared opportunity catalog."""

from __future__ import annotations

import argparse
import json
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "opportunities.json"


def load_catalog() -> dict:
    with CATALOG.open(encoding="utf-8") as handle:
        return json.load(handle)


def matches(item: dict, query: str | None, category: str | None) -> bool:
    if category and item.get("category") != category:
        return False
    if not query:
        return True
    needle = query.lower()
    haystack = " ".join(
        [
            str(item.get("name", "")),
            str(item.get("category", "")),
            str(item.get("description", "")),
            " ".join(item.get("tags", [])),
        ]
    ).lower()
    return needle in haystack


def format_item(item: dict) -> str:
    scope = " [VERIFY SCOPE]" if item.get("authorized_only") else ""
    tags = ", ".join(item.get("tags", []))
    return f"{item['id']:<18} {item['name']} ({item['category']}){scope}\n  {item['url']}\n  {item.get('description','')}\n  tags: {tags}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Search the Cipher Solving Suite opportunity catalog")
    parser.add_argument("--list", action="store_true", help="List matching opportunities")
    parser.add_argument("--search", metavar="TEXT", help="Search names, descriptions, categories and tags")
    parser.add_argument("--category", help="Filter by exact category")
    parser.add_argument("--open", dest="open_id", metavar="ID", help="Open one catalog item by id")
    parser.add_argument("--json", action="store_true", help="Print matching records as JSON")
    args = parser.parse_args()

    catalog = load_catalog()
    items = [item for item in catalog.get("items", []) if matches(item, args.search, args.category)]

    if args.open_id:
        selected = next((item for item in catalog.get("items", []) if item.get("id") == args.open_id), None)
        if not selected:
            parser.error(f"unknown opportunity id: {args.open_id}")
        print(f"Opening {selected['name']}: {selected['url']}")
        if selected.get("authorized_only"):
            print("Reminder: verify current program authorization and scope before testing.")
        webbrowser.open(selected["url"])
        return 0

    if args.json:
        print(json.dumps({"updated_at": catalog.get("updated_at"), "items": items}, indent=2))
        return 0

    print(f"Catalog updated: {catalog.get('updated_at', 'unknown')} | matches: {len(items)}")
    print(catalog.get("notice", ""))
    for item in items:
        print("\n" + format_item(item))
    if not items:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
