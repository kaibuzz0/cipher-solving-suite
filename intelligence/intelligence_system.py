#!/usr/bin/env python3
"""
Intelligence Gathering System
Real-time puzzle discovery and monitoring
"""

import json
import os
from datetime import datetime

class IntelligenceSystem:
    """Monitor multiple sources for new puzzles and challenges"""
    
    SOURCES = {
        "reddit": [
            "r/codes",
            "r/cryptography", 
            "r/puzzles",
            "r/bitcoinpuzzles",
            "r/SatoshisTreasure",
            "r/ethpuzzles"
        ],
        "ctf": [
            "ctftime.org",
            "cryptohack.org",
            "picoctf.org"
        ],
        "bug_bounty": [
            "hackerone.com",
            "bugcrowd.com",
            "intigriti.com"
        ],
        "hackathons": [
            "ethglobal.com",
            "devpost.com",
            "angelhack.com"
        ],
        "social": [
            "twitter.com",
            "discord.com"
        ]
    }
    
    def __init__(self):
        self.db_file = "intelligence/puzzle-database.json"
        self.puzzles = self._load_database()
    
    def _load_database(self):
        """Load puzzle database"""
        if os.path.exists(self.db_file):
            with open(self.db_file) as f:
                return json.load(f)
        return {
            "active": [],
            "solved": [],
            "researching": [],
            "archived": []
        }
    
    def add_puzzle(self, source, puzzle_type, prize, difficulty, url, notes=""):
        """Add new puzzle to tracking"""
        puzzle = {
            "id": f"puzzle-{datetime.now().timestamp()}",
            "source": source,
            "type": puzzle_type,
            "prize": prize,
            "difficulty": difficulty,
            "url": url,
            "notes": notes,
            "added": datetime.now().isoformat(),
            "status": "researching",
            "attempts": []
        }
        
        self.puzzles["researching"].append(puzzle)
        self._save_database()
        
        print(f"[INTEL] Added new puzzle from {source}")
        return puzzle
    
    def _save_database(self):
        """Save database"""
        os.makedirs(os.path.dirname(self.db_file), exist_ok=True)
        with open(self.db_file, "w") as f:
            json.dump(self.puzzles, f, indent=2)
    
    def get_active_puzzles(self):
        """Get all active puzzles"""
        return self.puzzles["active"]
    
    def get_research_queue(self):
        """Get puzzles being researched"""
        return self.puzzles["researching"]

def main():
    intel = IntelligenceSystem()
    
    print("="*70)
    print("🔍 INTELLIGENCE GATHERING SYSTEM")
    print("="*70)
    
    print("\n📡 Monitoring Sources:")
    for category, sources in IntelligenceSystem.SOURCES.items():
        print(f"\n  {category.upper()}:")
        for source in sources:
            print(f"    • {source}")
    
    print("\n\n🎯 Ready to track puzzles and challenges!")
    print("Use add_puzzle() to track new opportunities.")

if __name__ == "__main__":
    main()
