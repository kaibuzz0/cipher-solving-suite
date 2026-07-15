#!/usr/bin/env python3
"""
310 BTC Challenge - Character Position Analyzer
Identify where the visible characters appear in the image
"""

from PIL import Image
import numpy as np

class CharacterLocator:
    """Find character positions in the image"""
    
    def __init__(self, image_path: str):
        self.img = Image.open(image_path)
        self.arr = np.array(self.img)
        print(f"Image: {self.img.size}")
        
        # Characters visible in image (from hints)
        self.chars = "L3CEO275KOD899D4FA1F64"
        
    def find_character_regions(self):
        """
        Try to locate character-like structures
        Characters would be high contrast regions
        """
        if len(self.arr.shape) == 3:
            gray = np.mean(self.arr, axis=2).astype(np.uint8)
        else:
            gray = self.arr
        
        # Find high-contrast regions
        grad = np.abs(np.diff(gray, axis=1))
        edges = grad > 100
        
        # Find rows with many edges (likely text)
        edge_counts = np.sum(edges, axis=1)
        
        # Rows with above-average edge density
        avg_edges = np.mean(edge_counts)
        text_rows = np.where(edge_counts > avg_edges * 2)[0]
        
        print(f"\nRows with high edge density: {len(text_rows)}")
        print(f"Top 10: {text_rows[:10]}")
        
        # Group consecutive rows
        groups = []
        current = []
        for row in text_rows:
            if not current or row == current[-1] + 1:
                current.append(row)
            else:
                if len(current) > 5:  # At least 5 rows
                    groups.append(current)
                current = [row]
        if current and len(current) > 5:
            groups.append(current)
        
        print(f"\nFound {len(groups)} text-like regions:")
        for i, group in enumerate(groups[:10]):
            print(f"  Region {i}: rows {group[0]}-{group[-1]} ({len(group)} rows)")
        
        return groups
    
    def analyze_regions_for_characters(self, regions):
        """Analyze each region for the known characters"""
        
        for i, region in enumerate(regions[:5]):
            print(f"\n--- Region {i}: rows {region[0]}-{region[-1]} ---")
            
            # Extract this region
            sub_img = self.arr[region[0]:region[-1]+1, :, :3]
            
            # Simple analysis
            print(f"  Shape: {sub_img.shape}")
            print(f"  Mean color: {np.mean(sub_img, axis=(0,1))}")
            
            # Check for repeating patterns (might indicate characters)
            flat = sub_img.flatten()
            unique = len(np.unique(flat))
            print(f"  Unique pixel values: {unique}")
            
            if unique < 100:
                print(f"  Low entropy - possible text region")
    
    def extract_character_candidates(self):
        """
        Extract potential character images for manual review
        """
        # Focus on row 310 area (mentioned in hints)
        row_310_area = self.arr[300:320, :, :]
        
        img = Image.fromarray(row_310_area.astype(np.uint8))
        img.save('character_region_310.png')
        print("\nSaved character_region_310.png for manual inspection")
        
        # Also check nearby rows
        for offset in [-10, -5, 0, 5, 10]:
            row = 310 + offset
            if 0 <= row < self.arr.shape[0]:
                region = self.arr[row-5:row+6, :, :]
                img = Image.fromarray(region.astype(np.uint8))
                img.save(f'character_region_{row}.png')
                print(f"  Saved character_region_{row}.png")
    
    def create_hint_summary(self):
        """Summary of known hints"""
        print("\n" + "="*60)
        print("KNOWN HINTS FROM CHALLENGE")
        print("="*60)
        print(f"21 Characters: {self.chars}")
        print(f"Character count: {len(self.chars)}")
        print()
        print("Hex grid values:")
        hex_values = ["511", "B20", "332", "328", "410", "530", 
                      "22B", "0FE", "52E", "D0F", "7A1", "65B",
                      "52C", "7E7", "511", "2F6", "56F", "C4B"]
        for i in range(0, len(hex_values), 6):
            print(f"  {' '.join(hex_values[i:i+6])}")
        print()
        print("Row 310: Contains QR code (per hints)")
        print("Row 310: Only row with varying alpha (found)")
        print("Row 310: Contains encrypted data (found)")
        print()
        print("Password possibilities:")
        print("  - Characters in specific order")
        print("  - Hex grid concatenation")
        print("  - Combination of both")
        print("  - Character positions in image")

def main():
    locator = CharacterLocator('/root/310_btc_challenge/310_challenge.png')
    
    locator.create_hint_summary()
    regions = locator.find_character_regions()
    locator.analyze_regions_for_characters(regions)
    locator.extract_character_candidates()
    
    print("\n" + "="*60)
    print("Next: Review character_region_*.png files manually")
    print("Look for character order in the image")
    print("="*60)

if __name__ == "__main__":
    main()