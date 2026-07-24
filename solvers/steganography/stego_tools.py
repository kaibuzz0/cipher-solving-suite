#!/usr/bin/env python3
"""
Steganography Tools - Critical Tool
Extract hidden data from images, audio, files
"""

import os
import sys
from PIL import Image
import binascii

class SteganographyTools:
    """Comprehensive steganography analysis suite"""
    
    def __init__(self):
        pass
    
    def extract_lsb(self, image_path, bit_plane=0):
        """Extract LSB (Least Significant Bit) data"""
        try:
            img = Image.open(image_path)
            pixels = img.load()
            width, height = img.size
            
            binary_data = ""
            
            for y in range(height):
                for x in range(width):
                    pixel = pixels[x, y]
                    
                    # Handle RGB and RGBA
                    if len(pixel) >= 3:
                        r, g, b = pixel[0], pixel[1], pixel[2]
                        
                        # Extract LSB from each channel
                        binary_data += str((r >> bit_plane) & 1)
                        binary_data += str((g >> bit_plane) & 1)
                        binary_data += str((b >> bit_plane) & 1)
            
            # Convert binary to bytes
            message = ""
            for i in range(0, len(binary_data), 8):
                byte = binary_data[i:i+8]
                if len(byte) == 8:
                    char = chr(int(byte, 2))
                    if char.isprintable() or char in ['\n', '\t']:
                        message += char
                    else:
                        message += "?"
            
            return message
            
        except Exception as e:
            return f"Error: {str(e)}"
    
    def extract_all_bitplanes(self, image_path):
        """Extract all bitplanes from image"""
        try:
            img = Image.open(image_path)
            results = {}
            
            for bit in range(8):
                result = self.extract_lsb(image_path, bit)
                results[f'bit_{bit}'] = result[:200] + "..." if len(result) > 200 else result
            
            return results
            
        except Exception as e:
            return {"error": str(e)}
    
    def extract_metadata(self, image_path):
        """Extract image metadata (EXIF)"""
        try:
            img = Image.open(image_path)
            metadata = {
                'format': img.format,
                'mode': img.mode,
                'size': img.size,
                'info': dict(img.info)
            }
            
            # Try to get EXIF
            if hasattr(img, '_getexif') and img._getexif():
                exif = img._getexif()
                metadata['exif'] = {str(k): str(v) for k, v in exif.items()}
            
            return metadata
            
        except Exception as e:
            return {"error": str(e)}
    
    def analyze_file_structure(self, file_path):
        """Analyze file structure for hidden data"""
        try:
            with open(file_path, 'rb') as f:
                content = f.read()
            
            analysis = {
                'file_size': len(content),
                'file_header': content[:20].hex(),
                'file_trailer': content[-20:].hex() if len(content) > 20 else content.hex(),
                'entropy': self._calculate_entropy(content)
            }
            
            # Look for embedded files
            signatures = {
                'png': b'\x89PNG',
                'jpg': b'\xff\xd8\xff',
                'gif': b'GIF89a',
                'zip': b'PK\x03\x04',
                'pdf': b'%PDF',
                'hidden_text': b'This is'
            }
            
            for name, sig in signatures.items():
                if sig in content:
                    analysis[f'contains_{name}'] = True
            
            return analysis
            
        except Exception as e:
            return {"error": str(e)}
    
    def _calculate_entropy(self, data):
        """Calculate Shannon entropy"""
        from collections import Counter
        import math
        
        if not data:
            return 0
        
        counts = Counter(data)
        length = len(data)
        entropy = -sum(count * math.log2(count) for count in counts.values()) / length
        
        return entropy
    
    def full_analysis(self, file_path):
        """Run complete steganography analysis"""
        print(f"[*] Analyzing: {file_path}")
        print()
        
        # Check if image
        if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            print("[+] Image detected - running image analysis...")
            
            # Metadata
            print("\n[+] Extracting metadata...")
            metadata = self.extract_metadata(file_path)
            print(f"    Format: {metadata.get('format', 'Unknown')}")
            print(f"    Size: {metadata.get('size', 'Unknown')}")
            
            # Bitplanes
            print("\n[+] Extracting bitplanes...")
            bitplanes = self.extract_all_bitplanes(file_path)
            for bit, data in bitplanes.items():
                if 'error' not in bitplanes:
                    print(f"    {bit}: {data[:100]}...")
        
        # File structure analysis
        print("\n[+] Analyzing file structure...")
        structure = self.analyze_file_structure(file_path)
        print(f"    File size: {structure.get('file_size', 'Unknown')} bytes")
        print(f"    Entropy: {structure.get('entropy', 'Unknown'):.2f}")

def main():
    stego = SteganographyTools()
    
    print("="*70)
    print("🖼️  STEGANOGRAPHY TOOLS - PRODUCTION")
    print("="*70)
    print()
    
    print("Tools available:")
    print("  • extract_lsb() - Extract LSB data")
    print("  • extract_metadata() - Get EXIF data")
    print("  • analyze_file_structure() - Deep file analysis")
    print("  • full_analysis() - Complete stego analysis")
    print()
    
    print("Usage:")
    print("  from solvers.steganography.stego_tools import SteganographyTools")
    print("  stego = SteganographyTools()")
    print("  stego.full_analysis('image.png')")

if __name__ == "__main__":
    main()
