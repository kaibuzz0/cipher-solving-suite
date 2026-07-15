#!/usr/bin/env python3
"""
310 BTC Challenge - Alpha Channel Data Extraction
The alpha channel showed only 3 values - classic steganography
"""

from PIL import Image
import numpy as np
import os

class AlphaExtractor:
    """Extract hidden data from alpha channel"""
    
    def __init__(self, image_path: str):
        self.img = Image.open(image_path)
        self.arr = np.array(self.img)
        self.height, self.width = self.arr.shape[:2]
        
        if self.arr.shape[2] < 4:
            raise ValueError("Image has no alpha channel")
        
        self.alpha = self.arr[:, :, 3]
        print(f"Image: {self.width}x{self.height}")
        print(f"Alpha unique values: {np.unique(self.alpha)}")
    
    def extract_alpha_lsb(self) -> bytes:
        """Extract LSB from alpha channel"""
        # Alpha values are 253, 254, 255
        # LSB would be: 253=1, 254=0, 255=1
        lsb = self.alpha & 1
        
        # Flatten
        bits = lsb.flatten()
        
        # Pack into bytes
        bytes_data = []
        for i in range(0, len(bits) - 7, 8):
            byte = 0
            for j in range(8):
                byte = (byte << 1) | bits[i + j]
            bytes_data.append(byte)
        
        return bytes(bytes_data)
    
    def extract_alpha_pattern(self) -> bytes:
        """
        Extract based on pattern in alpha values
        253, 254, 255 could encode data
        """
        # Map values to bits
        # 253 = 0, 254 = 1, 255 = ?
        
        mapping = {253: 0, 254: 1}  # 255 could be delimiter or ignore
        
        bits = []
        for val in self.alpha.flatten():
            if val in mapping:
                bits.append(mapping[val])
        
        # Pack into bytes
        bytes_data = []
        for i in range(0, len(bits) - 7, 8):
            byte = 0
            for j in range(8):
                byte = (byte << 1) | bits[i + j]
            bytes_data.append(byte)
        
        return bytes(bytes_data)
    
    def extract_2bit_alpha(self) -> bytes:
        """Treat alpha as 2-bit data source"""
        # 253, 254, 255 in binary:
        # 253 = 11111101 (LSB: 1)
        # 254 = 11111110 (LSB: 0)
        # 255 = 11111111 (LSB: 1)
        
        # Actually let's look at last 2 bits
        two_bits = self.alpha & 0b11
        
        print(f"2-bit pattern unique values: {np.unique(two_bits)}")
        
        # Flatten and pack
        vals = two_bits.flatten()
        bytes_data = []
        
        # 4 values per byte
        for i in range(0, len(vals) - 3, 4):
            byte = (vals[i] << 6) | (vals[i+1] << 4) | (vals[i+2] << 2) | vals[i+3]
            bytes_data.append(byte)
        
        return bytes(bytes_data)
    
    def extract_row_310_alpha(self) -> bytes:
        """Extract specifically from row 310"""
        row = 310
        if row >= self.height:
            return b''
        
        row_alpha = self.alpha[row, :]
        print(f"\nRow 310 alpha values: {np.unique(row_alpha)}")
        
        # Convert to bits
        bits = row_alpha & 1
        
        # Pack
        bytes_data = []
        for i in range(0, len(bits) - 7, 8):
            byte = 0
            for j in range(8):
                byte = (byte << 1) | bits[i + j]
            bytes_data.append(byte)
        
        return bytes(bytes_data)
    
    def analyze_alpha_structure(self):
        """Analyze alpha channel for structure"""
        print("\n=== ALPHA CHANNEL ANALYSIS ===")
        
        # Check if it varies by row
        for row in [0, 100, 200, 310, 500, 1000]:
            if row < self.height:
                row_data = self.alpha[row, :]
                unique = np.unique(row_data)
                print(f"Row {row}: {len(unique)} unique values - {unique[:10]}")
    
    def try_all_extracts(self):
        """Try all extraction methods"""
        print("\n=== ALPHA EXTRACTION RESULTS ===")
        
        # Method 1: Simple LSB
        data1 = self.extract_alpha_lsb()
        print(f"\n1. Simple LSB: {len(data1)} bytes")
        self.check_for_patterns(data1)
        
        # Method 2: Pattern-based
        data2 = self.extract_alpha_pattern()
        print(f"\n2. Pattern-based: {len(data2)} bytes")
        self.check_for_patterns(data2)
        
        # Method 3: 2-bit
        data3 = self.extract_2bit_alpha()
        print(f"\n3. 2-bit: {len(data3)} bytes")
        self.check_for_patterns(data3)
        
        # Method 4: Row 310 only
        data4 = self.extract_row_310_alpha()
        print(f"\n4. Row 310 only: {len(data4)} bytes")
        self.check_for_patterns(data4)
        
        # Save all
        with open('alpha_lsb.bin', 'wb') as f:
            f.write(data1)
        with open('alpha_pattern.bin', 'wb') as f:
            f.write(data2)
        with open('alpha_2bit.bin', 'wb') as f:
            f.write(data3)
        with open('alpha_row310.bin', 'wb') as f:
            f.write(data4)
        
        print("\nSaved to: alpha_lsb.bin, alpha_pattern.bin, alpha_2bit.bin, alpha_row310.bin")
    
    def check_for_patterns(self, data: bytes):
        """Check extracted data for patterns"""
        # Check for printable ASCII
        printable = bytes([b for b in data if 32 <= b < 127])
        if len(printable) > 10:
            print(f"  Printable ASCII found: {printable[:100]}")
        
        # Check for hex string patterns (like private key)
        hex_chars = set('0123456789abcdefABCDEF')
        hex_count = sum(1 for b in data if chr(b) in hex_chars or 32 <= b < 127)
        if hex_count > len(data) * 0.8:
            print(f"  High hex-like content: {hex_count}/{len(data)}")
        
        # Check for repeating patterns
        if len(data) > 32:
            first_32 = data[:32]
            repeats = data.count(first_32)
            if repeats > 1:
                print(f"  Repeating pattern found: {repeats} times")

def main():
    extractor = AlphaExtractor('/root/310_btc_challenge/310_challenge.png')
    extractor.analyze_alpha_structure()
    extractor.try_all_extracts()

if __name__ == "__main__":
    main()