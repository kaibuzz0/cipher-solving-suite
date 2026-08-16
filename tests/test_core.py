import argparse
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

import scripts.intelligence_feed as intelligence_feed
import scripts.new_case as new_case
import scripts.source_registry as source_registry
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


class SourceRegistryTests(unittest.TestCase):
    def test_repository_source_registry_is_valid(self):
        data = source_registry.load_registry()
        self.assertEqual(source_registry.validate_registry(data), [])
        self.assertGreaterEqual(len(data["sources"]), 5)

    def test_duplicate_source_ids_are_rejected(self):
        source = {
            "id": "same",
            "name": "Example",
            "source_type": "official",
            "url": "https://example.com",
            "categories": ["research"],
            "tier": "primary",
            "freshness_hours": 24,
            "last_checked_at": None,
            "assigned_agent": "research-scout",
            "enabled": True,
            "publish_default_confidence": "high",
        }
        errors = source_registry.validate_registry({"sources": [source, dict(source)]})
        self.assertTrue(any("duplicate source id" in error for error in errors))

    def test_never_checked_source_is_due(self):
        source = {"enabled": True, "last_checked_at": None, "freshness_hours": 24}
        self.assertEqual(source_registry.source_due_state(source), "never-checked")

    def test_recent_source_is_fresh(self):
        source = {"enabled": True, "last_checked_at": "2026-08-16T12:00:00Z", "freshness_hours": 24}
        now = datetime(2026, 8, 16, 13, 0, tzinfo=timezone.utc)
        self.assertEqual(source_registry.source_due_state(source, now), "fresh")


class IntelligenceTests(unittest.TestCase):
    def make_item(self, item_id="one", title="One", source_url="https://example.com/a"):
        return {
            "id": item_id,
            "fingerprint": intelligence_feed.fingerprint(title, source_url),
            "title": title,
            "summary": "Summary",
            "category": "research",
            "source_id": "",
            "source_name": "Source",
            "source_url": source_url,
            "published_at": "2026-08-16T12:00:00Z",
            "checked_at": "2026-08-16T12:01:00Z",
            "confidence": "high",
            "relevance": "useful",
        }

    def test_repository_feed_is_valid(self):
        data = intelligence_feed.load_feed()
        self.assertEqual(intelligence_feed.validate_feed(data), [])

    def test_duplicate_ids_are_rejected(self):
        item = self.make_item("same")
        duplicate = dict(item)
        duplicate["fingerprint"] = intelligence_feed.fingerprint("Different", "https://example.com/b")
        duplicate["title"] = "Different"
        duplicate["source_url"] = "https://example.com/b"
        errors = intelligence_feed.validate_feed({"items": [item, duplicate]})
        self.assertTrue(any("duplicate id" in error for error in errors))

    def test_duplicate_fingerprints_are_rejected(self):
        item = self.make_item("one")
        duplicate = dict(item)
        duplicate["id"] = "two"
        errors = intelligence_feed.validate_feed({"items": [item, duplicate]})
        self.assertTrue(any("duplicate fingerprint" in error for error in errors))

    def test_source_url_must_be_https(self):
        item = self.make_item("bad-source", "Bad", "http://example.com/a")
        self.assertIn("source_url must use https", intelligence_feed.validate_item(item))

    def test_fingerprint_is_deterministic_and_ignores_query(self):
        a = intelligence_feed.fingerprint(" Example  Event ", "https://EXAMPLE.com/path/?utm_source=x")
        b = intelligence_feed.fingerprint("example event", "https://example.com/path")
        self.assertEqual(a, b)

    def test_add_item_persists_sourced_entry(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "intelligence.json"
            args = argparse.Namespace(
                title="Example event",
                summary="A sourced update.",
                category="hackathon",
                source_id=None,
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
            self.assertEqual(saved["items"][0]["fingerprint"], item["fingerprint"])
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
