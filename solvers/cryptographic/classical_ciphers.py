#!/usr/bin/env python3
"""
Classical Cipher GUI - High Priority Tool
Quick GUI for common classical ciphers
"""

class ClassicalCiphers:
    """Quick reference for classical ciphers"""
    
    @staticmethod
    def caesar(text, shift):
        """Caesar cipher"""
        result = []
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result.append(chr((ord(char) - base + shift) % 26 + base))
            else:
                result.append(char)
        return ''.join(result)
    
    @staticmethod
    def rot13(text):
        """ROT13 cipher"""
        return ClassicalCiphers.caesar(text, 13)
    
    @staticmethod
    def atbash(text):
        """Atbash cipher (A<->Z, B<->Y)"""
        result = []
        for char in text:
            if char.isalpha():
                if char.isupper():
                    result.append(chr(ord('Z') - (ord(char) - ord('A'))))
                else:
                    result.append(chr(ord('z') - (ord(char) - ord('a'))))
            else:
                result.append(char)
        return ''.join(result)
    
    @staticmethod
    def vigenere(text, key):
        """Vigenere cipher"""
        result = []
        key = key.upper()
        key_len = len(key)
        
        for i, char in enumerate(text):
            if char.isalpha():
                shift = ord(key[i % key_len]) - ord('A')
                if char.isupper():
                    result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
                else:
                    result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            else:
                result.append(char)
        return ''.join(result)
    
    @staticmethod
    def baconian(text, mode='encode'):
        """Bacon cipher"""
        bacon_dict = {
            'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 'E': 'AABAA',
            'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB', 'I': 'ABAAA', 'J': 'ABAAB',
            'K': 'ABABA', 'L': 'ABABB', 'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA',
            'P': 'ABBBB', 'Q': 'BAAAA', 'R': 'BAAAB', 'S': 'BAABA', 'T': 'BAABB',
            'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB', 'Y': 'BBAAA',
            'Z': 'BBAAB'
        }
        
        if mode == 'encode':
            return ' '.join(bacon_dict.get(c.upper(), c) for c in text if c.isalpha())
        else:
            reverse_dict = {v: k for k, v in bacon_dict.items()}
            return ''.join(reverse_dict.get(c, '') for c in text.split())
    
    @staticmethod
    def affine(text, a, b):
        """Affine cipher: ax + b mod 26"""
        result = []
        for char in text:
            if char.isalpha():
                x = ord(char.upper()) - ord('A')
                y = (a * x + b) % 26
                result.append(chr(y + ord('A')))
            else:
                result.append(char)
        return ''.join(result)
    
    @staticmethod
    def rail_fence(text, rails):
        """Rail fence transposition"""
        fence = [[] for _ in range(rails)]
        rail = 0
        direction = 1
        
        for char in text:
            fence[rail].append(char)
            rail += direction
            if rail == rails - 1 or rail == 0:
                direction *= -1
        
        return ''.join(''.join(rail) for rail in fence)

def main():
    ciphers = ClassicalCiphers()
    
    print("="*70)
    print("🔐 CLASSICAL CIPHERS - QUICK REFERENCE")
    print("="*70)
    print()
    
    test = "Hello World"
    
    print(f"Text: '{test}'")
    print()
    print("Available ciphers:")
    print(f"  Caesar (shift 3): {ciphers.caesar(test, 3)}")
    print(f"  ROT13: {ciphers.rot13(test)}")
    print(f"  Atbash: {ciphers.atbash(test)}")
    print(f"  Vigenere (key 'KEY'): {ciphers.vigenere(test, 'KEY')}")
    print(f"  Rail Fence (3 rails): {ciphers.rail_fence(test, 3)}")
    
    print()
    print("Usage:")
    print("  from solvers.cryptographic.classical_ciphers import ClassicalCiphers")
    print("  c = ClassicalCiphers()")
    print("  result = c.caesar('HELLO', 3)  # 'KHOOR'")

if __name__ == "__main__":
    main()
