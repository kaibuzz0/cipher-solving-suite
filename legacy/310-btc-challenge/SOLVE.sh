#!/bin/bash
echo "🔥 310 BTC PUZZLE SOLVER"
echo "========================="
echo ""
python3 scripts/check_archives.py
echo ""
python3 scripts/search_reddit.py
echo ""
python3 scripts/analyze_image.py
echo ""
echo "Done! Check results above."
