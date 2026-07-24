#!/usr/bin/env python3
"""
Earnings Tracker
Track progress and earnings from puzzle solving
"""

import json
import os
from datetime import datetime

class EarningsTracker:
    """Track puzzle solving earnings and statistics"""
    
    def __init__(self):
        self.data_file = "research/solutions/earnings.json"
        self.data = self._load_data()
    
    def _load_data(self):
        """Load earnings data"""
        if os.path.exists(self.data_file):
            with open(self.data_file) as f:
                return json.load(f)
        return {
            "total_earned": 0.0,
            "total_attempts": 0,
            "successful_solves": 0,
            "platforms": {},
            "history": []
        }
    
    def save_data(self):
        """Save earnings data"""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, "w") as f:
            json.dump(self.data, f, indent=2)
    
    def add_earnings(self, platform, amount, puzzle_name, notes=""):
        """Add earnings"""
        self.data["total_earned"] += amount
        self.data["successful_solves"] += 1
        
        if platform not in self.data["platforms"]:
            self.data["platforms"][platform] = {"earnings": 0, "solves": 0}
        
        self.data["platforms"][platform]["earnings"] += amount
        self.data["platforms"][platform]["solves"] += 1
        
        self.data["history"].append({
            "date": datetime.now().isoformat(),
            "platform": platform,
            "amount": amount,
            "puzzle": puzzle_name,
            "notes": notes
        })
        
        self.save_data()
        print(f"✅ Added ${amount:.2f} from {platform}")
    
    def add_attempt(self, platform, puzzle_name, notes=""):
        """Record attempt"""
        self.data["total_attempts"] += 1
        self.save_data()
    
    def get_stats(self):
        """Get statistics"""
        success_rate = 0
        if self.data["total_attempts"] > 0:
            success_rate = (self.data["successful_solves"] / self.data["total_attempts"]) * 100
        
        return {
            "total_earned": self.data["total_earned"],
            "total_attempts": self.data["total_attempts"],
            "successful_solves": self.data["successful_solves"],
            "success_rate": success_rate,
            "platforms": self.data["platforms"]
        }
    
    def display_dashboard(self):
        """Display earnings dashboard"""
        print("="*70)
        print("💰 EARNINGS DASHBOARD")
        print("="*70)
        print()
        
        stats = self.get_stats()
        
        print(f"Total Earned: ${stats['total_earned']:.2f}")
        print(f"Successful Solves: {stats['successful_solves']}")
        print(f"Total Attempts: {stats['total_attempts']}")
        print(f"Success Rate: {stats['success_rate']:.1f}%")
        print()
        
        if stats['platforms']:
            print("By Platform:")
            for platform, data in stats['platforms'].items():
                print(f"  • {platform}: ${data['earnings']:.2f} ({data['solves']} solves)")
        else:
            print("No earnings yet. Start solving!")
        
        print()
        print("="*70)
        print("Keep hunting! 🏆")

def main():
    tracker = EarningsTracker()
    tracker.display_dashboard()
    
    print("\nCommands:")
    print("  add [platform] [amount] [puzzle_name] - Add earnings")
    print("  attempt [platform] [puzzle_name] - Log attempt")
    print("  stats - Show statistics")

if __name__ == "__main__":
    main()
