#!/usr/bin/env python3
"""
310 BTC Challenge - Visual Analysis
Extract character positions from image to find password
"""

from PIL import Image
import numpy as np

class VisualAnalyzer:
    """Analyze image visually for character patterns"""
    
    def __init__(self, image_path):
        self.img = Image.open(image_path)
        self.arr = np.array(self.img)
        self.height, self.width = self.arr.shape[:2]
        print(f"Image: {self.width}x{self.height}")
    
    def analyze_character_regions(self):
        """Find regions with high contrast (likely characters)"""
        # Convert to grayscale
        if len(self.arr.shape) == 3:
            gray = np.mean(self.arr[:,:,:3], axis=2).astype(np.uint8)
        else:
            gray = self.arr
        
        # Look for areas with text-like patterns
        # Text has alternating high/low values
        diff_h = np.abs(np.diff(gray, axis=1))
        diff_v = np.abs(np.diff(gray, axis=0))
        
        # Find rows with lots of edges
        row_edges = np.sum(diff_h > 50, axis=1)
        text_rows = np.where(row_edges > np.mean(row_edges) * 3)[0]
        
        print(f"\nPotential text rows: {len(text_rows)}")
        print(f"Row ranges: {text_rows[:20]}")
        
        return text_rows
    
    def extract_row_detail(self, row_num):
        """Extract detailed view of a row"""
        if row_num >= self.height:
            return
        
        row = self.arr[row_num, :, :3]
        gray = np.mean(row, axis=1).astype(np.uint8)
        
        # Find columns with edges (character boundaries)
        edges = np.where(np.abs(np.diff(gray)) > 50)[0]
        
        print(f"\nRow {row_num}:")
        print(f"  Edge positions: {edges[:20]}")
        print(f"  Gray values: {gray[:50]}")
        
        # Look for repeating patterns
        return edges
    
    def find_grid_regions(self):
        """Find the hex grid in the image"""
        # Grid would have regular spacing
        # Look for regions with regular patterns
        
        gray = np.mean(self.arr[:,:,:3], axis=2).astype(np.uint8)
        
        # Check each row for regular patterns
        regular_rows = []
        for row in range(self.height):
            r = gray[row, :]
            # Look for repeating patterns
            edges = np.where(np.abs(np.diff(r)) > 30)[0]
            if len(edges) > 10 and len(edges) < 100:
                # Calculate spacing
                if len(edges) > 1:
                    spacing = np.diff(edges)
                    if np.std(spacing) < np.mean(spacing) * 0.5:
                        regular_rows.append((row, len(edges), np.mean(spacing)))
        
        print(f"\nRegular pattern rows: {len(regular_rows)}")
        for r in regular_rows[:10]:
            print(f"  Row {r[0]}: {r[1]} edges, spacing {r[2]:.1f}")
        
        return regular_rows
    
    def extract_suspect_regions(self):
        """Save regions that look like they contain text"""
        # Focus on middle area where characters might be
        mid_y = self.height // 2
        mid_x = self.width // 2
        
        regions = [
            (mid_y-100, mid_y+100, mid_x-200, mid_x+200, "center"),
            (300, 400, 0, self.width, "upper_middle"),
            (self.height-400, self.height-300, 0, self.width, "lower_middle"),
        ]
        
        for y1, y2, x1, x2, name in regions:
            if y1 >= 0 and y2 < self.height and x1 >= 0 and x2 < self.width:
                region = self.arr[y1:y2, x1:x2]
                img = Image.fromarray(region.astype(np.uint8))
                img.save(f'region_{name}.png')
                print(f"Saved region_{name}.png")

def main():
    analyzer = VisualAnalyzer('/root/310_btc_challenge/310_challenge.png')
    
    print("=" * 60)
    print("VISUAL ANALYSIS")
    print("=" * 60)
    
    # Find text-like regions
    text_rows = analyzer.analyze_character_regions()
    
    # Examine row 310 specifically
    analyzer.extract_row_detail(310)
    
    # Find grid patterns
    analyzer.find_grid_regions()
    
    # Extract suspect regions
    analyzer.extract_suspect_regions()
    
    print("\n" + "=" * 60)
    print("Manual inspection needed:")
    print("Check region_*.png files for character positions")
    print("=" * 60)

if __name__ == "__main__":
    main()