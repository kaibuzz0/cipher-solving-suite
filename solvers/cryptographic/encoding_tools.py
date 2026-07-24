#!/usr/bin/env python3
"""
Encoding Tools - Critical Tool
Base64, Hex, Binary, URL encoding/decoding with auto-detection
"""

import base64
import binascii
import urllib.parse

class EncodingTools:
    """Universal encoding/decoding toolkit"""
    
    @staticmethod
    def detect_encoding(text):
        """Auto-detect likely encoding"""
        text = text.strip()
        
        # Check if Base64
        if EncodingTools._is_base64(text):
            return 'base64'
        
        # Check if Hex
        if EncodingTools._is_hex(text):
            return 'hex'
        
        # Check if Binary
        if EncodingTools._is_binary(text):
            return 'binary'
        
        # Check if URL encoded
        if '%' in text:
            return 'url'
        
        # Check if Morse code
        if set(text).issubset({'.', '-', ' ', '/'}):
            return 'morse'
        
        return 'unknown'
    
    @staticmethod
    def _is_base64(s):
        """Check if string is valid Base64"""
        try:
            if len(s) % 4 != 0:
                return False
            base64.b64decode(s)
            return True
        except:
            return False
    
    @staticmethod
    def _is_hex(s):
        """Check if string is valid Hex"""
        try:
            int(s, 16)
            return len(s) % 2 == 0 and all(c in '0123456789abcdefABCDEF' for c in s)
        except:
            return False
    
    @staticmethod
    def _is_binary(s):
        """Check if string is valid binary"""
        return set(s).issubset({'0', '1', ' '})
    
    @staticmethod
    def decode_base64(text):
        """Decode Base64"""
        try:
            return base64.b64decode(text).decode('utf-8')
        except:
            return base64.b64decode(text).hex()
    
    @staticmethod
    def encode_base64(text):
        """Encode to Base64"""
        if isinstance(text, str):
            text = text.encode()
        return base64.b64encode(text).decode()
    
    @staticmethod
    def decode_hex(text):
        """Decode Hex"""
        return bytes.fromhex(text).decode('utf-8', errors='ignore')
    
    @staticmethod
    def encode_hex(text):
        """Encode to Hex"""
        if isinstance(text, str):
            text = text.encode()
        return text.hex()
    
    @staticmethod
    def decode_binary(text):
        """Decode Binary"""
        text = text.replace(' ', '')
        return ''.join(chr(int(text[i:i+8], 2)) for i in range(0, len(text), 8))
    
    @staticmethod
    def encode_binary(text):
        """Encode to Binary"""
        return ' '.join(format(ord(c), '08b') for c in text)
    
    @staticmethod
    def decode_url(text):
        """URL Decode"""
        return urllib.parse.unquote(text)
    
    @staticmethod
    def encode_url(text):
        """URL Encode"""
        return urllib.parse.quote(text)
    
    @staticmethod
    def rot13(text):
        """ROT13 Cipher"""
        result = []
        for char in text:
            if char.isalpha():
                shift = 13
                if char.islower():
                    result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a'))))
                else:
                    result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A'))))
            else:
                result.append(char)
        return ''.join(result)
    
    def auto_decode(self, text):
        """Auto-detect and decode"""
        encoding = self.detect_encoding(text)
        
        results = {
            'detected': encoding,
            'original': text
        }
        
        try:
            if encoding == 'base64':
                results['decoded'] = self.decode_base64(text)
            elif encoding == 'hex':
                results['decoded'] = self.decode_hex(text)
            elif encoding == 'binary':
                results['decoded'] = self.decode_binary(text)
            elif encoding == 'url':
                results['decoded'] = self.decode_url(text)
            else:
                results['decoded'] = None
        except Exception as e:
            results['error'] = str(e)
            results['decoded'] = None
        
        return results

def main():
    tools = EncodingTools()
    
    print("="*70)
    print("🔄 ENCODING TOOLS - PRODUCTION")
    print("="*70)
    print()
    
    # Demo
    test_string = "Hello, World!"
    
    print(f"Original: {test_string}")
    print()
    
    # Base64
    b64 = tools.encode_base64(test_string)
    print(f"Base64: {b64}")
    print(f"Decoded: {tools.decode_base64(b64)}")
    print()
    
    # Hex
    hex_str = tools.encode_hex(test_string)
    print(f"Hex: {hex_str}")
    print(f"Decoded: {tools.decode_hex(hex_str)}")
    print()
    
    # Auto-detect
    print("Auto-detect test:")
    result = tools.auto_decode(b64)
    print(f"  Detected: {result['detected']}")
    print(f"  Decoded: {result['decoded']}")

if __name__ == "__main__":
    main()
