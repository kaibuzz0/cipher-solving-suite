#!/usr/bin/env python3
"""
Research Templates
Standardized formats for puzzle documentation
"""

class ResearchTemplates:
    """Templates for consistent puzzle research"""
    
    @staticmethod
    def puzzle_analysis_template():
        """Template for analyzing a puzzle"""
        return """
# Puzzle Analysis: [PUZZLE_NAME]

## Basic Information
- **Name:** 
- **Source:** 
- **Type:** [cryptography/steganography/mathematical/etc]
- **Difficulty:** [easy/medium/hard/expert]
- **Prize:** 
- **Status:** [active/solved/unsolved]

## Initial Assessment
- [ ] Verified legitimate
- [ ] Prize confirmed
- [ ] Difficulty estimated
- [ ] Time commitment assessed

## Technical Details
- **Platform:** [Ethereum/Bitcoin/Web/etc]
- **Contract/URL:** 
- **Tools Needed:** 

## Analysis Notes
[Write your analysis here]

## Solution Attempts
### Attempt 1: [DATE]
- Method:
- Result:
- Notes:

## Resources
- Links:
- References:
- Tools used:

## Conclusion
- Solved: [Yes/No]
- Solution: [if solved]
- Time spent:
- Lessons learned:
"""
    
    @staticmethod
    def ctf_writeup_template():
        """Template for CTF writeups"""
        return """
# CTF Writeup: [CTF_NAME] - [CHALLENGE_NAME]

## Challenge Info
- **CTF:** 
- **Challenge:** 
- **Category:** [crypto/web/forensics/etc]
- **Points:** 
- **Solves:** 

## Description
[Challenge description]

## Initial Analysis
[Your first thoughts]

## Solution Process
### Step 1: [What you did]
### Step 2: [What you did]
### Step 3: [What you did]

## Flag
```
[flag{...}]
```

## Lessons Learned
- 
- 
- 

## Tools Used
- 

## References
- 
"""
    
    @staticmethod
    def bug_bounty_template():
        """Template for bug bounty reports"""
        return """
# Bug Bounty Report: [PROGRAM_NAME]

## Summary
- **Program:** 
- **Severity:** [Critical/High/Medium/Low]
- **Status:** [Reported/Fixed/Paid]
- **Bounty:** $

## Vulnerability Details
**Type:** [XSS/SQLi/etc]
**URL/Endpoint:** 
**Parameter:** 

## Steps to Reproduce
1. 
2. 
3. 

## Impact
[What could attacker do?]

## Proof of Concept
```
[code or screenshots]
```

## Remediation
[How to fix]

## Timeline
- Discovered: [date]
- Reported: [date]
- Triaged: [date]
- Fixed: [date]
- Paid: [date]

## Notes
- 
"""

def generate_templates():
    """Generate all templates"""
    templates = ResearchTemplates()
    
    print("="*70)
    print("📝 RESEARCH TEMPLATES")
    print("="*70)
    
    print("\n1. Puzzle Analysis Template:")
    print(templates.puzzle_analysis_template())
    
    print("\n2. CTF Writeup Template:")
    print(templates.ctf_writeup_template())
    
    print("\n3. Bug Bounty Template:")
    print(templates.bug_bounty_template())

if __name__ == "__main__":
    generate_templates()
