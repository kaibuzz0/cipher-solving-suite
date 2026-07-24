#!/usr/bin/env python3
"""
Steganography Analyzer
Extract hidden data from images
"""

from PIL import Image
import numpy as np

print("""
╔══════════════════════════════════════════════════════════╗
║        🖼️ STEGANOGRAPHY ANALYZER 🖼️                     ║
║     Find hidden messages in images                       ║
╚══════════════════════════════════════════════════════════╝

This tool analyzes images for hidden data using:
- Least Significant Bit (LSB) extraction
- Color channel analysis
- Metadata inspection
""")

def extract_lsb(image_path):
    """Extract LSB data from image"""
    try:
        img = Image.open(image_path)
        pixels = np.array(img)
        
        # Extract LSB from each channel
        height, width, channels = pixels.shape
        
        binary_data = []
        for h in range(height):
            for w in range(width):
                for c in range(channels):
                    binary_data.append(str(pixels[h, w, c] & 1))
        
        # Convert to bytes
        binary_string = ''.join(binary_data)
        
        # Try different offsets
        for offset in range(8):
            message = []
            for i in range(offset, len(binary_string) - 7, 8):
                byte = binary_string[i:i+8]
                char = chr(int(byte, 2))
                if 32 <= ord(char) <= 126:  # Printable ASCII
                    message.append(char)
                else:
                    break
            
            result = ''.join(message)
            if len(result) > 10:  # Meaningful message
                print(f"\nOffset {offset}: {result[:100]}...")
    
    except Exception as e:
        print(f"Error: {e}")

def analyze_image(image_path):
    """General image analysis"""
    try:
        img = Image.open(image_path)
        print(f"\nImage: {image_path}")
        print(f"Size: {img.size}")
        print(f"Mode: {img.mode}")
        print(f"Format: {img.format}")
        
        # Check for common stego indicators
        if img.mode == 'RGBA':
            print("\n⚠️ Alpha channel present - could hide data")
        
        # Analyze file size vs image size
        import os
        file_size = os.path.getsize(image_path)
        expected_size = img.size[0] * img.size[1] * len(img.mode)
        if file_size > expected_size * 1.5:
            print("⚠️ File size larger than expected - possible embedded data")
        
    except Exception as e:
        print(f"Error analyzing image: {e}")

def main():
    print("\nEnter image path to analyze:")
    image_path = input("Path: ").strip()
    
    if not image_path:
        # Demo with sample
        print("\nDemo mode - would analyze: puzzles/level-3-hard/hidden_message.png")
        return
    
    analyze_image(image_path)
    
    print("\nExtract LSB data? (y/n)")
    if input().lower() == 'y':
        extract_lsb(image_path)

if __name__ == "__main__":
    main()
