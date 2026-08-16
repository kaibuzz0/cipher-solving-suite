#!/usr/bin/env python3
"""
310 BTC Challenge - Additional Analysis Tools
QR code scanning, color analysis, and pattern detection
"""

from PIL import Image, ImageStat
import numpy as np
import sys
import os
import re

class BTC310Analyzer:
    """Extended analysis for 310 BTC specific patterns"""
    
    def __init__(self, image_path: str):
        self.img = Image.open(image_path)
        self.arr = np.array(self.img)
        print(f"Loaded: {self.img.size}")
        
        # Known hints from the challenge
        self.known_chars = "L3CEO275KOD899D4FA1F64"
        self.hex_grid = [
            "511", "B20", "332", "328", "410", "530",
            "22B", "0FE", "52E", "D0F", "7A1", "65B",
            "52C", "7E7", "511", "2F6", "56F", "C4B"
        ]
    
    def extract_all_channels(self):
        """Separate and save R, G, B channels"""
        if len(self.arr.shape) != 3:
            print("Not RGB image")
            return
        
        r = self.arr[:,:,0]
        g = self.arr[:,:,1]  
        b = self.arr[:,:,2]
        
        Image.fromarray(r).save('channel_r.png')
        Image.fromarray(g).save('channel_g.png')
        Image.fromarray(b).save('channel_b.png')
        print("Channels extracted: channel_r.png, channel_g.png, channel_b.png")
    
    def analyze_color_distribution(self):
        """Analyze color statistics"""
        stat = ImageStat.Stat(self.img)
        print("\nColor Statistics:")
        print(f"  Mean: R={stat.mean[0]:.1f}, G={stat.mean[1]:.1f}, B={stat.mean[2]:.1f}")
        print(f"  RMS: R={stat.rms[0]:.1f}, G={stat.rms[1]:.1f}, B={stat.rms[2]:.1f}")
        print(f"  Extrema: {stat.extrema}")
    
    def scan_for_text_patterns(self):
        """Scan for ASCII text in image data"""
        # Flatten and look for printable ASCII
        if len(self.arr.shape) == 3:
            flat = self.arr.flatten()
        else:
            flat = self.arr.flatten()
        
        # Look for strings of printable chars
        text_found = []
        current = ""
        
        for val in flat:
            if 32 <= val <= 126:
                current += chr(val)
                if len(current) > 50:  # Save long strings
                    text_found.append(current)
                    current = ""
            else:
                if len(current) >= 4:
                    text_found.append(current)
                current = ""
        
        # Deduplicate and show unique
        unique = list(set([t for t in text_found if len(t) >= 4]))
        print(f"\nFound {len(unique)} unique text patterns")
        for t in unique[:20]:  # Show first 20
            print(f"  '{t}'")
        
        return unique
    
    def check_known_patterns(self):
        """Check for known hint patterns"""
        print("\nKnown Pattern Analysis:")
        print(f"  Challenge chars: {self.known_chars}")
        print(f"  Hex grid: {self.hex_grid}")
        
        # Look for these in image
        flat = self.arr.flatten()
        
        # Check if hex values appear
        hex_values_found = []
        for hex_val in self.hex_grid:
            # Convert hex to int
            try:
                dec = int(hex_val, 16)
                if dec in flat:
                    hex_values_found.append(hex_val)
            except:
                pass
        
        print(f"  Hex values found in image data: {len(hex_values_found)}")
    
    def create_difference_image(self, other_image_path: str = None):
        """Create difference image or auto-difference"""
        # For now, create a high-pass filter (difference from local mean)
        if len(self.arr.shape) == 3:
            # Use green channel
            data = self.arr[:,:,1].astype(float)
        else:
            data = self.arr.astype(float)
        
        # Local difference (edge enhancement)
        diff = np.abs(data[:-1, :-1] - data[1:, 1:])
        diff = (diff / diff.max() * 255).astype(np.uint8)
        
        Image.fromarray(diff).save('difference.png')
        print("Difference/edge image saved: difference.png")
    
    def extract_region(self, x1, y1, x2, y2, name="region"):
        """Extract and save a region"""
        region = self.img.crop((x1, y1, x2, y2))
        region.save(f'{name}_{x1}_{y1}.png')
        print(f"Region saved: {name}_{x1}_{y1}.png")
    
    def scan_for_hidden_data(self):
        """Comprehensive scan for hidden data"""
        results = {
            'text_patterns': [],
            'suspicious_pixels': [],
            'lsb_data': {}
        }
        
        print("\n=== Comprehensive Scan ===")
        
        # 1. Text scan
        results['text_patterns'] = self.scan_for_text_patterns()
        
        # 2. LSB analysis per channel
        if len(self.arr.shape) == 3:
            for i, name in enumerate(['R', 'G', 'B']):
                channel = self.arr[:,:,i]
                lsb = (channel & 1).flatten()
                
                # Check if LSB has structure
                ones_ratio = np.mean(lsb)
                results['lsb_data'][name] = {
                    'ones_ratio': ones_ratio,
                    'suspicious': abs(ones_ratio - 0.5) > 0.1  # Should be ~0.5 for random
                }
                print(f"  LSB {name}: {ones_ratio:.3f} ones ratio")
        
        return results

def quick_analyze(image_path):
    """Quick analysis of the 310 BTC image"""
    print(f"\n{'='*60}")
    print(f"310 BTC Challenge Analysis")
    print(f"{'='*60}")
    
    analyzer = BTC310Analyzer(image_path)
    analyzer.analyze_color_distribution()
    analyzer.check_known_patterns()
    analyzer.scan_for_hidden_data()
    
    # Extract channels
    analyzer.extract_all_channels()
    analyzer.create_difference_image()
    
    print(f"\n{'='*60}")
    print("Analysis complete. Check output files.")
    print(f"{'='*60}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('image', help='Image file')
    parser.add_argument('--quick', action='store_true', help='Quick full analysis')
    args = parser.parse_args()
    
    if args.quick:
        quick_analyze(args.image)
    else:
        analyzer = BTC310Analyzer(args.image)
        analyzer.analyze_color_distribution()