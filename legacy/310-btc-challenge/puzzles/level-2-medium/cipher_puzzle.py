#!/usr/bin/env python3
"""
Level 2: The Cipher (0.1 BTC)
Difficulty: Medium
Requires: Understanding of classical ciphers
"""

import hashlib
import getpass

CIPHER_TEXT = """
Gur punsafe vf uvqqra va gur pbqr,
Gur xrl vf gur ynfg guerr jbeqf bs guvf fragrapr.
Ebg13 vf lbhe sevraq.
"""

def rot13(s):
    """Apply ROT13 cipher"""
    result = []
    for c in s:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result.append(chr((ord(c) - base + 13) % 26 + base))
        else:
            result.append(c)
    return ''.join(result)

print("""
╔══════════════════════════════════════════════════════════╗
║           🔐 LEVEL 2: THE CIPHER 🔐                     ║
║              Prize: 0.1 BTC                               ║
╚══════════════════════════════════════════════════════════╝

The message has been encoded using a classical cipher.

CIPHER TEXT:
""")

print(CIPHER_TEXT)

print("""
\nINSTRUCTIONS:
1. Decode the cipher text
2. Find the hidden key in the message
3. Use the key to unlock the wallet
""")

def check_solution():
    print("\nDecoded message:")
    decoded = rot13(CIPHER_TEXT)
    print(decoded)
    
    print("\nEnter the key (last three words of the decoded sentence):")
    user_input = input("Key: ").strip().lower()
    
    # Expected: "this sentence"
    if "sentence" in user_input:
        print("\n✅ CORRECT!")
        print("\n🎉 You've solved Level 2!")
        print("\n🏆 Prize: 0.1 BTC")
        print("\n⚠️ Next level requires prime number knowledge")
        return True
    else:
        print("\n❌ Not quite. Decode the message and look for the key.")
        return False

if __name__ == "__main__":
    check_solution()
