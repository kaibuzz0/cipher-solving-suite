#!/usr/bin/env python3
"""
Ethereum Puzzle Scanner
Scan blockchain for puzzle contracts with ETH prizes
"""

import re
import json
from datetime import datetime

class EthPuzzleScanner:
    """Scan Ethereum for puzzle contracts"""
    
    def __init__(self):
        self.potential_puzzles = []
        
    def analyze_contract_code(self, address, code, balance):
        """Analyze contract code for puzzle patterns"""
        
        # Puzzle indicators
        puzzle_keywords = [
            r'function\s+solve',
            r'function\s+answer',
            r'function\s+claim',
            r'function\s+unlock',
            r'function\s+check',
            r'puzzle',
            r'challenge',
            r'treasure',
            r'riddle',
            r'game',
            r'prize',
            r'reward'
        ]
        
        # Scam indicators (red flags)
        scam_patterns = [
            r'transfer.*msg\.sender',
            r'require.*msg\.value',
            r'owner.*transfer',
            r'selfdestruct'
        ]
        
        score = 0
        is_puzzle = False
        is_suspicious = False
        
        # Check for puzzle patterns
        for keyword in puzzle_keywords:
            if re.search(keyword, code, re.IGNORECASE):
                score += 10
                is_puzzle = True
        
        # Check for scam patterns
        for pattern in scam_patterns:
            if re.search(pattern, code, re.IGNORECASE):
                score -= 20
                is_suspicious = True
        
        # Must have balance to be interesting
        if balance <= 0:
            score = 0
        
        return {
            "address": address,
            "balance": balance,
            "is_potential_puzzle": is_puzzle and score > 20,
            "is_suspicious": is_suspicious,
            "score": score,
            "indicators_found": score // 10
        }
    
    def manual_check_guide(self):
        """Guide for manually checking contracts"""
        return """
🔍 ETHEREUM PUZZLE SCANNING - MANUAL MODE

Step 1: Go to Etherscan
  https://etherscan.io/contractsVerified

Step 2: Look for contracts with:
  - Balance > 0 ETH
  - Recent activity
  - Verified source code

Step 3: Check for puzzle functions:
  - function solve(
  - function answer(
  - function claim(
  - function unlock(

Step 4: Analyze the code:
  - What does the puzzle want?
  - Is it solvable?
  - Is it legitimate?

Step 5: If legitimate:
  - Document in research/active-puzzles/
  - Attempt to solve
  - Claim prize if successful

⚠️  RED FLAGS - SKIP THESE:
  - Requires sending ETH to play
  - No verified source code
  - "Guaranteed" returns
  - Owner can drain contract
  - Recently created + high balance

✅ GREEN FLAGS - GOOD SIGNS:
  - Clear puzzle logic
  - Around for months
  - Community discussion
  - Reasonable prize
  - Verifiable rules

Stay safe! 🛡️
"""
    
    def run_interactive(self):
        """Interactive mode"""
        print("="*70)
        print("🔷 ETHEREUM PUZZLE SCANNER")
        print("="*70)
        print()
        print(self.manual_check_guide())
        
        print("\n🎯 Ready to scan!")
        print("Go to: https://etherscan.io/contractsVerified")
        print("Find contracts with ETH balance and puzzle functions.")
        print("Document findings in research/active-puzzles/")

def main():
    scanner = EthPuzzleScanner()
    scanner.run_interactive()

if __name__ == "__main__":
    main()
