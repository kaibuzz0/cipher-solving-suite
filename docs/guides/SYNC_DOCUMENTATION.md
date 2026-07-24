# 📡 Termux-PC Bridge Documentation

**Seamless synchronization between Android (Termux) and PC environments**

---

## 🌉 Bridge Architecture

```
PC (Windows/Linux/Mac)                          Termux (Android)
    │                                               │
    ├── cipher-solving-suite/                       ├── cipher-solving-suite/
    │   ├── research/                               │   ├── research/
    │   ├── solvers/                                │   ├── solvers/
    │   └── sync/pc-bridge/                         │   └── sync/termux-scripts/
    │           │                                           │
    │           └──────→  SHARED BRIDGE  ←───────────────┘
    │                   (Cloud/Git/Local)
    │                           │
    │           ┌─────────────┴─────────────┐
    │           │                             │
    │    Real-time sync                Batch sync
    │    (Every 5 min)                 (On demand)
    │
```

---

## 🔄 Sync Modes

### Mode 1: Real-Time Sync (Automatic)
**Trigger:** Every 5 minutes  
**Method:** File watching + git auto-commit

```bash
# On PC
python sync/pc-bridge/auto_sync_daemon.py

# On Termux
bash sync/termux-scripts/termux-manager.sh auto
```

### Mode 2: Manual Sync (On Demand)
**Trigger:** User command  
**Method:** Explicit push/pull

```bash
# Push PC → Bridge
python sync/pc-bridge/push.py

# Pull Bridge → Termux
bash sync/termux-scripts/termux-manager.sh pull
```

### Mode 3: Smart Sync (Intelligent)
**Trigger:** Before/after solving sessions  
**Method:** Selective sync based on changes

```bash
# Smart sync
python sync/pc-bridge/smart_sync.py --mode=pre-session
python sync/pc-bridge/smart_sync.py --mode=post-session
```

---

## 📁 What Gets Synced

### High Priority (Always Sync):
- `research/active-puzzles/` - Current targets
- `intelligence/` - Real-time feeds
- `workspace/collaboration/` - Team files
- `sync/shared-data/` - Common database

### Medium Priority (Session Sync):
- `solvers/` - Tools and results
- `docs/` - Documentation updates
- `assets/` - Wordlists and patterns

### Low Priority (Weekly Sync):
- `research/solved-case-studies/` - Archive
- `research/techniques/` - Methodology docs

---

## 🚀 Quick Sync Commands

### From PC:
```bash
# Full sync to bridge
make sync-push

# Pull from bridge
make sync-pull

# Status check
make sync-status
```

### From Termux:
```bash
# Setup sync
cd sync/termux-scripts
bash termux-manager.sh setup

# Pull updates
bash termux-manager.sh pull

# Push changes
bash termux-manager.sh push

# Auto-sync mode
bash termux-manager.sh auto
```

---

## 📱 Termux-Specific Features

### Optimized for Mobile:
- Lightweight sync (compressed data)
- Battery-aware (syncs only when charging)
- Network-efficient (WiFi only option)
- Storage management (auto-cleanup)

### Mobile Tools:
- Quick research mode
- Photo-to-text conversion
- QR code scanning
- Notification alerts

---

## 🔐 Security

### Sync Security:
- ✅ Encrypted transmission (HTTPS/SSH)
- ✅ Token-based authentication
- ✅ Integrity verification (checksums)
- ✅ No sensitive keys in sync

### Data Privacy:
- Personal notes excluded from sync
- Workspace/private folder stays local
- Team collaboration in shared space

---

## 🛠️ Troubleshooting

### Common Issues:

**Issue:** Sync fails
**Solution:** Check network, restart daemon

**Issue:** Conflicts
**Solution:** Manual merge, timestamp resolution

**Issue:** Large files
**Solution:** Exclude cache, compress data

**Issue:** Permission denied
**Solution:** Check SSH keys, token validity

---

## 📝 Sync Best Practices

1. **Before solving session:**
   ```bash
   sync-pull  # Get latest data
   ```

2. **During session:**
   ```bash
   # Work on local copy
   # Auto-sync handles backup
   ```

3. **After session:**
   ```bash
   sync-push  # Share findings
   ```

4. **End of day:**
   ```bash
   sync-full-backup  # Complete archive
   ```

---

## 🎯 Use Cases

### Library PC Session:
1. Pull latest from Termux
2. Research puzzles
3. Push findings back
4. Continue on phone

### Mobile Research:
1. Check puzzles on phone
2. Take photos of clues
3. Process with OCR
4. Sync to PC for solving

### Team Collaboration:
1. Share via sync bridge
2. Multiple devices access
3. Real-time updates
4. Version control

---

**Seamless cross-platform puzzle solving! 🚀**
