# 🔍 ETHEREUM SMART CONTRACT PUZZLE HUNTING

**Method:** Manual search using Etherscan.io (No API needed)  
**Perfect for:** Library PCs, quick sessions  
**Prizes:** Real ETH, can verify before attempting

---

## 🎯 QUICK START (15 minutes)

### Step 1: Open Etherscan
```
URL: https://etherscan.io
```

### Step 2: Search for Puzzle Contracts
```
In search box, try:
- "puzzle"
- "treasure"
- "challenge"
- "riddle"
- "game"
- "crypto puzzle"
```

### Step 3: Filter by Balance
```
Look for contracts with:
✅ Balance > 0 ETH
✅ Recent activity
✅ Verified source code
```

### Step 4: Analyze Source Code
```
Click on contract → Contract tab
Look for:
- function solve(...)
- function claim(...)
- function answer(...)
- require(...) statements
- Prize/reward variables
```

### Step 5: Solve & Claim
```
1. Understand the puzzle
2. Find solution (password, math, etc.)
3. Interact with contract (MetaMask)
4. Call solve() or claim()
5. Receive ETH!
```

---

## 📊 WHAT TO LOOK FOR

### Good Signs (Likely Real Puzzle):
```solidity
✅ function solve(string answer) public
✅ function claim() external
✅ require(!solved, "Already solved")
✅ uint256 public prize = 1 ether;
✅ balance > 0 ETH
✅ Verified source code
✅ Recent transactions
```

### Red Flags (Scam/Ended):
```solidity
❌ Balance = 0 ETH
❌ No source code
❌ Already drained
❌ Suspicious functions (drain, steal)
❌ Too complex (likely honeypot)
```

---

## 🔧 TOOLS FOR LIBRARY PC

### Web-Based (No Install):
1. **Etherscan.io** - Main tool
2. **Remix IDE** - https://remix.ethereum.org
   - Analyze contracts
   - Test interactions
3. **EthConverter** - wei <-> ETH
4. **Dcode.fr** - For encodings

### With Phone:
1. **MetaMask mobile** - For transactions
2. **Etherscan app** - Quick checking
3. **Camera** - Screenshot addresses

---

## 💡 SEARCH STRATEGIES

### Strategy 1: Keyword Search
```
Etherscan search → Contracts tab
Keywords: puzzle, treasure, challenge, riddle
Sort by: Balance (high to low)
```

### Strategy 2: Recent Deployments
```
Look at recent verified contracts
Check which have ETH
Filter for puzzle-like names
```

### Strategy 3: Popular Puzzles
```
Search Twitter: #EthereumPuzzle
Check if contract still funded
See if community solving
```

### Strategy 4: NFT Projects
```
OpenSea.io
Some NFTs have "treasure hunt" mechanics
Check descriptions for clues
```

---

## 🏆 VERIFIED ACTIVE PUZZLES (Examples)

**Note:** These may be solved by now, use as template:

### Type 1: Password Puzzles
```solidity
function solve(string memory password) public {
    require(keccak256(password) == answerHash);
    payable(msg.sender).transfer(address(this).balance);
}
```
**How to solve:** Brute force password or find in clues

### Type 2: Math Puzzles
```solidity
function solve(uint256 answer) public {
    require(answer == 2**256 - 1);
    // Prize logic
}
```
**How to solve:** Calculate answer, call function

### Type 3: Riddle Puzzles
```solidity
function solve(string memory riddleAnswer) public {
    require(riddleAnswer == "something");
    // Prize logic
}
```
**How to solve:** Solve riddle, submit answer

### Type 4: NFT-Based
```
Contract: ERC721 with hidden clues
Prize: ETH or rare NFT
How: Analyze NFT metadata
```

---

## ⚠️ SAFETY RULES

### BEFORE SOLVING:
```
✅ Check contract balance (must be > 0)
✅ Read full source code
✅ Verify it's not a honeypot
✅ Check if already solved
✅ Understand the puzzle
```

### HONEYPOT DETECTION:
```
❌ Functions that drain your wallet
❌ Requires sending ETH to "solve"
❌ Hidden owner-only withdrawals
❌ Too good to be true prizes
```

### CLAIMING PRIZES:
```
✅ Use MetaMask (not on public PC!)
✅ Gas fees apply
✅ May need to be quick (others competing)
✅ Document your win!
```

---

## 📋 SESSION CHECKLIST

### At Library:
- [ ] Open etherscan.io
- [ ] Search "puzzle" contracts
- [ ] Filter by balance > 0
- [ ] Open 3-5 promising contracts
- [ ] Read source code
- [ ] Identify puzzle type
- [ ] Attempt solve (at home!)

### Documentation:
- [ ] Save contract addresses
- [ ] Screenshot code
- [ ] Note puzzle type
- [ ] Research solution method
- [ ] Plan solve strategy

---

## 🚀 READY TO HUNT?

**Next Steps:**
1. Go to etherscan.io
2. Search "puzzle"
3. Find active contracts
4. Analyze source
5. Solve and claim ETH!

**Good luck! 🍀**
