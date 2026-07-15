#!/usr/bin/env python3
"""
310 BTC Challenge - Password Brute Forcer
Try passwords derived from visible characters in image
"""

from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Hash import SHA256
import base64
import itertools
import sys

class BTC310BruteForcer:
    """Brute force passwords for the encrypted data"""
    
    def __init__(self, encrypted_b64: str):
        self.encrypted_data = base64.b64decode(encrypted_b64)
        
        # OpenSSL format: Salted__ + salt(8) + ciphertext
        if not self.encrypted_data.startswith(b'Salted__'):
            raise ValueError("Not OpenSSL format")
        
        self.salt = self.encrypted_data[8:16]
        self.ciphertext = self.encrypted_data[16:]
        
        # Known from challenge hints
        self.chars = "L3CEO275KOD899D4FA1F64"
        self.hex_words = [
            "511", "B20", "332", "328", "410", "530",
            "22B", "0FE", "52E", "D0F", "7A1", "65B",
            "52C", "7E7", "511", "2F6", "56F", "C4B"
        ]
        
    def try_decrypt(self, password: str) -> str:
        """Try to decrypt with given password"""
        try:
            # Try PBKDF2 first (like GSMG Phase 4)
            key_iv = PBKDF2(password.encode(), self.salt, dkLen=48, count=10000, hmac_hash_module=SHA256)
            key = key_iv[:32]
            iv = key_iv[32:]
            
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted = cipher.decrypt(self.ciphertext)
            
            # Check for valid plaintext
            try:
                text = decrypted.decode('utf-8', errors='strict')
                # Look for Bitcoin private key patterns or readable text
                if 'private' in text.lower() or 'key' in text.lower() or text.startswith('5') or text.startswith('K') or text.startswith('L'):
                    return text
                if len([c for c in text if 32 <= ord(c) < 127]) / len(text) > 0.9:
                    return text
            except:
                pass
            
            # Try PBKDF1
            from Crypto.Protocol.KDF import PBKDF1
            key_iv = PBKDF1(password.encode(), self.salt, 48, 1000, SHA256)
            key = key_iv[:32]
            iv = key_iv[32:]
            
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted = cipher.decrypt(ciphertext)
            
            try:
                text = decrypted.decode('utf-8', errors='strict')
                if 'private' in text.lower() or 'key' in text.lower() or text.startswith('5') or text.startswith('K') or text.startswith('L'):
                    return text
            except:
                pass
                
        except Exception as e:
            pass
        
        return None
    
    def generate_passwords(self):
        """Generate password candidates from hints"""
        passwords = []
        
        # Direct use of visible characters
        passwords.append(self.chars)
        passwords.append(self.chars.lower())
        passwords.append(self.chars.upper())
        
        # Hex grid concatenations
        hex_concat = ''.join(self.hex_words)
        passwords.append(hex_concat)
        passwords.append(hex_concat.lower())
        
        # Combinations
        passwords.append(self.chars + hex_concat)
        passwords.append(hex_concat + self.chars)
        
        # With common separators
        for sep in ['', '_', '-', ' ']:
            passwords.append(sep.join(self.hex_words))
        
        # Permutations of short segments (if reasonable)
        # Try some common words
        passwords.extend([
            "pip", "Pip", "PIP",
            "bitcoin", "Bitcoin", "BITCOIN",
            "310", "310btc", "310BTC",
            "challenge", "Challenge",
            "theseedisplanted",
            "L3CEO275KOD899D4FA1F64",
            "L3CEO275KOD899D4FA1F64310"
        ])
        
        return list(set(passwords))  # Deduplicate
    
    def brute_force(self, max_attempts: int = 10000):
        """Try all generated passwords"""
        passwords = self.generate_passwords()
        print(f"Generated {len(passwords)} password candidates")
        
        for i, pwd in enumerate(passwords[:max_attempts]):
            if i % 100 == 0:
                print(f"Tried {i} passwords...")
            
            result = self.try_decrypt(pwd)
            if result:
                print(f"\n✅ FOUND! Password: {pwd}")
                print(f"Decrypted: {result[:200]}")
                return pwd, result
        
        print("\n❌ Password not found in candidate list")
        return None, None

def main():
    # Load the encrypted data from alpha channel extraction
    with open('/root/310_btc_challenge/alpha_row310.bin', 'rb') as f:
        data = f.read()
    
    # The file is base64 encoded, decode it
    encrypted_data = base64.b64decode(data)
    
    print("310 BTC Challenge - Password Brute Force")
    print("=" * 50)
    print(f"Encrypted data: {len(encrypted_data)} bytes")
    print(f"Salt: {encrypted_data[8:16].hex()}")
    
    # Convert back to base64 for the tool (it expects b64 string)
    encrypted_b64 = base64.b64encode(encrypted_data).decode()
    
    forcer = BTC310BruteForcer(encrypted_b64)
    password, decrypted = forcer.brute_force()
    
    if password:
        with open('decrypted_key.txt', 'w') as f:
            f.write(f"Password: {password}\n")
            f.write(f"Decrypted: {decrypted}\n")
        print("\nSaved to decrypted_key.txt")

if __name__ == "__main__":
    main()