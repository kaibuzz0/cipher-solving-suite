#!/bin/bash
# QUICK PUZZLE FINDER
# Opens all the best puzzle sources

echo "🔍 OPENING ETHEREUM PUZZLE SOURCES..."
echo ""

# Open Etherscan (main tool)
echo "Opening Etherscan Verified Contracts..."
start https://etherscan.io/contractsVerified 2>/dev/null || 
xdg-open https://etherscan.io/contractsVerified 2>/dev/null ||
echo "  → https://etherscan.io/contractsVerified"

sleep 2

# Open Reddit
echo ""
echo "Opening Reddit r/ethpuzzles..."
start https://reddit.com/r/ethpuzzles 2>/dev/null || 
xdg-open https://reddit.com/r/ethpuzzles 2>/dev/null ||
echo "  → https://reddit.com/r/ethpuzzles"

sleep 2

# Open Twitter
echo ""
echo "Opening Twitter #EthereumPuzzle..."
start "https://twitter.com/search?q=%23EthereumPuzzle" 2>/dev/null || 
xdg-open "https://twitter.com/search?q=%23EthereumPuzzle" 2>/dev/null ||
echo "  → https://twitter.com/search?q=%23EthereumPuzzle"

sleep 2

# Open OpenSea
echo ""
echo "Opening OpenSea puzzles..."
start "https://opensea.io/collection?search[query]=puzzle" 2>/dev/null || 
xdg-open "https://opensea.io/collection?search[query]=puzzle" 2>/dev/null ||
echo "  → https://opensea.io (search 'puzzle')"

echo ""
echo "✅ All sources opened!"
echo ""
echo "Next steps:"
echo "  1. Check Etherscan verified contracts"
echo "  2. Look for contracts with ETH balance"
echo "  3. Read source code"
echo "  4. Find solve() functions"
echo "  5. SOLVE AND WIN!"
echo ""
echo "Good luck! 🍀"
