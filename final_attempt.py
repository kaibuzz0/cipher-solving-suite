#!/usr/bin/env python3
"""
310 BTC Challenge - Final Attempt: Smart Combinations
Try hex grid in different reading orders + character combinations
"""

from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Hash import SHA256
from Cryptodome.Util.Padding import unpad
import base64
import itertools

class FinalAttempt:
    def __init__(self):
        with open('/root/310_btc_challenge/alpha_row310.bin', 'rb') as f:
            data = f.read()
        self.encrypted_data = base64.b64decode(data)
        self.salt = self.encrypted_data[8:16]
        self.ciphertext = self.encrypted_data[16:]
        
        self.hex_grid = [
            ["511", "B20", "332", "328", "410", "530"],
            ["22B", "0FE", "52E", "D0F", "7A1", "65B"],
            ["52C", "7E7", "511", "2F6", "56F", "C4B"]
        ]
        
        self.flat_hex = ["511", "B20", "332", "328", "410", "530",
                        "22B", "0FE", "52E", "D0F", "7A1", "65B",
                        "52C", "7E7", "511", "2F6", "56F", "C4B"]
        
        self.chars = "L3CEO275KOD899D4FA1F64"
    
    def try_decrypt(self, password):
        try:
            key_iv = PBKDF2(password.encode(), self.salt, dkLen=48, count=1000, hmac_hash_module=SHA256)
            key = key_iv[:32]
            iv = key_iv[32:]
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted = cipher.decrypt(self.ciphertext)
            unpadded = unpad(decrypted, AES.block_size)
            return unpadded
        except:
            return None
    
    def check_bitcoin_key(self, data):
        if not data:
            return False, None
        try:
            text = data.decode('latin-1')
            base58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
            
            # Look for valid Bitcoin key
            for start in ['5', 'K', 'L']:
                idx = text.find(start)
                if idx >= 0:
                    key = start
                    for c in text[idx+1:]:
                        if c in base58:
                            key += c
                        else:
                            break
                        if len(key) >= 51:
                            return True, key[:52]
            return False, None
        except:
            return False, None
    
    def try_hex_orders(self):
        """Try different ways to read the hex grid"""
        
        # Row by row
        row_order = ''.join(self.flat_hex)
        
        # Column by column
        col_order = ''
        for col in range(6):
            for row in range(3):
                col_order += self.hex_grid[row][col]
        
        # Reverse row
        rev_row = ''.join(reversed(self.flat_hex))
        
        # Reverse col
        rev_col = ''
        for col in reversed(range(6)):
            for row in range(3):
                rev_col += self.hex_grid[row][col]
        
        # Snake pattern
        snake = ''
        for row in range(3):
            if row % 2 == 0:
                for col in range(6):
                    snake += self.hex_grid[row][col]
            else:
                for col in reversed(range(6)):
                    snake += self.hex_grid[row][col]
        
        orders = [
            ("Row order", row_order),
            ("Column order", col_order),
            ("Reverse row", rev_row),
            ("Reverse col", rev_col),
            ("Snake", snake),
        ]
        
        print("\nTrying hex grid orders...")
        for name, pwd in orders:
            data = self.try_decrypt(pwd)
            found, key = self.check_bitcoin_key(data)
            if found:
                return name, pwd, key
            print(f"  {name}: no")
        
        return None, None, None
    
    def try_segment_combinations(self):
        """Try combinations of 4-char segments"""
        segments = ['L3CE', 'O275', 'KOD8', '99D4', 'FA1F', '64']
        
        print("\nTrying segment permutations (this will take a while)...")
        count = 0
        for perm in itertools.permutations(segments):
            pwd = ''.join(perm)
            data = self.try_decrypt(pwd)
            found, key = self.check_bitcoin_key(data)
            if found:
                return pwd, key
            count += 1
            if count % 720 == 0:  # 6! = 720
                print(f"  Tried {count} permutations...")
            if count > 10000:  # Limit
                break
        
        return None, None
    
    def try_mixed_passwords(self):
        """Try mixed combinations"""
        passwords = [
            # Hex orders
            ''.join(self.flat_hex),
            ''.join(reversed(self.flat_hex)),
            # With separators
            '-'.join(self.flat_hex),
            '_'.join(self.flat_hex),
            # Lowercase
            ''.join(self.flat_hex).lower(),
            # With chars
            self.chars + ''.join(self.flat_hex),
            ''.join(self.flat_hex) + self.chars,
            # Pip combinations
            'pip' + ''.join(self.flat_hex),
            ''.join(self.flat_hex) + 'pip',
            # 310 combinations
            '310' + ''.join(self.flat_hex),
            ''.join(self.flat_hex) + '310',
        ]
        
        print("\nTrying mixed passwords...")
        for pwd in passwords:
            data = self.try_decrypt(pwd)
            found, key = self.check_bitcoin_key(data)
            if found:
                return pwd, key
            print(f"  {pwd[:40]}...: no")
        
        return None, None
    
    def run(self):
        print("=" * 60)
        print("310 BTC - FINAL ATTEMPT")
        print("=" * 60)
        
        # Try hex orders
        name, pwd, key = self.try_hex_orders()
        if pwd:
            print(f"\n✅ FOUND! {name}: {pwd}")
            print(f"Key: {key}")
            return pwd, key
        
        # Try mixed
        pwd, key = self.try_mixed_passwords()
        if pwd:
            print(f"\n✅ FOUND! {pwd}")
            print(f"Key: {key}")
            return pwd, key
        
        # Try segment permutations (limited)
        pwd, key = self.try_segment_combinations()
        if pwd:
            print(f"\n✅ FOUND! {pwd}")
            print(f"Key: {key}")
            return pwd, key
        
        print("\n❌ Not found in tested combinations")
        return None, None

if __name__ == "__main__":
    attempt = FinalAttempt()
    pwd, key = attempt.run()
    
    if pwd and key:
        with open('solution_final.txt', 'w') as f:
            f.write(f"Password: {pwd}\n")
            f.write(f"Key: {key}\n")
        print("\nSaved to solution_final.txt")