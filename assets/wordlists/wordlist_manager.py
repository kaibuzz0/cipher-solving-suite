#!/usr/bin/env python3
"""
Wordlist Manager - Critical Tool
Generate and manage password dictionaries
"""

import os
import itertools

class WordlistManager:
    """Generate and manage wordlists for password cracking"""
    
    COMMON_PASSWORDS = [
        'password', '123456', '12345678', 'qwerty', 'abc123',
        'monkey', 'letmein', 'dragon', '111111', 'baseball',
        'iloveyou', 'trustno1', 'sunshine', 'princess', 'admin',
        'welcome', 'shadow', 'ashley', 'football', 'jesus',
        'michael', 'ninja', 'mustang', 'password1', '123456789',
        'adobe123', 'admin123', 'letmein1', 'photoshop', '1234567'
    ]
    
    def __init__(self, wordlist_dir="assets/wordlists"):
        self.wordlist_dir = wordlist_dir
        os.makedirs(wordlist_dir, exist_ok=True)
    
    def get_common_passwords(self):
        """Return list of common passwords"""
        return self.COMMON_PASSWORDS
    
    def generate_combinations(self, words, separator='', min_len=2, max_len=3):
        """Generate word combinations"""
        combinations = []
        
        for length in range(min_len, max_len + 1):
            for combo in itertools.permutations(words, length):
                combinations.append(separator.join(combo))
        
        return combinations
    
    def generate_mutations(self, base_word):
        """Generate password mutations"""
        mutations = set()
        
        # Original
        mutations.add(base_word)
        
        # Capitalizations
        mutations.add(base_word.lower())
        mutations.add(base_word.upper())
        mutations.add(base_word.capitalize())
        mutations.add(base_word.swapcase())
        
        # Numbers
        for i in range(1000):
            mutations.add(f"{base_word}{i}")
            mutations.add(f"{i}{base_word}")
        
        # Special chars
        special = ['!', '@', '#', '$', '%', '^', '&', '*', '123', '1', '01']
        for char in special:
            mutations.add(f"{base_word}{char}")
            mutations.add(f"{char}{base_word}")
        
        # Years
        for year in range(1970, 2027):
            mutations.add(f"{base_word}{year}")
            mutations.add(f"{year}{base_word}")
        
        return list(mutations)
    
    def save_wordlist(self, name, words):
        """Save wordlist to file"""
        filepath = os.path.join(self.wordlist_dir, f"{name}.txt")
        
        with open(filepath, 'w') as f:
            for word in words:
                f.write(f"{word}\n")
        
        print(f"[+] Saved wordlist: {filepath} ({len(words)} words)")
        return filepath
    
    def load_wordlist(self, name):
        """Load wordlist from file"""
        filepath = os.path.join(self.wordlist_dir, f"{name}.txt")
        
        if not os.path.exists(filepath):
            return self.COMMON_PASSWORDS
        
        with open(filepath, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    
    def create_default_wordlists(self):
        """Create default wordlists"""
        print("[*] Creating default wordlists...")
        
        # Common passwords
        self.save_wordlist("common_passwords", self.COMMON_PASSWORDS)
        
        # Numbers only
        numbers = [str(i) for i in range(10000)]
        self.save_wordlist("numbers", numbers)
        
        # Years
        years = [str(y) for y in range(1950, 2027)]
        self.save_wordlist("years", years)
        
        # Common mutations
        mutations = []
        for word in ['password', 'admin', 'user', 'login']:
            mutations.extend(self.generate_mutations(word)[:100])
        self.save_wordlist("mutations", mutations)
        
        print("[+] Default wordlists created!")

def main():
    manager = WordlistManager()
    
    print("="*70)
    print("📚 WORDLIST MANAGER - PRODUCTION")
    print("="*70)
    print()
    
    # Create default wordlists
    manager.create_default_wordlists()
    
    print()
    print("Usage:")
    print("  from assets.wordlists.wordlist_manager import WordlistManager")
    print("  manager = WordlistManager()")
    print("  words = manager.load_wordlist('common_passwords')")

if __name__ == "__main__":
    main()
