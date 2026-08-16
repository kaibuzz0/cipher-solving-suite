import argparse
import json
import tempfile
import unittest
from pathlib import Path

import scripts.intelligence_feed as intelligence_feed
import scripts.new_case as new_case
from tools.earnings_tracker import EarningsTracker
from tools.opportunity_finder import load_catalog, matches
from tools.scanning.opportunity_scanner import build_snapshot

ROOT = Path(__file__).resolve().parents[1]


class CatalogTests(unittest.TestCase):
    def test_catalog_has_unique_ids_and_urls(self):
        catalog = load_catalog()
        items = catalog["items"]
        self.assertGreater(len(items), 0)
        ids = [item["id"] for item in items]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(all(item["url"].startswith("https://") for item in items))

    def test_search_matches_tags_and_category(self):
        item = {"name": "Example", "category": "ctf", "description": "Puzzle", "tags": ["crypto"]}
        self.assertTrue(matches(item, "crypto", None))
        self.assertTrue(matches(item, None, "ctf"))
        self.assertFalse(matches(item, None, "hackathon"))

    def test_snapshot_is_explicitly_not_live(self):
        snapshot = build_snapshot()
        self.assertFalse(snapshot["live_scan"])
        self.assertEqual(snapshot["source"], "data/opportunities.json")

    def test_tool_registry_has_unique_ids_and_required_fields(self):
        registry = json.loads((ROOT / "data" / "tools.json").read_text(encoding="utf-8"))
        items = registry["items"]
        self.assertGreater(len(items), 0)
        ids = [item["id"] for item in items]
        self.assertEqual(len(ids), len(set(ids)))
        for item in items:
            for field in ("name", "category", "path", "command", "description", "maturity"):
                self.assertTrue(item.get(field), f"{item.get('id')} missing {field}")
            self.assertTrue((ROOT / item["path"]).exists(), f"registered path missing: {item['path']}")


class IntelligenceTests(unittest.TestCase):
    def test_repository_feed_is_valid(self):
        data = intelligence_feed.load_feed()
        self.assertEqual(intelligence_feed.validate_feed(data), [])

    def test_duplicate_ids_are_rejected(self):
        item = {
            "id": "same",
            "title": "One",
            "summary": "Summary",
            "category": "research",
            "source_name": "Source",
            "source_url": "https://example.com/a",
            "published_at": "2026-08-16T12:00:00Z",
            "checked_at": "2026-08-16T12:01:00Z",
            "confidence": "high",
            "relevance": "useful",
        }
        errors = intelligence_feed.validate_feed({"items": [item, dict(item)]})
        self.assertTrue(any("duplicate id" in error for error in errors))

    def test_source_url_must_be_https(self):
        item = {
            "id": "bad-source",
            "title": "Bad",
            "summary": "Summary",
            "category": "research",
            "source_name": "Source",
            "source_url": "http://example.com/a",
            "published_at": "2026-08-16T12:00:00Z",
            "checked_at": "2026-08-16T12:01:00Z",
            "confidence": "medium",
            "relevance": "watch",
        }
        self.assertIn("source_url must use https", intelligence_feed.validate_item(item))

    def test_add_item_persists_sourced_entry(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "intelligence.json"
            args = argparse.Namespace(
                title="Example event",
                summary="A sourced update.",
                category="hackathon",
                source_name="Official organizer",
                source_url="https://example.com/event",
                published_at="2026-08-16T12:00:00Z",
                confidence="high",
                relevance="high",
                notes="Useful for agents",
                related_case=None,
                tags=["coding", "prize"],
            )
            item = intelligence_feed.add_item(args, path)
            saved = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(saved["items"][0]["id"], item["id"])
            self.assertEqual(saved["items"][0]["source_name"], "Official organizer")
            self.assertEqual(intelligence_feed.validate_feed(saved), [])


class EarningsTests(unittest.TestCase):
    def test_attempt_and_earning_persist(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "earnings.json"
            tracker = EarningsTracker(path)
            tracker.add_attempt("ctf", "case-1", "started")
            tracker.add_earnings("ctf", 25.0, "case-1", "verified payout")
            reloaded = EarningsTracker(path)
            stats = reloaded.get_stats()
            self.assertEqual(stats["total_attempts"], 1)
            self.assertEqual(stats["successful_solves"], 1)
            self.assertEqual(stats["total_earned"], 25.0)
            self.assertEqual(stats["platforms"]["ctf"]["attempts"], 1)
            self.assertEqual(len(reloaded.data["history"]), 2)

    def test_negative_earning_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            tracker = EarningsTracker(Path(tmp) / "earnings.json")
            with self.assertRaises(ValueError):
                tracker.add_earnings("x", -1, "bad")


class CaseWorkflowTests(unittest.TestCase):
    def test_slugify(self):
        self.assertEqual(new_case.slugify("Puzzle 310: Alpha/Beta"), "puzzle-310-alpha-beta")

    def test_create_case_builds_expected_files_and_security_flag(self):
        original_root = new_case.CASES_ROOT
        try:
            with tempfile.TemporaryDirectory() as tmp:
                new_case.CASES_ROOT = Path(tmp)
                case_dir = new_case.create_case(
                    "Authorized Test",
                    "bug-bounty",
                    "Example Program",
                    "https://example.com/program",
                    "https://example.com/policy",
                )
                self.assertTrue((case_dir / "README.md").exists())
                self.assertTrue((case_dir / "notes.md").exists())
                self.assertTrue((case_dir / "attempts.md").exists())
                self.assertTrue((case_dir / "evidence" / ".gitkeep").exists())
                metadata = json.loads((case_dir / "case.json").read_text(encoding="utf-8"))
                self.assertTrue(metadata["authorization_required"])
                self.assertEqual(metadata["authorization_url"], "https://example.com/policy")
                self.assertEqual(metadata["status"], "new")
        finally:
            new_case.CASES_ROOT = original_root


if __name__ == "__main__":
    unittest.main()
