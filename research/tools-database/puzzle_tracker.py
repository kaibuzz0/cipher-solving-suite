#!/usr/bin/env python3
"""
Puzzle Tracking Database
Comprehensive tracking of all active and solved puzzles
"""

import json
import os
from datetime import datetime
from pathlib import Path

class PuzzleDatabase:
    """Central database for all puzzle solving operations"""
    
    def __init__(self, db_path="research/active-puzzles/puzzle-db.json"):
        self.db_path = db_path
        self.db = self._load_db()
    
    def _load_db(self):
        """Load database"""
        if os.path.exists(self.db_path):
            with open(self.db_path) as f:
                return json.load(f)
        return {
            "active": [],
            "solved": [],
            "archived": [],
            "stats": {
                "total_attempts": 0,
                "successful_solves": 0,
                "total_earnings": 0.0
            }
        }
    
    def save_db(self):
        """Save database"""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        with open(self.db_path, "w") as f:
            json.dump(self.db, f, indent=2)
    
    def add_puzzle(self, name, puzzle_type, source, difficulty, prize, url, notes=""):
        """Add new puzzle to track"""
        puzzle = {
            "id": f"puzzle-{int(datetime.now().timestamp())}",
            "name": name,
            "type": puzzle_type,
            "source": source,
            "difficulty": difficulty,
            "prize": prize,
            "url": url,
            "notes": notes,
            "status": "active",
            "added": datetime.now().isoformat(),
            "attempts": [],
            "solved_date": None
        }
        
        self.db["active"].append(puzzle)
        self.save_db()
        
        print(f"[DB] Added puzzle: {name}")
        return puzzle
    
    def mark_solved(self, puzzle_id, solution, earnings=0):
        """Mark puzzle as solved"""
        for puzzle in self.db["active"]:
            if puzzle["id"] == puzzle_id:
                puzzle["status"] = "solved"
                puzzle["solved_date"] = datetime.now().isoformat()
                puzzle["solution"] = solution
                puzzle["earnings"] = earnings
                
                self.db["solved"].append(puzzle)
                self.db["active"] = [p for p in self.db["active"] if p["id"] != puzzle_id]
                
                self.db["stats"]["successful_solves"] += 1
                self.db["stats"]["total_earnings"] += earnings
                
                self.save_db()
                print(f"[DB] Marked as solved: {puzzle['name']}")
                return True
        
        return False
    
    def get_stats(self):
        """Get solving statistics"""
        return {
            "active_puzzles": len(self.db["active"]),
            "solved_puzzles": len(self.db["solved"]),
            "total_earnings": self.db["stats"]["total_earnings"],
            "solve_rate": self.db["stats"]["successful_solves"] / max(self.db["stats"]["total_attempts"], 1)
        }
    
    def list_active(self):
        """List all active puzzles"""
        return self.db["active"]

def main():
    db = PuzzleDatabase()
    
    print("="*70)
    print("🗄️ PUZZLE TRACKING DATABASE")
    print("="*70)
    
    # Demo
    db.add_puzzle(
        name="Caesar Challenge #1",
        puzzle_type="classical_cipher",
        source="cryptopals.com",
        difficulty="easy",
        prize="0",
        url="https://cryptopals.com/sets/1/challenges/1",
        notes="Base64 encoding challenge"
    )
    
    stats = db.get_stats()
    print(f"\n📊 Database Stats:")
    print(f"  Active puzzles: {stats['active_puzzles']}")
    print(f"  Solved puzzles: {stats['solved_puzzles']}")
    print(f"  Total earnings: ${stats['total_earnings']:.2f}")
    
    print("\n✅ Puzzle Database Operational")

if __name__ == "__main__":
    main()
