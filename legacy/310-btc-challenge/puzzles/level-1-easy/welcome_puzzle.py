#!/usr/bin/env python3
"""
Level 1: The Welcome Puzzle (0.01 BTC)
Difficulty: Easy
Time Estimate: 5-30 minutes

This puzzle introduces basic concepts.
"""

import base64
import hashlib
import getpass

print("""
╔══════════════════════════════════════════════════════════╗
║         🎯 LEVEL 1: THE WELCOME PUZZLE 🎯               ║
║              Prize: 0.01 BTC                            ║
╚══════════════════════════════════════════════════════════╝

Welcome, treasure hunter! This is your first test.

CLUE 1: The password is hidden in the README.
        Look for base64 encoded text.
        
CLUE 2: The decoded password opens the first wallet.
        
CLUE 3: The wallet address is your proof of completion.
""")

def check_solution():
    """Verify the solution"""
    
    print("\nEnter the decoded password from the README:")
    user_input = getpass.getpass("Password: ")
    
    # The actual password (base64 of "b5339mnhK/UTEXmpokerchallenge")
    # This is just a demonstration - real puzzle is harder
    expected_hash = "5f4dcc3b5aa765d61d8327deb882cf99"  # MD5 of "password"
    
    if hashlib.md5(user_input.encode()).hexdigest() == expected_hash:
        print("\n✅ CORRECT!")
        print("\n🎉 You've solved Level 1!")
        print("\n🏆 Prize: 0.01 BTC")
        print("\n📧 Submit your wallet address to claim:")
        print("   Wallet: bc1q... (example)")
        print("\n📝 Take note of this achievement code:")
        print("   ACHIEVEMENT-1-" + hashlib.sha256(user_input.encode()).hexdigest()[:16])
        return True
    else:
        print("\n❌ Incorrect. Try again!")
        print("💡 Hint: Decode the base64 in the README")
        return False

if __name__ == "__main__":
    check_solution()
