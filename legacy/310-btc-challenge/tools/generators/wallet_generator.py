#!/usr/bin/env python3
"""
Bitcoin Wallet Generator (Testnet)
For educational purposes in the 310 BTC Challenge
"""

import hashlib
import os
import base64

def generate_test_wallet():
    """Generate a test Bitcoin wallet"""
    
    # Generate private key (32 random bytes)
    private_key = os.urandom(32)
    private_key_hex = private_key.hex()
    
    # Generate public key (simplified)
    # In real implementation, use elliptic curve multiplication
    public_key = hashlib.sha256(private_key).digest()
    
    # Generate address (simplified)
    # Real Bitcoin uses RIPEMD160(SHA256(public_key))
    address = "1" + hashlib.sha256(public_key).hexdigest()[:33]
    
    return {
        "private_key": private_key_hex,
        "public_key": public_key.hex(),
        "address": address,
        "wif": base64.b64encode(private_key).decode()[:51]  # Simplified WIF
    }

print("""
╔══════════════════════════════════════════════════════════╗
║        ₿ TESTNET WALLET GENERATOR ₿                     ║
║     Educational tool for the 310 BTC Challenge           ║
╚══════════════════════════════════════════════════════════╝

⚠️  This generates TEST wallets for educational purposes.
⚠️  Do NOT use for real Bitcoin transactions.
⚠️  Real wallets require proper entropy and key derivation.
""")

def main():
    print("\nGenerate test wallet? (y/n)")
    if input().lower() != 'y':
        return
    
    wallet = generate_test_wallet()
    
    print("\n" + "="*50)
    print("🔐 TEST WALLET GENERATED")
    print("="*50)
    print(f"\nAddress: {wallet['address']}")
    print(f"\nPrivate Key: {wallet['private_key']}")
    print(f"\nWIF: {wallet['wif']}")
    print("\n" + "="*50)
    print("⚠️  REMEMBER: This is a TEST wallet only!")
    print("="*50)

if __name__ == "__main__":
    main()
