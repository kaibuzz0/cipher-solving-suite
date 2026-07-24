# 🔐 310 BTC Challenge

[![Bitcoin](https://img.shields.io/badge/Bitcoin-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)]()
[![Status](https://img.shields.io/badge/Status-EDUCATIONAL-informational)]()

**Tools and research for cryptographic puzzle solving.**

---

## 🎯 Active Puzzles with Real Rewards

| Puzzle | Prize | Status | Difficulty | Link |
|--------|-------|--------|------------|------|
| **Satoshi Treasure** | $1M+ BTC | 🟢 Active | ⭐⭐⭐⭐ | [satoshistreasure.xyz](https://satoshistreasure.xyz) |
| **Piękna Banana** | 1 BTC | 🟡 Unclear | ⭐⭐⭐⭐ | [pienkbanana.com](https://pienkbanana.com) |
| **Bitcoin Brainwallets** | Variable | 🟢 Ongoing | ⭐⭐⭐ | Various |
| **Ethereum Contracts** | ETH/NFTs | 🟢 Constant | ⭐⭐⭐ | Etherscan |
| **The 310 BTC** | 310 BTC | 🔴 Solved | ⭐⭐⭐⭐⭐ | Educational |

---

## 📁 Repository Structure

```
310-btc-challenge/
├── README.md                    # This file
├── 310_challenge.png           # The original puzzle image
├── solution.txt                # Solution documentation
│
├── ANALYSIS TOOLS/              # Deep inspection tools
│   ├── analyze_310.py             # Main analysis script
│   ├── alpha_extract.py           # Alpha channel extraction
│   ├── char_locator.py            # Character pattern finder
│   ├── scan_bitplanes.py          # Bitplane scanner
│   ├── visual_analyze.py          # Visual analysis
│   ├── steg_tools.py              # Steganography toolkit
│   └── original_analysis.ipynb    # Jupyter notebook analysis
│
├── BITPLANES/                   # Extracted bitplane images
│   └── bitplanes/                 # 24 bitplanes (R,G,B × 8)
│       ├── bitplane_r_0.png      # Red channel bit 0
│       ├── bitplane_r_1.png      # Red channel bit 1
│       └── ... (all 24 bitplanes)
│
├── BRUTE FORCE TOOLS/           # Computational attacks
│   ├── brute_force.py             # Basic brute force
│   ├── comprehensive_brute.py       # Comprehensive search
│   ├── smart_brute.py             # Intelligent brute force
│   ├── permute_brute.py           # Permutation attacks
│   └── final_attempt.py           # Final solution attempts
│
├── PUZZLE LEVELS/               # Educational puzzles
│   ├── level-1-easy/              # Welcome puzzle (0.01 BTC)
│   │   └── welcome_puzzle.py
│   └── level-2-medium/            # Cipher challenge (0.1 BTC)
│       └── cipher_puzzle.py
│
├── SOLVER TOOLS/               # Cryptographic tools
│   ├── solvers/
│   │   ├── rsa_factorizer.py      # RSA factorization
│   │   └── steganalyzer.py          # LSB extraction
│   └── generators/
│       └── wallet_generator.py      # Test wallet generator
│
├── EXTRACTED DATA/              # Analysis results
│   ├── alpha_2bit.bin             # Alpha channel data
│   ├── alpha_lsb.bin              # LSB data
│   ├── alpha_pattern.bin          # Pattern data
│   ├── alpha_row310.bin           # Row 310 specific
│   ├── channel_r.png              # Red channel
│   ├── channel_g.png              # Green channel
│   ├── channel_b.png              # Blue channel
│   ├── difference.png             # Difference analysis
│   ├── region_center.png          # Center region
│   ├── row_310_region.png         # Row 310 analysis
│   └── character_region_*.png     # Character extraction
│
└── DOCUMENTATION/
    └── docs/theory/
        └── cryptography-101.md      # Learning resource
```

---

## 🚀 Quick Start

```bash
# Educational levels
python PUZZLE_LEVELS/level-1-easy/welcome_puzzle.py
python PUZZLE_LEVELS/level-2-medium/cipher_puzzle.py

# Analysis tools
python ANALYSIS_TOOLS/analyze_310.py
python ANALYSIS_TOOLS/steg_tools.py

# Solvers
python SOLVER_TOOLS/solvers/rsa_factorizer.py
```

---

## 🎯 Recommended Focus

1. **Satoshi Treasure** - $1M+ still unclaimed
2. **Practice here** - Learn techniques
3. **Then solve** - Active puzzles for real rewards

---

**Author:** kaibuzz0  
**Last Updated:** 2026-07-24
