#!/usr/bin/env python3
"""
310 BTC Challenge - Steganography Analysis Toolkit
Phone-optimized for Termux/Python
"""

from PIL import Image
import numpy as np
import sys
import os
from typing import Tuple, Optional

class StegAnalyzer:
    """Steganography analysis for 310 BTC Challenge"""
    
    def __init__(self, image_path: str):
        self.image_path = image_path
        self.img = Image.open(image_path)
        self.img_array = np.array(self.img)
        self.height, self.width = self.img_array.shape[:2]
        print(f"Image loaded: {self.width}x{self.height}")
        print(f"Mode: {self.img.mode}")
        print(f"Channels: {len(self.img_array.shape)}")
    
    def extract_lsb(self, bit_plane: int = 0, channel: str = 'all') -> Image.Image:
        """
        Extract LSB (Least Significant Bit) from image
        bit_plane: 0 = least significant, 7 = most
        channel: 'r', 'g', 'b', 'all'
        """
        if len(self.img_array.shape) == 3:
            if channel == 'r':
                data = self.img_array[:,:,0]
            elif channel == 'g':
                data = self.img_array[:,:,1]
            elif channel == 'b':
                data = self.img_array[:,:,2]
            else:  # all
                # Process all channels
                result = np.zeros_like(self.img_array)
                for c in range(3):
                    lsb = (self.img_array[:,:,c] >> bit_plane) & 1
                    result[:,:,c] = lsb * 255
                return Image.fromarray(result.astype(np.uint8))
        else:
            data = self.img_array
        
        # Extract bit plane
        lsb = (data >> bit_plane) & 1
        result = (lsb * 255).astype(np.uint8)
        
        return Image.fromarray(result)
    
    def extract_bit_planes(self, output_dir: str):
        """Extract all 8 bit planes from all channels"""
        os.makedirs(output_dir, exist_ok=True)
        
        channels = ['r', 'g', 'b'] if len(self.img_array.shape) == 3 else ['gray']
        
        for ch in channels:
            for bit in range(8):
                try:
                    result = self.extract_lsb(bit, ch)
                    if ch == 'gray':
                        fn = f"{output_dir}/bitplane_{bit}.png"
                    else:
                        fn = f"{output_dir}/bitplane_{ch}_{bit}.png"
                    result.save(fn)
                    print(f"Saved: {fn}")
                except Exception as e:
                    print(f"Error bit {bit} {ch}: {e}")
    
    def analyze_row(self, row: int) -> dict:
        """Analyze specific row (row 310 is special per hints)"""
        if row >= self.height:
            return None
        
        row_data = self.img_array[row,:]
        
        analysis = {
            'row': row,
            'mean': np.mean(row_data),
            'std': np.std(row_data),
            'min': np.min(row_data),
            'max': np.max(row_data),
            'unique_count': len(np.unique(row_data))
        }
        
        # Check for patterns
        if len(row_data.shape) == 2:
            # Check LSB patterns
            lsb_pattern = (row_data >> 0) & 1
            analysis['lsb_mean'] = np.mean(lsb_pattern)
        
        return analysis
    
    def extract_row_lsb(self, row: int) -> bytes:
        """Extract LSB data from a specific row as bytes"""
        if row >= self.height:
            return b''
        
        row_data = self.img_array[row,:]
        
        # Get LSBs
        if len(row_data.shape) == 2:
            # RGB - extract from all channels
            bits = []
            for c in range(3):
                channel_bits = (row_data[:,c] >> 0) & 1
                bits.extend(channel_bits)
            
            # Convert bits to bytes
            bit_array = np.array(bits)
            byte_data = []
            for i in range(0, len(bit_array), 8):
                byte_bits = bit_array[i:i+8]
                if len(byte_bits) == 8:
                    byte_val = int(''.join(map(str, byte_bits)), 2)
                    byte_data.append(byte_val)
            
            return bytes(byte_data)
        else:
            # Grayscale
            bits = (row_data >> 0) & 1
            byte_data = []
            for i in range(0, len(bits), 8):
                byte_bits = bits[i:i+8]
                if len(byte_bits) == 8:
                    byte_val = int(''.join(map(str, byte_bits)), 2)
                    byte_data.append(byte_val)
            return bytes(byte_data)
    
    def scan_for_qr_patterns(self) -> list:
        """Scan image for potential QR code patterns"""
        # QR codes have specific patterns: finder patterns at corners
        # This is a basic scanner
        
        findings = []
        
        # Look for square-like structures
        # Simplified: look for regions with high contrast
        if len(self.img_array.shape) == 3:
            gray = np.mean(self.img_array, axis=2).astype(np.uint8)
        else:
            gray = self.img_array
        
        # Edge detection via simple gradient
        grad_x = np.abs(np.diff(gray, axis=1))
        grad_y = np.abs(np.diff(gray, axis=0))
        
        # Regions with high edge density might be QR-like
        findings.append({
            'edge_density_x': np.mean(grad_x),
            'edge_density_y': np.mean(grad_y)
        })
        
        return findings
    
    def save_cropped(self, x: int, y: int, w: int, h: int, output: str):
        """Save cropped region"""
        cropped = self.img.crop((x, y, x+w, y+h))
        cropped.save(output)
        print(f"Cropped saved: {output}")
    
    def get_pixel_info(self, x: int, y: int) -> dict:
        """Get detailed pixel information"""
        if x >= self.width or y >= self.height:
            return None
        
        pixel = self.img_array[y, x]
        
        info = {
            'x': x,
            'y': y,
            'raw': pixel.tolist() if hasattr(pixel, 'tolist') else pixel,
            'lsb': [int(v) & 1 for v in pixel] if len(self.img_array.shape) == 3 else int(pixel) & 1
        }
        
        return info

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='310 BTC Challenge Steganography Tools')
    parser.add_argument('image', help='Image file to analyze')
    parser.add_argument('--lsb', action='store_true', help='Extract LSB from all bit planes')
    parser.add_argument('--row', type=int, help='Analyze specific row')
    parser.add_argument('--crop', help='Crop region (x,y,w,h)')
    parser.add_argument('--output', default='output', help='Output directory')
    
    args = parser.parse_args()
    
    analyzer = StegAnalyzer(args.image)
    
    if args.lsb:
        print("Extracting all bit planes...")
        analyzer.extract_bit_planes(args.output)
    
    if args.row is not None:
        print(f"\nAnalyzing row {args.row}:")
        analysis = analyzer.analyze_row(args.row)
        if analysis:
            for k, v in analysis.items():
                print(f"  {k}: {v}")
        
        # Extract LSB data from row
        print(f"\nExtracting LSB data from row {args.row}...")
        data = analyzer.extract_row_lsb(args.row)
        if data:
            print(f"Extracted {len(data)} bytes")
            # Look for printable ASCII
            printable = bytes([b for b in data if 32 <= b < 127])
            if printable:
                print(f"Printable: {printable[:100]}")
    
    if args.crop:
        x, y, w, h = map(int, args.crop.split(','))
        analyzer.save_cropped(x, y, w, h, f"{args.output}/crop_{x}_{y}.png")

if __name__ == "__main__":
    main()