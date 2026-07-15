#!/usr/bin/env python3
"""
310 BTC Challenge - Permutation Brute Force
Try all permutations of the 21 visible characters
"""

from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Hash import SHA256
import base64
import itertools
import sys

# Load the encrypted data
with open('/root/310_btc_challenge/alpha_row310.bin', 'rb') as f:
    data = f.read()

encrypted_data = base64.b64decode(data)
salt = encrypted_data[8:16]
ciphertext = encrypted_data[16:]

# The 21 characters from image
chars = "L3CEO275KOD899D4FA1F64"

print(f"Characters: {chars} ({len(chars)} chars)")
print(f"Encrypted: {len(encrypted_data)} bytes")
print(f"Ciphertext: {len(ciphertext)} bytes")
print(f"Salt: {salt.hex()}")
print()

# Try different segment lengths
# Full 21! permutations is impossible (5e19)
# Try smaller chunks and combinations

def try_decrypt(password: str) -> bool:
    """Try to decrypt with given password"""
    try:
        key_iv = PBKDF2(password.encode(), salt, dkLen=48, count=10000, hmac_hash_module=SHA256)
        key = key_iv[:32]
        iv = key_iv[32:]
        
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(ciphertext)
        
        # Check for valid Bitcoin key format or readable text
        try:
            text = decrypted.decode('utf-8', errors='strict')
            valid_chars = sum(1 for c in text if c.isprintable())
            if valid_chars / len(text) > 0.95:
                print(f"\n✅ FOUND! Password: {password}")
                print(f"Decrypted: {text[:200]}")
                return True
        except:
            pass
            
        # Check for Bitcoin private key format (starts with 5, K, or L)
        if decrypted[0:1] in [b'5', b'K', b'L']:
            try:
                text = decrypted.decode('ascii', errors='strict')
                if len(text) > 50 and text[:1] in '5KL':
                    print(f"\n✅ BITCOIN KEY! Password: {password}")
                    print(f"Key: {text[:100]}")
                    return True
            except:
                pass
                
    except Exception as e:
        pass
    
    return False

# Strategy: Try the full string first, then variations
print("Trying direct passwords...")
test_passwords = [
    chars,
    chars.lower(),
    chars.upper(),
    ''.join(reversed(chars)),
    'L3CEO275KOD899D4FA1F64',
    'pip',
    'Pip',
    '310',
    '310btc',
    'bitcoin',
    'challenge',
]

for pwd in test_passwords:
    if try_decrypt(pwd):
        sys.exit(0)

# Try some permutations of smaller segments
print("\nTrying permutations of 4-character segments...")
segments = ['L3CE', 'O275', 'KOD8', '99D4', 'FA1F', '64']

for perm in itertools.permutations(segments):
    pwd = ''.join(perm)
    if try_decrypt(pwd):
        sys.exit(0)

print("\nTrying permutations of 3-character segments...")
segments3 = ['L3C', 'EO2', '75K', 'OD8', '99D', '4FA', '1F6', '4']

# Too many permutations, try a sample
for i, perm in enumerate(itertools.permutations(segments3)):
    if i > 10000:  # Limit to prevent running forever
        break
    pwd = ''.join(perm)
    if i % 1000 == 0:
        print(f"Tried {i} permutations...")
    if try_decrypt(pwd):
        sys.exit(0)

print("\n❌ Password not found in tested permutations")
print("Need more hints or different approach")