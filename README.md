# 🔐 310 BTC Challenge - Real Puzzle Solver

[![Bitcoin](https://img.shields.io/badge/Bitcoin-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white)]()
[![Prize](https://img.shields.io/badge/Prize-310%20BTC-success)]()
[![Status](https://img.shields.io/badge/Status-SOLVED%20%26%20STUDYING-informational)]()

**Tools and research for solving the famous 310 BTC puzzle created by Alister Milne.**

> *"The puzzle that captivated the crypto world. 310 BTC hidden in plain sight."*

---

## 🎯 About This Repository

This repository contains our work on the legendary **310 BTC Puzzle** (2019-2020), created by [@AlisterMilne](https://twitter.com/AlisterMilne). While the main prize has been claimed, this repo serves as:

- ✅ **Educational resource** - Learn from real puzzle-solving techniques
- 🔧 **Tool collection** - Steganography, cryptography, analysis tools
- 📚 **Research archive** - Documenting what worked and what didn't
- 🧠 **Training ground** - Practice for future puzzles
- 🗂️ **Case study** - Understanding multi-layer cryptographic challenges

---

## 🏆 The Original Challenge

**Creator:** Alister Milne (@AlisterMilne)  
**Prize:** 310 BTC (~$3,000,000 at the time)  
**Status:** ✅ **SOLVED** (2020)  
**Difficulty:** 🌶️🌶️🌶️🌶️🌶️ (Legendary)  
**Time to Solve:** ~1 year by community

### How It Worked

The puzzle consisted of:
1. **Image file** (310_challenge.png) containing hidden data
2. **Multi-stage unlocking** - Required solving multiple layers
3. **Steganography** - Data hidden in image bitplanes
4. **Cryptography** - Encrypted keys requiring mathematical solutions
5. **Social element** - Community collaboration essential

**Final Solution:** A wallet containing 310 BTC was unlocked through combined efforts of the crypto community.

---

## 📁 Repository Structure

```
310-btc-challenge/
│
├── 📄 README.md                    # This file
├── 📄 310_challenge.png           # The original puzzle image
├── 📄 solution.txt                # Solution documentation
│
├── 🔍 ANALYSIS TOOLS/              # Deep inspection tools
│   ├── analyze_310.py             # Main analysis script
│   ├── alpha_extract.py           # Alpha channel extraction
│   ├── char_locator.py            # Character pattern finder
│   ├── scan_bitplanes.py          # Bitplane scanner
│   ├── visual_analyze.py          # Visual analysis
│   ├── steg_tools.py              # Steganography toolkit
│   └── original_analysis.ipynb    # Jupyter notebook analysis
│
├── 🖼️ BITPLANES/                   # Extracted bitplane images
│   └── bitplanes/                 # 24 bitplanes (R,G,B × 8)
│       ├── bitplane_r_0.png      # Red channel bit 0
│       ├── bitplane_r_1.png      # Red channel bit 1
│       └── ... (all 24 bitplanes)
│
├── 💪 BRUTE FORCE TOOLS/           # Computational attacks
│   ├── brute_force.py             # Basic brute force
│   ├── comprehensive_brute.py       # Comprehensive search
│   ├── smart_brute.py             # Intelligent brute force
│   ├── permute_brute.py           # Permutation attacks
│   └── final_attempt.py           # Final solution attempts
│
├── 🎮 PUZZLE LEVELS/               # Educational puzzles
│   ├── level-1-easy/              # Welcome puzzle (0.01 BTC)
│   │   └── welcome_puzzle.py
│   └── level-2-medium/            # Cipher challenge (0.1 BTC)
│       └── cipher_puzzle.py
│
├── 🛠️ SOLVER TOOLS/               # Cryptographic tools
│   ├── solvers/
│   │   ├── rsa_factorizer.py      # RSA factorization
│   │   └── steganalyzer.py          # LSB extraction
│   └── generators/
│       └── wallet_generator.py      # Test wallet generator
│
├── 📊 EXTRACTED DATA/              # Analysis results
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
└── 📚 DOCUMENTATION/
    └── docs/theory/
        └── cryptography-101.md      # Learning resource
```

---

## 🚀 Quick Start

### 1. Clone and Explore

```bash
git clone https://github.com/kaibuzz0/310-btc-challenge.git
cd 310-btc-challenge
```

### 2. Run the Welcome Puzzle

```bash
cd puzzles/level-1-easy
python welcome_puzzle.py
```

**Your first clue:**
```
S2V5IDogYjUzMzltbmhLL1VURVhtcG9rZXJjaGFsbGVuZ2U=
```

### 3. Analyze the Original Image

```bash
python analyze_310.py
python scan_bitplanes.py
python steg_tools.py
```

---

## 🛠️ Tools Included

### Steganography Analysis

**scan_bitplanes.py**
- Extracts all 24 bitplanes (RGB × 8)
- Saves as individual images
- Helps find hidden visual data

**steg_tools.py**
- LSB (Least Significant Bit) extraction
- Alpha channel analysis
- Pattern detection

**alpha_extract.py**
- Specialized alpha channel extraction
- Extracts 2-bit, LSB, and pattern data
- Focuses on row 310 (hint hint)

### Cryptographic Solvers

**rsa_factorizer.py**
- Fermat's factorization method
- Pollard's Rho algorithm
- Trial division
- Educational RSA cracking

**cipher_solver.py** (via steganalyzer.py)
- Caesar cipher brute force
- ROT13
- Atbash
- Frequency analysis

### Brute Force Tools

**smart_brute.py**
- Intelligent brute force with patterns
- Dictionary attacks
- Rule-based generation

**comprehensive_brute.py**
- Exhaustive search
- Multi-threaded
- Progress tracking

---

## 🔍 What We Found

### Key Discoveries

1. **Bitplane 0** contained visual artifacts
2. **Alpha channel** had hidden data patterns
3. **Row 310** was significant (filename clue)
4. **LSB** contained encoded information
5. **Multiple layers** required sequential solving

### Analysis Results

Check these files for findings:
- `bitplanes/` - All extracted bitplanes
- `alpha_*.bin` - Alpha channel data
- `solution.txt` - Solution documentation
- `character_region_*.png` - Extracted characters

---

## 🎓 Learning Resources

### For Beginners

**Start here:**
1. Read `docs/theory/cryptography-101.md`
2. Try Level 1 puzzle (`welcome_puzzle.py`)
3. Try Level 2 puzzle (`cipher_puzzle.py`)
4. Study the analysis scripts
5. Review `solution.txt`

**Key Concepts:**
- Steganography (hiding data in images)
- Bitplanes (individual bits of color channels)
- LSB (Least Significant Bit) encoding
- RSA cryptography
- Pattern recognition

### For Advanced Users

**Study the analysis:**
- `analyze_310.py` - Comprehensive image analysis
- `original_analysis.ipynb` - Jupyter notebook with visualizations
- Bitplane extraction methodology
- Brute force optimization techniques

---

## 📊 Puzzle Difficulty Levels

### Level 1: The Welcome (Easy) - 0.01 BTC
**Concept:** Base64 encoding  
**Skills:** Basic encoding/decoding  
**Time:** 5-30 minutes  
**Tool:** Manual or Python

### Level 2: The Cipher (Medium) - 0.1 BTC
**Concept:** ROT13 cipher  
**Skills:** Classical cryptography  
**Time:** 30-60 minutes  
**Tool:** cipher_solver.py

### Level 3: The Vault (Hard) - 1 BTC
**Concept:** RSA factorization  
**Skills:** Mathematical computation  
**Time:** Hours to days  
**Tool:** rsa_factorizer.py

### Original 310 BTC Puzzle (Legendary)
**Concept:** Multi-layer steganography + cryptography  
**Skills:** Advanced analysis, pattern recognition, mathematics  
**Time:** 1+ year (community effort)  
**Tool:** Combination of all tools

---

## 🤝 Collaboration

This puzzle was solved through community collaboration. Key contributors:
- Multiple analysts working together
- Tool sharing
- Finding sharing (not solutions)
- Pattern recognition

**Lessons learned:**
- Teamwork > individual genius
- Diverse skills essential
- Persistence pays off
- Documentation crucial

---

## ⚠️ Important Notes

### Educational Purpose
- ✅ Learn from real puzzle techniques
- ✅ Practice steganography analysis
- ✅ Understand cryptographic methods
- ✅ Build solving tools

### Ethics
- ⚠️ Original puzzle is SOLVED
- ⚠️ Prizes have been claimed
- ✅ This is for EDUCATION
- ✅ Share knowledge
- ✅ Respect puzzle creators

### Security
- Use test wallets only
- Never use real funds for experiments
- Verify all tools before running
- Keep private keys secure

---

## 🔗 Related Resources

### Original Sources
- **Creator:** [@AlisterMilne](https://twitter.com/AlisterMilne)
- **Tweet:** Original announcement (archived)
- **Solution:** Community write-ups

### Our Other Projects
- **[hive-develoment](https://github.com/kaibuzz0/hive-develoment)** - Unified OS
- **[crypto-puzzle-solver](https://github.com/kaibuzz0/crypto-puzzle-solver)** - Active puzzle research
- **[termux-pc-hermes-sync-files-](https://github.com/kaibuzz0/termux-pc-hermes-sync-files-)** - Cross-platform tools

### Learning Resources
- [Cryptopals](https://cryptopals.com/) - Crypto challenges
- [OverTheWire](https://overthewire.org/) - Security games
- [StegSolve](https://github.com/zardus/ctf-tools/tree/master/stegsolve) - Steganography tool

---

## 📈 Success Metrics

| Metric | Status |
|--------|--------|
| Original Puzzle | ✅ Solved (by community) |
| Tools Built | 15+ analysis scripts |
| Knowledge Gained | Expert-level steganography |
| Educational Value | ⭐⭐⭐⭐⭐ |
| Fun Factor | ⭐⭐⭐⭐⭐ |

---

## 🎯 Future Work

- [ ] Create interactive tutorial
- [ ] Add more educational puzzles
- [ ] Build automated steganography detector
- [ ] Document advanced techniques
- [ ] Share case study presentation

---

## 🏆 Acknowledgments

**Thanks to:**
- Alister Milne for creating this legendary puzzle
- The crypto community for solving it
- All contributors to steganography tools
- Open source cryptography libraries

**Special thanks to everyone who attempted this puzzle!**

---

```
The puzzle may be solved, but the knowledge remains.
Study the techniques, learn the methods,
Apply them to future challenges.

Not all treasure is silver and gold,
Some is the wisdom gained along the road.
```

**Author:** kaibuzz0  
**Created:** 2026-07-24  
**Purpose:** Educational preservation  
**License:** MIT (for educational use)

---

**Ready to learn from the best? Start with `welcome_puzzle.py`! 🚀**
