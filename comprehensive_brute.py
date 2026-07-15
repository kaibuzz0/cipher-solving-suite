#!/usr/bin/env python3
"""
310 BTC Challenge - Comprehensive Brute Force
Try all known hints systematically
"""

from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF1, PBKDF2
from Cryptodome.Hash import SHA256, SHA1, MD5
from Cryptodome.Util.Padding import unpad
import base64
import itertools

class ComprehensiveBrute:
    def __init__(self):
        with open('/root/310_btc_challenge/alpha_row310.bin', 'rb') as f:
            data = f.read()
        self.encrypted_data = base64.b64decode(data)
        self.salt = self.encrypted_data[8:16]
        self.ciphertext = self.encrypted_data[16:]
        
        # Known hints
        self.chars = "L3CEO275KOD899D4FA1F64"
        self.hex_words = ["511", "B20", "332", "328", "410", "530",
                         "22B", "0FE", "52E", "D0F", "7A1", "65B",
                         "52C", "7E7", "511", "2F6", "56F", "C4B"]
        
        print(f"Encrypted: {len(self.encrypted_data)} bytes")
        print(f"Salt: {self.salt.hex()}")
    
    def try_decrypt(self, password, kdf='PBKDF2', count=10000, hash_module=SHA256):
        """Try to decrypt and return plaintext if valid"""
        try:
            if kdf == 'PBKDF2':
                key_iv = PBKDF2(password.encode(), self.salt, dkLen=48, 
                               count=count, hmac_hash_module=hash_module)
            else:  # PBKDF1
                key_iv = PBKDF1(password.encode(), self.salt, 48, count, hash_module)
            
            key = key_iv[:32]
            iv = key_iv[32:]
            
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted = cipher.decrypt(self.ciphertext)
            
            # Try to unpad
            try:
                unpadded = unpad(decrypted, AES.block_size)
                return unpadded
            except:
                # Invalid padding
                return None
        except:
            return None
    
    def check_for_key(self, data):
        """Check if data contains a Bitcoin key"""
        if not data:
            return False
        
        try:
            text = data.decode('latin-1')
        except:
            return False
        
        # Look for Bitcoin patterns
        base58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
        
        # Pattern 1: Starts with 5, K, or L followed by base58 chars
        for start in ['5', 'K', 'L']:
            if text.startswith(start):
                rest = ''.join(c for c in text[1:] if c in base58)
                if len(rest) >= 50:
                    return True, start + rest[:51]
        
        # Pattern 2: Contains printable string of base58 chars
        key_chars = []
        for c in text:
            if c in base58:
                key_chars.append(c)
            else:
                if len(key_chars) >= 51:
                    candidate = ''.join(key_chars)
                    if candidate[0] in '5KL':
                        return True, candidate[:52]
                key_chars = []
        
        return False, None
    
    def brute_force(self):
        """Try all combinations"""
        passwords = [
            # Direct from hints
            'pip', 'Pip', 'PIP',
            '310', '310btc', '310BTC',
            'KOD8', 'kod8', 'Kod8',
            self.chars,
            self.chars.lower(),
            ''.join(reversed(self.chars)),
            'L3CE', 'O275', 'KOD8', '99D4', 'FA1F', '64',
            # Combinations
            'pip310', '310pip', 'bitcoin', 'Bitcoin',
            'thekey', 'private', 'key',
            # Empty
            '',
        ]
        
        kdfs = [
            ('PBKDF2', 1000, SHA256),
            ('PBKDF2', 10000, SHA256),
            ('PBKDF1', 1000, SHA256),
        ]
        
        print(f"\nTrying {len(passwords)} passwords x {len(kdfs)} KDF variations...")
        
        for pwd in passwords:
            for kdf_name, count, hash_mod in kdfs:
                data = self.try_decrypt(pwd, kdf_name, count, hash_mod)
                if data:
                    found, key = self.check_for_key(data)
                    if found:
                        print(f"\n✅ FOUND!")
                        print(f"Password: {pwd}")
                        print(f"KDF: {kdf_name} count={count}")
                        print(f"Key: {key}")
                        return pwd, key
        
        print("\n❌ No valid key found")
        return None, None

if __name__ == "__main__":
    brute = ComprehensiveBrute()
    pwd, key = brute.brute_force()
    
    if pwd and key:
        with open('/root/310_btc_challenge/solution_v2.txt', 'w') as f:
            f.write(f"Password: {pwd}\n")
            f.write(f"KDF: PBKDF2 count=1000 or 10000\n")
            f.write(f"Private Key (WIF): {key}\n")
        print("\nSaved to solution_v2.txt")