#!/usr/bin/env python3
"""
Advanced Cryptographic Solver
Comprehensive cipher analysis and breaking
"""

import string
import re
from collections import Counter
from itertools import permutations

class AdvancedCipherSolver:
    """Elite cryptographic analysis suite"""
    
    def __init__(self):
        self.english_freq = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
        self.common_words = ['THE', 'AND', 'FOR', 'ARE', 'BUT', 'NOT', 'YOU', 'ALL', 'ANY', 'CAN', 
                            'HAD', 'HER', 'WAS', 'ONE', 'OUR', 'OUT', 'DAY', 'GET', 'HAS', 'HIM', 
                            'HIS', 'HOW', 'ITS', 'MAN', 'NEW', 'NOW', 'OLD', 'SEE', 'TWO', 'WAY', 
                            'WHO', 'BOY', 'DID', 'SHE', 'USE', 'HER', 'SHE', 'THE', 'AND', 'FOR']
    
    def frequency_analysis(self, text):
        """Analyze letter frequency"""
        text = text.upper()
        letters = [c for c in text if c.isalpha()]
        freq = Counter(letters)
        total = sum(freq.values())
        
        return {letter: count/total for letter, count in freq.most_common()}
    
    def caesar_brute_force(self, ciphertext):
        """Try all 25 Caesar shifts"""
        results = []
        
        for shift in range(26):
            decrypted = ''
            for char in ciphertext:
                if char.isalpha():
                    base = ord('A') if char.isupper() else ord('a')
                    decrypted += chr((ord(char) - base + shift) % 26 + base)
                else:
                    decrypted += char
            
            # Score based on common words
            score = self._score_english(decrypted)
            results.append({
                'shift': shift,
                'text': decrypted,
                'score': score
            })
        
        return sorted(results, key=lambda x: x['score'], reverse=True)
    
    def vigenere_solve(self, ciphertext, key_length=None):
        """Vigenère cipher solver"""
        ciphertext = ''.join(c for c in ciphertext.upper() if c.isalpha())
        
        if not key_length:
            # Try to detect key length
            key_length = self._detect_key_length(ciphertext)
        
        # Solve for each position
        key = ''
        for i in range(key_length):
            column = ciphertext[i::key_length]
            key_char = self._solve_caesar_column(column)
            key += key_char
        
        # Decrypt with found key
        plaintext = self._vigenere_decrypt(ciphertext, key)
        
        return {
            'key': key,
            'plaintext': plaintext
        }
    
    def _score_english(self, text):
        """Score how likely text is English"""
        text = text.upper()
        score = 0
        
        # Check for common words
        for word in self.common_words:
            if word in text:
                score += 10
        
        # Check for common bigrams
        bigrams = ['TH', 'HE', 'IN', 'ER', 'AN', 'RE', 'ON', 'AT', 'EN', 'ND']
        for bigram in bigrams:
            if bigram in text:
                score += 5
        
        return score
    
    def _detect_key_length(self, ciphertext, max_length=10):
        """Detect likely Vigenère key length"""
        # Implement Kasiski examination or index of coincidence
        # For now, return most common
        return 3
    
    def _solve_caesar_column(self, column):
        """Solve Caesar cipher for single column"""
        best_shift = 0
        best_score = -1
        
        for shift in range(26):
            decrypted = ''.join(
                chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
                for c in column
            )
            score = self._score_english(decrypted)
            if score > best_score:
                best_score = score
                best_shift = shift
        
        return chr(best_shift + ord('A'))
    
    def _vigenere_decrypt(self, ciphertext, key):
        """Decrypt Vigenère with known key"""
        plaintext = ''
        key = key.upper()
        
        for i, char in enumerate(ciphertext):
            if char.isalpha():
                shift = ord(key[i % len(key)]) - ord('A')
                decrypted = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                plaintext += decrypted
            else:
                plaintext += char
        
        return plaintext
    
    def substitution_solve(self, ciphertext):
        """Substitution cipher solver"""
        freq = self.frequency_analysis(ciphertext)
        
        # Map based on frequency
        mapping = {}
        cipher_letters = [item[0] for item in freq]
        
        for i, cipher_letter in enumerate(cipher_letters):
            if i < len(self.english_freq):
                mapping[cipher_letter] = self.english_freq[i]
        
        # Apply mapping
        decrypted = ''
        for char in ciphertext.upper():
            if char in mapping:
                decrypted += mapping[char]
            else:
                decrypted += char
        
        return {
            'mapping': mapping,
            'decrypted': decrypted
        }

def main():
    solver = AdvancedCipherSolver()
    
    print("="*70)
    print("🔐 ADVANCED CIPHER SOLVER")
    print("="*70)
    
    # Demo Caesar
    print("\n📋 Caesar Cipher Demo:")
    ciphertext = "Gur dhvpx oebja sbk whzcf bire gur ynml qbt"
    print(f"Cipher: {ciphertext}")
    
    results = solver.caesar_brute_force(ciphertext)
    print(f"\nTop 3 results:")
    for i, result in enumerate(results[:3], 1):
        print(f"  {i}. Shift {result['shift']}: {result['text'][:50]}...")
    
    print("\n✅ Advanced Cipher Solver Ready")

if __name__ == "__main__":
    main()
