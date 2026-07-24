#!/usr/bin/env python3
"""
Pattern Detector - High Priority Tool
Automatically detect cipher and encoding types
"""

import re
import string
from collections import Counter

class PatternDetector:
    """Automatically detect patterns in ciphertext"""
    
    def __init__(self):
        pass
    
    def analyze_text(self, text):
        """Comprehensive text analysis"""
        analysis = {
            'length': len(text),
            'alphabet': set(text),
            'alphabet_size': len(set(text)),
            'is_printable': all(c in string.printable for c in text),
            'frequency': self._frequency_analysis(text),
            'patterns': self._find_patterns(text)
        }
        
        # Detect specific types
        analysis['detections'] = self._detect_types(text, analysis)
        
        return analysis
    
    def _frequency_analysis(self, text):
        """Analyze character frequency"""
        text = text.upper()
        letters = [c for c in text if c.isalpha()]
        
        if not letters:
            return {}
        
        freq = Counter(letters)
        total = len(letters)
        
        return {letter: count/total for letter, count in freq.most_common()}
    
    def _find_patterns(self, text):
        """Find repeating patterns"""
        patterns = {}
        
        # Check for repeating sequences
        for length in range(2, 10):
            for i in range(len(text) - length):
                seq = text[i:i+length]
                if seq in text[i+length:]:
                    patterns[seq] = patterns.get(seq, 0) + 1
        
        return patterns
    
    def _detect_types(self, text, analysis):
        """Detect cipher/encoding types"""
        detections = []
        
        # Check Base64
        if self._is_base64(text):
            detections.append({
                'type': 'Base64',
                'confidence': 0.9,
                'reason': 'Valid Base64 characters and padding'
            })
        
        # Check Hex
        if self._is_hex(text):
            detections.append({
                'type': 'Hexadecimal',
                'confidence': 0.95,
                'reason': 'Valid hex digits (0-9, A-F)'
            })
        
        # Check Binary
        if self._is_binary(text):
            detections.append({
                'type': 'Binary',
                'confidence': 0.95,
                'reason': 'Only 0s and 1s'
            })
        
        # Check Caesar/ROT
        if self._is_likely_caesar(text, analysis):
            detections.append({
                'type': 'Caesar/ROT Cipher',
                'confidence': 0.7,
                'reason': 'Letter frequency suggests simple substitution'
            })
        
        # Check Vigenère
        if self._is_likely_vigenere(text, analysis):
            detections.append({
                'type': 'Vigenère Cipher',
                'confidence': 0.6,
                'reason': 'Index of coincidence suggests polyalphabetic'
            })
        
        # Check Morse
        if self._is_morse(text):
            detections.append({
                'type': 'Morse Code',
                'confidence': 0.9,
                'reason': 'Only dots, dashes, and spaces'
            })
        
        # Check URL encoding
        if '%' in text:
            detections.append({
                'type': 'URL Encoded',
                'confidence': 0.8,
                'reason': 'Contains % characters'
            })
        
        return detections
    
    def _is_base64(self, s):
        """Check if Base64"""
        import base64
        try:
            if len(s) % 4 != 0:
                return False
            base64.b64decode(s)
            return True
        except:
            return False
    
    def _is_hex(self, s):
        """Check if Hex"""
        try:
            int(s, 16)
            return len(s) % 2 == 0 and all(c in '0123456789abcdefABCDEF' for c in s)
        except:
            return False
    
    def _is_binary(self, s):
        """Check if Binary"""
        return set(s).issubset({'0', '1', ' '})
    
    def _is_morse(self, s):
        """Check if Morse"""
        return set(s).issubset({'.', '-', ' ', '/'})
    
    def _is_likely_caesar(self, text, analysis):
        """Check if likely Caesar cipher"""
        freq = analysis['frequency']
        if not freq:
            return False
        
        # Check if frequency distribution matches English
        most_common = list(freq.keys())[:6]
        english_common = ['E', 'T', 'A', 'O', 'I', 'N']
        
        # If common letters are at top, likely simple substitution
        matches = sum(1 for c in most_common if c in english_common)
        return matches >= 3
    
    def _is_likely_vigenere(self, text, analysis):
        """Check if likely Vigenère"""
        # Calculate Index of Coincidence
        text = ''.join(c for c in text.upper() if c.isalpha())
        if len(text) < 10:
            return False
        
        freq = analysis['frequency']
        n = len(text)
        ic = sum(f * (f-1) for f in [text.count(c) for c in set(text)]) / (n * (n-1))
        
        # English IC is ~0.067, random is ~0.038
        # Vigenère has IC closer to random but higher
        return 0.04 < ic < 0.06
    
    def suggest_tools(self, analysis):
        """Suggest tools to try"""
        suggestions = []
        
        for detection in analysis['detections']:
            d_type = detection['type']
            
            if d_type == 'Base64':
                suggestions.append('encoding_tools.decode_base64()')
            elif d_type == 'Hexadecimal':
                suggestions.append('encoding_tools.decode_hex()')
            elif d_type == 'Binary':
                suggestions.append('encoding_tools.decode_binary()')
            elif d_type == 'Caesar/ROT Cipher':
                suggestions.append('advanced_cipher_solver.caesar_brute_force()')
            elif d_type == 'Vigenère Cipher':
                suggestions.append('advanced_cipher_solver.vigenere_solve()')
        
        return suggestions

def main():
    detector = PatternDetector()
    
    print("="*70)
    print("🎯 PATTERN DETECTOR - PRODUCTION")
    print("="*70)
    print()
    
    # Demo
    test_text = "SGVsbG8sIFdvcmxkIQ=="  # Base64 of "Hello, World!"
    
    print(f"Analyzing: {test_text}")
    print()
    
    result = detector.analyze_text(test_text)
    
    print(f"Length: {result['length']}")
    print(f"Alphabet size: {result['alphabet_size']}")
    print()
    
    print("Detections:")
    for detection in result['detections']:
        print(f"  • {detection['type']} ({detection['confidence']*100:.0f}%)")
        print(f"    Reason: {detection['reason']}")
    
    print()
    print("Suggestions:")
    for suggestion in detector.suggest_tools(result):
        print(f"  • Try: {suggestion}")

if __name__ == "__main__":
    main()
