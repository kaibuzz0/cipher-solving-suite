#!/usr/bin/env python3
"""
Real-Time Opportunity Finder
Checks multiple platforms for active opportunities
"""

import webbrowser
import sys

class OpportunityFinder:
    """Find real money opportunities right now"""
    
    OPPORTUNITIES = {
        "Bug Bounties (High Pay)": [
            ("HackerOne", "https://hackerone.com/bug-bounty-programs"),
            ("Immunefi (Web3)", "https://immunefi.com/explore/"),
            ("Bugcrowd", "https://bugcrowd.com/programs"),
            ("Intigriti", "https://app.intigriti.com/programs"),
        ],
        "CTF Competitions (Cash Prizes)": [
            ("CTFtime Calendar", "https://ctftime.org/event/list/upcoming"),
            ("CTFtime Active", "https://ctftime.org/"),
        ],
        "Hackathons (Big Prizes)": [
            ("Devpost", "https://devpost.com/hackathons"),
            ("ETHGlobal", "https://ethglobal.com/events"),
            ("Gitcoin", "https://gitcoin.co/hackathons"),
            ("DoraHacks", "https://dorahacks.io/"),
        ],
        "Learning (Skill Building)": [
            ("PicoCTF", "https://picoctf.org/"),
            ("CryptoHack", "https://cryptohack.org/"),
            ("Hacker101", "https://www.hacker101.com/"),
            ("PortSwigger", "https://portswigger.net/web-security"),
        ],
        "Smart Contract Auditing": [
            ("Code4rena", "https://code4rena.com/"),
            ("Sherlock", "https://www.sherlock.xyz/"),
            ("Code4rena Contests", "https://code4rena.com/contests"),
        ],
        "Government/Enterprise": [
            ("Challenge.gov", "https://www.challenge.gov/"),
            ("Innocentive", "https://www.wazoku.com/challenges"),
        ]
    }
    
    def show_menu(self):
        """Display menu"""
        print("="*70)
        print("🎯 REAL MONEY OPPORTUNITY FINDER")
        print("="*70)
        print()
        
        idx = 1
        for category, links in self.OPPORTUNITIES.items():
            print(f"\n{category}:")
            for name, url in links:
                print(f"  [{idx}] {name}")
                idx += 1
        
        print("\n" + "="*70)
        print("Enter number to open platform, or 'all' to open everything")
        print("="*70)
    
    def open_platform(self, choice):
        """Open selected platform"""
        idx = 1
        for category, links in self.OPPORTUNITIES.items():
            for name, url in links:
                if str(idx) == choice:
                    print(f"\n🚀 Opening: {name}")
                    webbrowser.open(url)
                    return True
                idx += 1
        return False
    
    def open_all(self):
        """Open all platforms"""
        print("\n🚀 Opening all platforms...")
        for category, links in self.OPPORTUNITIES.items():
            for name, url in links:
                print(f"  • {name}")
                webbrowser.open(url)

def main():
    finder = OpportunityFinder()
    finder.show_menu()
    
    choice = input("\nEnter choice: ").strip()
    
    if choice.lower() == 'all':
        finder.open_all()
    else:
        if not finder.open_platform(choice):
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
