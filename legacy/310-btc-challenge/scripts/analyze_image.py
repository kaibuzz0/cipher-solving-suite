#!/usr/bin/env python3
"""
Image Analysis for 310_challenge.png
"""

from PIL import Image
import numpy as np
import os

print("="*70)
print("🖼️ IMAGE ANALYSIS")
print("="*70)

def analyze():
    if not os.path.exists("310_challenge.png"):
        print("❌ 310_challenge.png not found!")
        return
    
    img = Image.open("310_challenge.png")
    pixels = np.array(img)
    
    print(f"\nSize: {img.size}")
    print(f"Mode: {img.mode}")
    print(f"Shape: {pixels.shape}")
    
    if pixels.shape[0] > 310:
        print(f"\n✓ Row 310 exists!")
        row = pixels[310, :, :]
        print(f"  Unique values: {len(np.unique(row))}")

if __name__ == "__main__":
    analyze()
