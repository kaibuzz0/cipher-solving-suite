#!/usr/bin/env python3
"""
310 BTC Challenge - Smart Password Brute Force
Try combinations of visible characters and hex grid
"""

from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Hash import SHA256
import base64
import itertools
import hashlib

class SmartBruteForcer:
    """Smart brute force using known hints"""
    
    def __init__(self):
        # Load encrypted data
        with open('/root/310_btc_challenge/alpha_row310.bin', 'rb') as f:
            data = f.read()
        self.encrypted_data = base64.b64decode(data)
        self.salt = self.encrypted_data[8:16]
        self.ciphertext = self.encrypted_data[16:]
        
        print(f"Encrypted: {len(self.encrypted_data)} bytes")
        print(f"Salt: {self.salt.hex()}")
        
        # Known data
        self.chars = "L3CEO275KOD899D4FA1F64"  # 22 chars
        self.hex_grid = [
            "511", "B20", "332", "328", "410", "530",
            "22B", "0FE", "52E", "D0F", "7A1", "65B",
            "52C", "7E7", "511", "2F6", "56F", "C4B"
        ]
    
    def try_decrypt(self, password: str) -> tuple:
        """Try decryption, return (success, plaintext)"""
        try:
            key_iv = PBKDF2(password.encode(), self.salt, dkLen=48, count=10000, hmac_hash_module=SHA256)
            key = key_iv[:32]
            iv = key_iv[32:]
            
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted = cipher.decrypt(self.ciphertext)
            
            # Check for Bitcoin private key patterns
            text = decrypted.decode('latin-1')
            
            # Bitcoin WIF keys start with 5, K, or L and are 51-52 chars
            printable = ''.join(c for c in text if c.isprintable())
            
            # Check patterns
            if printable.startswith('5') and len(printable) > 50:
                return True, f"BITCOIN WIF: {printable[:60]}"
            
            if printable.startswith('K') or printable.startswith('L'):
                if len(printable) > 50:
                    return True, f"BITCOIN WIF: {printable[:60]}"
            
            # Check for hex private key (64 hex chars)
            hex_chars = set('0123456789abcdefABCDEF')
            if all(c in hex_chars for c in printable[:64]) and len(printable) >= 64:
                return True, f"HEX KEY: {printable[:64]}"
            
            # High printable ratio = likely plaintext
            if len(printable) > 10:
                ratio = sum(1 for c in text if c.isprintable()) / len(text)
                if ratio > 0.9:
                    return True, f"PLAINTEXT: {printable[:100]}"
            
        except:
            pass
        
        return False, None
    
    def try_variations(self):
        """Try variations of the character string"""
        variations = [
            self.chars,
            self.chars.lower(),
            self.chars.upper(),
            ''.join(reversed(self.chars)),
            self.chars.replace('8', '').replace('9', ''),  # Remove duplicates
            'L3CE', 'O275', 'KOD8', '99D4', 'FA1F', '64',  # Segments
        ]
        
        print("\nTrying character variations...")
        for pwd in variations:
            success, result = self.try_decrypt(pwd)
            if success:
                return pwd, result
            print(f"  {pwd}: no")
        
        return None, None
    
    def try_hex_combinations(self):
        """Try combinations of hex grid"""
        # Join all hex values
        hex_concat = ''.join(self.hex_grid)
        
        combos = [
            hex_concat,
            hex_concat.lower(),
            ''.join(reversed(self.hex_grid)),
        ]
        
        print("\nTrying hex combinations...")
        for pwd in combos:
            success, result = self.try_decrypt(pwd)
            if success:
                return pwd, result
            print(f"  {pwd[:50]}...: no")
        
        return None, None
    
    def try_mixed(self):
        """Try combinations of chars + hex"""
        hex_concat = ''.join(self.hex_grid)
        
        mixed = [
            self.chars + hex_concat,
            hex_concat + self.chars,
            self.chars.lower() + hex_concat.lower(),
            'pip' + self.chars,
            'Pip' + self.chars,
            '310' + self.chars,
            self.chars + '310',
            'bitcoin' + self.chars,
            self.chars + 'bitcoin',
        ]
        
        print("\nTrying mixed combinations...")
        for pwd in mixed:
            success, result = self.try_decrypt(pwd)
            if success:
                return pwd, result
            print(f"  {pwd[:50]}...: no")
        
        return None, None
    
    def try_permutations_short(self):
        """Try permutations of smaller segments"""
        segments = ['L3CE', 'O275', 'KOD8', '99D4', 'FA1F', '64']
        
        print("\nTrying 4-char segment permutations...")
        count = 0
        for perm in itertools.permutations(segments):
            pwd = ''.join(perm)
            success, result = self.try_decrypt(pwd)
            if success:
                return pwd, result
            count += 1
            if count % 100 == 0:
                print(f"  Tried {count} permutations...")
        
        return None, None
    
    def run_all(self):
        """Run all brute force methods"""
        print("310 BTC Smart Brute Force")
        print("=" * 50)
        
        methods = [
            ("Variations", self.try_variations),
            ("Hex combinations", self.try_hex_combinations),
            ("Mixed", self.try_mixed),
            ("Permutations", self.try_permutations_short),
        ]
        
        for name, method in methods:
            print(f"\n{'='*50}")
            print(f"Method: {name}")
            print('='*50)
            pwd, result = method()
            if pwd:
                print(f"\n✅ FOUND!")
                print(f"Password: {pwd}")
                print(f"Result: {result}")
                return pwd, result
        
        print("\n❌ Password not found")
        return None, None

if __name__ == "__main__":
    forcer = SmartBruteForcer()
    password, result = forcer.run_all()
    
    if password:
        print("\n" + "=" * 50)
        print("SOLUTION FOUND")
        print("=" * 50)
        with open('solution.txt', 'w') as f:
            f.write(f"Password: {password}\n")
            f.write(f"Result: {result}\n")
        print("Saved to solution.txt")