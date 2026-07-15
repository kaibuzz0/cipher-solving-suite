#!/usr/bin/env python3
"""
310 BTC Challenge - Targeted Analysis
Focus on known hints from the challenge
"""

from PIL import Image
import numpy as np
import os

class Targeted310Analyzer:
    """Analyze specific areas based on hints"""
    
    def __init__(self, image_path: str):
        self.img = Image.open(image_path)
        self.arr = np.array(self.img)
        self.height, self.width = self.arr.shape[:2]
        print(f"Image: {self.width}x{self.height}")
        
        # Known from hints
        self.row_310 = 310
        self.chars_in_image = "L3CEO275KOD899D4FA1F64"  # 21 chars
        
    def analyze_row_310(self):
        """Deep dive on row 310 - mentioned as having QR code"""
        print("\n=== ROW 310 ANALYSIS ===")
        
        if self.row_310 >= self.height:
            print("Row 310 doesn't exist")
            return
        
        # Get row data
        row_data = self.arr[self.row_310, :, :3]  # RGB
        
        # Check each channel's LSB
        for name, idx in [('R', 0), ('G', 1), ('B', 2)]:
            channel = row_data[:, idx]
            lsb = channel & 1
            
            # Convert to bytes
            bits = lsb.flatten()
            bytes_data = []
            for i in range(0, len(bits), 8):
                if i + 8 <= len(bits):
                    byte = 0
                    for j in range(8):
                        byte = (byte << 1) | bits[i + j]
                    bytes_data.append(byte)
            
            byte_str = bytes(bytes_data)
            
            # Look for patterns
            print(f"\n{name} channel LSB:")
            print(f"  First 20 bytes: {byte_str[:20].hex()}")
            
            # Check for QR code pattern (dark modules)
            # QR has specific finder patterns at corners
            if np.mean(lsb) > 0.45 and np.mean(lsb) < 0.55:
                print(f"  Pattern: Balanced - could be data")
            elif np.mean(lsb) > 0.7:
                print(f"  Pattern: Mostly white - could be QR finder")
            elif np.mean(lsb) < 0.3:
                print(f"  Pattern: Mostly dark - could be QR data")
    
    def extract_combined_lsb(self, row: int) -> bytes:
        """Extract LSB combining all channels in sequence"""
        if row >= self.height:
            return b''
        
        row_data = self.arr[row, :, :3]
        
        # Interleave R,G,B LSBs
        bits = []
        for i in range(row_data.shape[0]):
            bits.append(row_data[i, 0] & 1)  # R
            bits.append(row_data[i, 1] & 1)  # G
            bits.append(row_data[i, 2] & 1)  # B
        
        # Pack into bytes
        bytes_data = []
        for i in range(0, len(bits) - 7, 8):
            byte = 0
            for j in range(8):
                byte = (byte << 1) | bits[i + j]
            bytes_data.append(byte)
        
        return bytes(bytes_data)
    
    def check_qr_signature(self):
        """Look for QR code finder patterns"""
        print("\n=== QR CODE SCAN ===")
        
        # QR finder pattern: ratio 1:1:3:1:1
        # Look for this in row 310
        
        row_data = self.arr[self.row_310, :, :3]
        gray = np.mean(row_data, axis=1).astype(np.uint8)
        
        # Simple edge detection
        diff = np.abs(np.diff(gray))
        
        # Look for regions with high contrast changes
        edges = np.where(diff > 100)[0]
        
        print(f"Found {len(edges)} high-contrast edges in row 310")
        
        if len(edges) > 10:
            print(f"Edge positions: {edges[:20]}")
    
    def extract_alpha_channel(self):
        """Check if there's data in alpha channel"""
        if self.arr.shape[2] < 4:
            print("\nNo alpha channel (RGB only)")
            return
        
        alpha = self.arr[:, :, 3]
        unique = np.unique(alpha)
        
        print(f"\n=== ALPHA CHANNEL ===")
        print(f"Unique values: {len(unique)}")
        print(f"Values: {unique[:20]}")
        
        if len(unique) < 10:
            print("Low entropy - possible data hidden here")
            
            # Check row 310 specifically
            row_alpha = alpha[self.row_310, :]
            print(f"Row 310 alpha: {row_alpha[:50]}")
    
    def scan_for_hex_values(self):
        """Scan for the known hex grid values"""
        hex_values = [0x511, 0xB20, 0x332, 0x328, 0x410, 0x530, 
                      0x22B, 0x0FE, 0x52E, 0xD0F, 0x7A1, 0x65B,
                      0x52C, 0x7E7, 0x2F6, 0x56F, 0xC4B]
        
        print("\n=== HEX VALUE SEARCH ===")
        
        # Check if these appear in image data
        found = 0
        for val in hex_values:
            if val < 256:
                # Could be in single byte
                if val in self.arr:
                    found += 1
            else:
                # Would span multiple bytes
                pass
        
        print(f"Found {found}/{len(hex_values)} hex values in raw data")
    
    def save_row_310_extracted(self):
        """Save row 310 as separate image for manual inspection"""
        # Extract rows around 310
        start = max(0, self.row_310 - 5)
        end = min(self.height, self.row_310 + 6)
        
        region = self.arr[start:end, :, :]
        
        img = Image.fromarray(region.astype(np.uint8))
        img.save('row_310_region.png')
        print("\nSaved row_310_region.png (11 rows centered on 310)")

def main():
    analyzer = Targeted310Analyzer('/root/310_btc_challenge/310_challenge.png')
    
    analyzer.analyze_row_310()
    analyzer.check_qr_signature()
    analyzer.extract_alpha_channel()
    analyzer.scan_for_hex_values()
    analyzer.save_row_310_extracted()
    
    # Try extracting combined LSB
    print("\n=== COMBINED LSB EXTRACTION (Row 310) ===")
    data = analyzer.extract_combined_lsb(310)
    print(f"Extracted {len(data)} bytes")
    print(f"Hex: {data[:50].hex()}")
    
    # Look for printable
    printable = bytes([b for b in data if 32 <= b < 127])
    if printable:
        print(f"Printable: {printable}")

if __name__ == "__main__":
    main()