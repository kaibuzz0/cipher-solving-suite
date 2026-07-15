#!/usr/bin/env python3
"""
310 BTC Challenge - Bitplane Analyzer
Looks for patterns, QR codes, and hidden data in bitplanes
"""

from PIL import Image
import numpy as np
import os
import sys

class BitplaneScanner:
    """Scan extracted bitplanes for hidden patterns"""
    
    def __init__(self, bitplane_dir: str):
        self.bitplane_dir = bitplane_dir
        self.findings = []
    
    def scan_file(self, filepath: str):
        """Scan a single bitplane file"""
        img = Image.open(filepath)
        arr = np.array(img)
        
        filename = os.path.basename(filepath)
        
        # Basic stats
        white_pixels = np.sum(arr > 128)
        total_pixels = arr.size
        white_ratio = white_pixels / total_pixels
        
        result = {
            'file': filename,
            'white_ratio': white_ratio,
            'mean': np.mean(arr),
            'has_structure': False,
            'patterns': []
        }
        
        # Check for structure (not random noise)
        # Look for vertical/horizontal lines
        h_diff = np.abs(np.diff(arr, axis=0))
        v_diff = np.abs(np.diff(arr, axis=1))
        
        h_edges = np.sum(h_diff > 200) / h_diff.size
        v_edges = np.sum(v_diff > 200) / v_diff.size
        
        result['h_edges'] = h_edges
        result['v_edges'] = v_edges
        result['has_structure'] = (h_edges > 0.01) or (v_edges > 0.01)
        
        # Look for QR-like patterns (finder patterns: 3 squares in corners)
        # This is a simplified check
        if result['has_structure']:
            result['patterns'].append('edge_structure')
        
        return result
    
    def scan_all(self):
        """Scan all bitplane files"""
        files = sorted([f for f in os.listdir(self.bitplane_dir) if f.endswith('.png')])
        
        print(f"Scanning {len(files)} bitplane files...")
        print("=" * 60)
        
        results = []
        for f in files:
            filepath = os.path.join(self.bitplane_dir, f)
            try:
                result = self.scan_file(filepath)
                results.append(result)
                
                status = "🔍 STRUCTURE" if result['has_structure'] else "noise"
                print(f"{f:30s} | {result['white_ratio']:.3f} | {status}")
                
            except Exception as e:
                print(f"Error scanning {f}: {e}")
        
        # Summary
        print("\n" + "=" * 60)
        print("SUMMARY:")
        structured = [r for r in results if r['has_structure']]
        print(f"  Files with structure: {len(structured)}/{len(results)}")
        
        if structured:
            print("\n  Files worth investigating:")
            for r in structured:
                print(f"    - {r['file']}")
        
        return results
    
    def extract_row_data(self, image_path: str, row: int):
        """Extract data from specific row of bitplane"""
        img = Image.open(image_path)
        arr = np.array(img)
        
        if row >= arr.shape[0]:
            return None
        
        row_data = arr[row, :]
        
        # Convert to bits
        bits = (row_data > 128).astype(int)
        
        # Pack into bytes
        bytes_data = []
        for i in range(0, len(bits), 8):
            byte_bits = bits[i:i+8]
            if len(byte_bits) == 8:
                byte_val = sum(b << (7-j) for j, b in enumerate(byte_bits))
                bytes_data.append(byte_val)
        
        return bytes(bytes_data)
    
    def search_for_text(self, image_path: str):
        """Search bitplane for ASCII text patterns"""
        img = Image.open(image_path)
        arr = np.array(img)
        
        # Flatten and look for printable sequences
        flat = arr.flatten()
        bits = (flat > 128).astype(int)
        
        # Convert to bytes
        text = ""
        for i in range(0, len(bits), 8):
            byte_bits = bits[i:i+8]
            if len(byte_bits) == 8:
                byte_val = sum(b << (7-j) for j, b in enumerate(byte_bits))
                if 32 <= byte_val <= 126:
                    text += chr(byte_val)
                else:
                    if len(text) > 10:
                        return text
                    text = ""
        
        return text if len(text) > 10 else None

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('bitplane_dir', help='Directory with bitplane images')
    parser.add_argument('--scan', action='store_true', help='Scan all bitplanes')
    parser.add_argument('--text-search', action='store_true', help='Search for text in bitplanes')
    args = parser.parse_args()
    
    scanner = BitplaneScanner(args.bitplane_dir)
    
    if args.scan:
        scanner.scan_all()
    
    if args.text_search:
        print("\nSearching for text patterns...")
        files = sorted([f for f in os.listdir(args.bitplane_dir) if f.endswith('.png')])
        for f in files:
            text = scanner.search_for_text(os.path.join(args.bitplane_dir, f))
            if text:
                print(f"\n{f}:")
                print(f"  Found: {text[:100]}...")

if __name__ == "__main__":
    main()