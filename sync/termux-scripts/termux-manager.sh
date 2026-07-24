#!/data/data/com.termux/files/usr/bin/bash
# Termux Sync Script for Cipher Solving Suite
# Syncs with PC and manages puzzle data

VERSION="2.0.0"
SYNC_DIR="/sdcard/cipher-suite-sync"
HERMES_DIR="/data/data/com.termux/files/home/cipher-solving-suite"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Cipher Solving Suite - Termux Sync v${VERSION}${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Setup directories
setup() {
    echo "[SETUP] Creating sync directories..."
    mkdir -p "$SYNC_DIR/active-puzzles"
    mkdir -p "$SYNC_DIR/solutions"
    mkdir -p "$SYNC_DIR/intelligence"
    mkdir -p "$SYNC_DIR/shared"
    mkdir -p "$HERMES_DIR"
    echo -e "${GREEN}✓ Directories ready${NC}"
}

# Pull from PC
pull_from_pc() {
    echo "[SYNC] Pulling updates from PC..."
    
    if [ -d "$SYNC_DIR" ]; then
        cp -r "$SYNC_DIR"/* "$HERMES_DIR/" 2>/dev/null
        echo -e "${GREEN}✓ Synced from PC${NC}"
    else
        echo -e "${YELLOW}⚠ No PC data found${NC}"
    fi
}

# Push to PC  
push_to_pc() {
    echo "[SYNC] Pushing to PC..."
    
    if [ -d "$HERMES_DIR" ]; then
        cp -r "$HERMES_DIR"/* "$SYNC_DIR/" 2>/dev/null
        echo -e "${GREEN}✓ Pushed to PC${NC}"
    fi
}

# Check puzzle status
check_puzzles() {
    echo "[STATUS] Checking active puzzles..."
    
    if [ -f "$HERMES_DIR/intelligence/puzzle-database.json" ]; then
        echo "Active puzzles found:"
        cat "$HERMES_DIR/intelligence/puzzle-database.json" | grep -o '"active"' | wc -l
    else
        echo "No puzzle database yet"
    fi
}

# Research mode
research_mode() {
    echo "[RESEARCH] Starting research session..."
    echo ""
    echo "Sources to check:"
    echo "  • Reddit: r/codes, r/cryptography, r/puzzles"
    echo "  • CTFtime: ctftime.org"
    echo "  • HackerOne: hackerone.com"
    echo ""
    echo "Use browser to research new puzzles"
    echo "Document findings in $HERMES_DIR/research/"
}

# Solve mode
solve_mode() {
    echo "[SOLVE] Active puzzle solving..."
    echo ""
    echo "Available tools:"
    echo "  • solvers/cryptographic/ - Cipher tools"
    echo "  • solvers/steganography/ - Image analysis"
    echo "  • solvers/brute-force/ - Password cracking"
    echo ""
    echo "Choose puzzle and start solving!"
}

# Auto sync
auto_sync() {
    echo "[AUTO] Starting auto-sync (Ctrl+C to stop)..."
    
    while true; do
        pull_from_pc
        sleep 300  # Sync every 5 minutes
    done
}

# Show help
show_help() {
    echo ""
    echo "Usage: $0 [COMMAND]"
    echo ""
    echo "Commands:"
    echo "  setup       - Initialize directories"
    echo "  pull        - Pull from PC"
    echo "  push        - Push to PC"
    echo "  research    - Start research mode"
    echo "  solve       - Start solving mode"
    echo "  status      - Check puzzle status"
    echo "  auto        - Auto-sync mode"
    echo "  help        - Show this help"
    echo ""
    echo "Examples:"
    echo "  $0 setup"
    echo "  $0 research"
    echo "  $0 solve"
}

# Main
case "$1" in
    setup)
        setup
        ;;
    pull)
        pull_from_pc
        ;;
    push)
        push_to_pc
        ;;
    research)
        research_mode
        ;;
    solve)
        solve_mode
        ;;
    status)
        check_puzzles
        ;;
    auto)
        auto_sync
        ;;
    help|--help|-h|*)
        show_help
        ;;
esac

echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Cipher Solving Suite - Termux Ready${NC}"
echo -e "${BLUE}========================================${NC}"
