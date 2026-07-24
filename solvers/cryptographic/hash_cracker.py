#!/usr/bin/env python3
"""
Hash Cracker - Critical Tool
Crack MD5, SHA1, SHA256, SHA512 hashes
"""

import hashlib
import itertools
import string
from datetime import datetime

class HashCracker:
    """Crack password hashes using multiple methods"""
    
    COMMON_PASSWORDS = [
        'password', '123456', 'admin', 'root', 'toor',
        'password123', 'admin123', 'letmein', 'welcome',
        'qwerty', 'abc123', 'password1', '12345678',
        'sunshine', 'princess', 'dragon', 'baseball',
        'football', 'monkey', 'master', 'hello',
        'shadow', 'superman', 'batman', 'trustno1'
    ]
    
    def __init__(self):
        self.wordlist = []
    
    def identify_hash(self, hash_value):
        """Identify hash type by length"""
        lengths = {
            32: 'MD5',
            40: 'SHA1',
            64: 'SHA256',
            128: 'SHA512'
        }
        return lengths.get(len(hash_value), 'Unknown')
    
    def crack_dict(self, target_hash, wordlist=None):
        """Crack using dictionary attack"""
        if wordlist is None:
            wordlist = self.COMMON_PASSWORDS
        
        hash_type = self.identify_hash(target_hash)
        print(f"[*] Attempting to crack {hash_type}: {target_hash}")
        
        for word in wordlist:
            word = word.strip()
            
            if hash_type == 'MD5':
                if hashlib.md5(word.encode()).hexdigest() == target_hash:
                    return word
            elif hash_type == 'SHA1':
                if hashlib.sha1(word.encode()).hexdigest() == target_hash:
                    return word
            elif hash_type == 'SHA256':
                if hashlib.sha256(word.encode()).hexdigest() == target_hash:
                    return word
            elif hash_type == 'SHA512':
                if hashlib.sha512(word.encode()).hexdigest() == target_hash:
                    return word
        
        return None
    
    def crack_brute(self, target_hash, charset=string.ascii_lowercase, min_len=1, max_len=4):
        """Brute force attack"""
        hash_type = self.identify_hash(target_hash)
        print(f"[*] Brute forcing {hash_type}: {target_hash}")
        print(f"[*] Charset: {charset}")
        print(f"[*] Length: {min_len}-{max_len}")
        
        for length in range(min_len, max_len + 1):
            print(f"[*] Trying length {length}...")
            
            for attempt in itertools.product(charset, repeat=length):
                word = ''.join(attempt)
                
                if hash_type == 'MD5':
                    if hashlib.md5(word.encode()).hexdigest() == target_hash:
                        return word
                elif hash_type == 'SHA1':
                    if hashlib.sha1(word.encode()).hexdigest() == target_hash:
                        return word
                elif hash_type == 'SHA256':
                    if hashlib.sha256(word.encode()).hexdigest() == target_hash:
                        return word
        
        return None
    
    def generate_hash(self, plaintext, algorithm='md5'):
        """Generate hash from plaintext"""
        if algorithm == 'md5':
            return hashlib.md5(plaintext.encode()).hexdigest()
        elif algorithm == 'sha1':
            return hashlib.sha1(plaintext.encode()).hexdigest()
        elif algorithm == 'sha256':
            return hashlib.sha256(plaintext.encode()).hexdigest()
        elif algorithm == 'sha512':
            return hashlib.sha512(plaintext.encode()).hexdigest()

def main():
    cracker = HashCracker()
    
    print("="*70)
    print("🔐 HASH CRACKER - PRODUCTION")
    print("="*70)
    print()
    
    # Demo
    test_password = "admin"
    test_hash = cracker.generate_hash(test_password, 'md5')
    
    print(f"Test: MD5 of '{test_password}' = {test_hash}")
    print()
    
    # Crack it
    result = cracker.crack_dict(test_hash)
    
    if result:
        print(f"✓ Cracked! Password: {result}")
    else:
        print("✗ Not found in dictionary")
    
    print()
    print("Usage:")
    print("  from solvers.cryptographic.hash_cracker import HashCracker")
    print("  cracker = HashCracker()")
    print("  result = cracker.crack_dict(hash_value)")

if __name__ == "__main__":
    main()
