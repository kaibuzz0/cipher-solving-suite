#!/usr/bin/env python3
"""
XOR Cipher Tool - High Priority Tool
XOR encryption/decryption with key guessing
"""

import itertools
import string
from collections import Counter

class XORTool:
    """XOR cipher analysis and cracking"""
    
    def __init__(self):
        self.common_words = ['the', 'and', 'for', 'are', 'but', 'not', 'you', 'all']
    
    def xor_bytes(self, data, key):
        """XOR data with key"""
        return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])
    
    def xor_hex(self, hex_data, key):
        """XOR hex string with key"""
        data = bytes.fromhex(hex_data)
        key_bytes = key.encode() if isinstance(key, str) else key
        result = self.xor_bytes(data, key_bytes)
        return result.hex()
    
    def xor_strings(self, text, key):
        """XOR two strings"""
        return ''.join(chr(ord(t) ^ ord(k)) for t, k in zip(text, itertools.cycle(key)))
    
    def crack_single_byte(self, data):
        """Crack single-byte XOR"""
        best_score = -1
        best_key = None
        best_result = None
        
        for key in range(256):
            result = bytes([b ^ key for b in data])
            
            # Check if printable
            try:
                text = result.decode('ascii')
                if all(c in string.printable for c in text):
                    # Score based on common characters
                    score = sum(1 for c in text.lower() if c in 'etaoinsrhl ')
                    if score > best_score:
                        best_score = score
                        best_key = key
                        best_result = text
            except:
                continue
        
        return best_key, best_result
    
    def crack_repeating_xor(self, data, min_keylen=2, max_keylen=10):
        """Crack repeating-key XOR"""
        best_result = None
        best_key = None
        
        for keylen in range(min_keylen, max_keylen + 1):
            # Split into blocks
            blocks = [data[i::keylen] for i in range(keylen)]
            
            # Crack each block as single-byte XOR
            key = []
            plaintext = []
            
            for block in blocks:
                k, p = self.crack_single_byte(block)
                if k is not None:
                    key.append(k)
                    plaintext.append(p)
            
            if len(key) == keylen:
                # Reconstruct
                result = ''.join(''.join(row[i] for row in plaintext if i < len(row)) 
                                for i in range(max(len(p) for p in plaintext)))
                
                # Score
                score = sum(1 for word in self.common_words if word in result.lower())
                if score > 2:
                    best_key = bytes(key).hex()
                    best_result = result
        
        return best_key, best_result
    
    def hamming_distance(self, b1, b2):
        """Calculate Hamming distance between two byte strings"""
        return sum(bin(x ^ y).count('1') for x, y in zip(b1, b2))

def main():
    xor = XORTool()
    
    print("="*70)
    print("🔑 XOR CIPHER TOOL - PRODUCTION")
    print("="*70)
    print()
    
    # Demo
    original = "Hello, World!"
    key = b"secret"
    
    print(f"Original: {original}")
    print(f"Key: {key}")
    
    # Encrypt
    encrypted = xor.xor_bytes(original.encode(), key)
    print(f"Encrypted (hex): {encrypted.hex()}")
    
    # Decrypt
    decrypted = xor.xor_bytes(encrypted, key)
    print(f"Decrypted: {decrypted.decode()}")
    
    print()
    print("Usage:")
    print("  from solvers.cryptographic.xor_tool import XORTool")
    print("  xor = XORTool()")
    print("  # Encrypt")
    print("  encrypted = xor.xor_bytes(b'Text', b'key')")
    print("  # Decrypt")
    print("  decrypted = xor.xor_bytes(encrypted, b'key')")

if __name__ == "__main__":
    main()
