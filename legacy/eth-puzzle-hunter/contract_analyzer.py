#!/usr/bin/env python3
"""
Ethereum Contract Analyzer
Analyze smart contract bytecode for puzzle characteristics
"""

import json

class ContractAnalyzer:
    """Analyze Ethereum smart contracts for puzzles"""
    
    def __init__(self):
        self.puzzle_patterns = {
            "solve_function": [
                "function solve(",
                "function answer(",
                "function submit(",
                "function unlock("
            ],
            "claim_function": [
                "function claim(",
                "function withdraw(",
                "function getReward(",
                "function prize("
            ],
            "puzzle_keywords": [
                "puzzle",
                "riddle",
                "challenge",
                "treasure",
                "clue",
                "hint",
                "password",
                "solution",
                "answer"
            ],
            "security_patterns": [
                "require(",
                "assert(",
                "keccak256",
                "sha256",
                "abi.encode"
            ]
        }
    
    def analyze_source_code(self, source_code):
        """Analyze Solidity source code for puzzle patterns"""
        findings = {
            "is_likely_puzzle": False,
            "confidence": 0,
            "solve_function": False,
            "claim_function": False,
            "has_keywords": [],
            "security_score": 0,
            "recommendation": ""
        }
        
        source_lower = source_code.lower()
        
        # Check for solve function
        for pattern in self.puzzle_patterns["solve_function"]:
            if pattern.lower() in source_lower:
                findings["solve_function"] = True
                findings["confidence"] += 30
        
        # Check for claim function
        for pattern in self.puzzle_patterns["claim_function"]:
            if pattern.lower() in source_lower:
                findings["claim_function"] = True
                findings["confidence"] += 30
        
        # Check for puzzle keywords
        keywords_found = []
        for keyword in self.puzzle_patterns["puzzle_keywords"]:
            if keyword in source_lower:
                keywords_found.append(keyword)
                findings["confidence"] += 5
        
        findings["has_keywords"] = keywords_found
        
        # Check security patterns
        security_count = 0
        for pattern in self.puzzle_patterns["security_patterns"]:
            if pattern.lower() in source_lower:
                security_count += 1
        
        findings["security_score"] = security_count
        
        # Determine if likely puzzle
        if findings["confidence"] >= 50:
            findings["is_likely_puzzle"] = True
            findings["recommendation"] = "Strong candidate - investigate further"
        elif findings["confidence"] >= 30:
            findings["recommendation"] = "Possible puzzle - check balance"
        else:
            findings["recommendation"] = "Unlikely puzzle - skip"
        
        return findings
    
    def generate_report(self, address, findings):
        """Generate human-readable report"""
        report = f"""
{'='*60}
CONTRACT ANALYSIS: {address}
{'='*60}

Likely Puzzle: {'✅ YES' if findings['is_likely_puzzle'] else '❌ No'}
Confidence: {findings['confidence']}/100

Functions Found:
  Solve Function: {'✅ Yes' if findings['solve_function'] else '❌ No'}
  Claim Function: {'✅ Yes' if findings['claim_function'] else '❌ No'}

Keywords Found: {', '.join(findings['has_keywords']) if findings['has_keywords'] else 'None'}
Security Score: {findings['security_score']}/10

Recommendation: {findings['recommendation']}

Next Steps:
  1. Check contract balance on Etherscan
  2. Read full source code
  3. Understand solve mechanism
  4. Attempt solution
  5. Claim prize if successful!
{'='*60}
"""
        return report

def demo():
    """Demo with sample contract code"""
    analyzer = ContractAnalyzer()
    
    # Sample puzzle contract code
    sample_code = """
    pragma solidity ^0.8.0;
    
    contract TreasurePuzzle {
        string private answer;
        uint256 public prize;
        bool public solved;
        
        constructor() {
            answer = "secret123";
            prize = 1 ether;
            solved = false;
        }
        
        function solve(string memory _answer) public {
            require(!solved, "Already solved");
            require(keccak256(abi.encodePacked(_answer)) == 
                    keccak256(abi.encodePacked(answer)), "Wrong answer");
            
            solved = true;
            payable(msg.sender).transfer(prize);
        }
        
        function claim() public {
            require(solved, "Not solved yet");
            // Additional claiming logic
        }
    }
    """
    
    print("="*70)
    print("🔍 DEMO: Contract Analysis")
    print("="*70)
    
    findings = analyzer.analyze_source_code(sample_code)
    report = analyzer.generate_report("0x1234...abcd", findings)
    print(report)

if __name__ == "__main__":
    demo()
