#!/usr/bin/env python3
"""
Brute Force Engine - High Priority Tool
Comprehensive brute force attack toolkit
"""

import itertools
import string
import hashlib
from concurrent.futures import ThreadPoolExecutor

class BruteForceEngine:
    """Multi-threaded brute force engine"""
    
    def __init__(self, max_workers=4):
        self.max_workers = max_workers
    
    def brute_password(self, target_hash, hash_type='md5', 
                       charset=string.ascii_lowercase + string.digits,
                       min_len=1, max_len=6, callback=None):
        """Brute force password cracking"""
        
        print(f"[*] Brute forcing {hash_type.upper()}...")
        print(f"[*] Charset: {charset}")
        print(f"[*] Length: {min_len}-{max_len}")
        print(f"[*] Target: {target_hash}")
        
        total_combinations = sum(len(charset)**i for i in range(min_len, max_len+1))
        print(f"[*] Total combinations: {total_combinations:,}")
        
        checked = 0
        
        for length in range(min_len, max_len + 1):
            print(f"[*] Trying length {length}...")
            
            for attempt in itertools.product(charset, repeat=length):
                password = ''.join(attempt)
                checked += 1
                
                # Generate hash
                if hash_type == 'md5':
                    test_hash = hashlib.md5(password.encode()).hexdigest()
                elif hash_type == 'sha1':
                    test_hash = hashlib.sha1(password.encode()).hexdigest()
                elif hash_type == 'sha256':
                    test_hash = hashlib.sha256(password.encode()).hexdigest()
                else:
                    continue
                
                # Check match
                if test_hash == target_hash:
                    print(f"\n[+] FOUND: {password}")
                    return password
                
                # Progress callback
                if callback and checked % 10000 == 0:
                    callback(checked, total_combinations)
        
        print("\n[-] Not found")
        return None
    
    def brute_pattern(self, pattern, known_chars=None, charset=None):
        """Brute force pattern with wildcards"""
        if charset is None:
            charset = string.ascii_lowercase + string.digits
        
        if known_chars is None:
            known_chars = {}
        
        # Find wildcards
        wildcards = [i for i, c in enumerate(pattern) if c == '?']
        
        if not wildcards:
            return [pattern]
        
        results = []
        
        for replacements in itertools.product(charset, repeat=len(wildcards)):
            result = list(pattern)
            for i, char in zip(wildcards, replacements):
                result[i] = char
            results.append(''.join(result))
        
        return results
    
    def dictionary_attack(self, target_hash, wordlist, hash_type='md5'):
        """Dictionary attack with wordlist"""
        print(f"[*] Dictionary attack ({len(wordlist)} words)...")
        
        for i, word in enumerate(wordlist):
            word = word.strip()
            
            if hash_type == 'md5':
                test_hash = hashlib.md5(word.encode()).hexdigest()
            elif hash_type == 'sha1':
                test_hash = hashlib.sha1(word.encode()).hexdigest()
            elif hash_type == 'sha256':
                test_hash = hashlib.sha256(word.encode()).hexdigest()
            else:
                continue
            
            if test_hash == target_hash:
                print(f"[+] Found at position {i}: {word}")
                return word
            
            if i % 1000 == 0:
                print(f"    Progress: {i}/{len(wordlist)}", end='\r')
        
        print("\n[-] Not in dictionary")
        return None
    
    def hybrid_attack(self, target_hash, base_words, hash_type='md5'):
        """Hybrid: Dictionary + Mutations"""
        from assets.wordlists.wordlist_manager import WordlistManager
        
        manager = WordlistManager()
        
        print("[*] Generating mutations...")
        all_candidates = []
        
        for word in base_words:
            mutations = manager.generate_mutations(word)
            all_candidates.extend(mutations)
        
        print(f"[*] Testing {len(all_candidates)} candidates...")
        return self.dictionary_attack(target_hash, all_candidates, hash_type)

def main():
    engine = BruteForceEngine()
    
    print("="*70)
    print("💪 BRUTE FORCE ENGINE - PRODUCTION")
    print("="*70)
    print()
    
    # Demo
    test_password = "abc"
    test_hash = hashlib.md5(test_password.encode()).hexdigest()
    
    print(f"Demo: Brute forcing MD5 of '{test_password}'")
    print(f"Hash: {test_hash}")
    print()
    
    result = engine.brute_password(
        test_hash,
        charset=string.ascii_lowercase,
        min_len=1,
        max_len=3
    )
    
    if result:
        print(f"✓ Cracked: {result}")
    
    print()
    print("Usage:")
    print("  from solvers.brute-force.brute_engine import BruteForceEngine")
    print("  engine = BruteForceEngine()")
    print("  result = engine.brute_password(hash, charset, min_len, max_len)")

if __name__ == "__main__":
    main()
