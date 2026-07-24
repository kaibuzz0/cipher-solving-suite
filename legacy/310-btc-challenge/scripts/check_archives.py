#!/usr/bin/env python3
"""
Archive Recovery Tool
Check if bitcoinchallenge.codes is archived
"""

import urllib.request
import ssl

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

print("="*70)
print("🌐 CHECKING ARCHIVE.ORG FOR BITCOINCHALLENGE.CODES")
print("="*70)

print("\nManual check URLs:")
print("  https://web.archive.org/web/*/https://bitcoinchallenge.codes")
print("  https://webcache.googleusercontent.com/search?q=bitcoinchallenge.codes")
print("\nTry these to see when site was last alive")
print("="*70)
