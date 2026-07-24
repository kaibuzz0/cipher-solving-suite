#!/usr/bin/env python3
"""
Sync Daemon - Termux/PC Bridge
Real-time synchronization between devices
"""

import os
import json
import time
from datetime import datetime
from pathlib import Path

class SyncDaemon:
    """Production sync daemon"""
    
    def __init__(self, mode="pc"):
        self.mode = mode  # "pc" or "termux"
        self.config = self._load_config()
        self.sync_dir = self._get_sync_dir()
        
    def _load_config(self):
        """Load sync config"""
        config_path = "config/sync-config.json"
        if os.path.exists(config_path):
            with open(config_path) as f:
                return json.load(f)
        return {
            "sync_enabled": True,
            "interval": 300,
            "sync_dirs": [
                "research/active-puzzles",
                "research/solutions",
                "intelligence/feeds",
                "workspace/active"
            ]
        }
    
    def _get_sync_dir(self):
        """Get sync directory based on platform"""
        if self.mode == "termux":
            return "/sdcard/cipher-suite-sync"
        else:
            return os.path.expanduser("~/cipher-suite-sync")
    
    def sync_now(self):
        """Execute sync"""
        print(f"[{datetime.now()}] Syncing...")
        
        for dir_path in self.config["sync_dirs"]:
            self._sync_directory(dir_path)
        
        print(f"[{datetime.now()}] Sync complete")
    
    def _sync_directory(self, dir_path):
        """Sync a specific directory"""
        src = Path(dir_path)
        dst = Path(self.sync_dir) / dir_path
        
        if not src.exists():
            return
        
        os.makedirs(dst, exist_ok=True)
        
        # Copy files that have changed
        for file_path in src.rglob("*"):
            if file_path.is_file():
                relative = file_path.relative_to(src)
                dst_file = dst / relative
                
                if not dst_file.exists() or self._file_changed(file_path, dst_file):
                    os.makedirs(dst_file.parent, exist_ok=True)
                    import shutil
                    shutil.copy2(file_path, dst_file)
    
    def _file_changed(self, src, dst):
        """Check if file has changed"""
        return os.path.getmtime(src) > os.path.getmtime(dst)
    
    def run_daemon(self):
        """Run continuous sync"""
        print(f"🔄 Sync Daemon Started ({self.mode} mode)")
        print(f"   Syncing every {self.config['interval']} seconds")
        print(f"   Press Ctrl+C to stop")
        
        try:
            while True:
                self.sync_now()
                time.sleep(self.config["interval"])
        except KeyboardInterrupt:
            print("\n👋 Sync daemon stopped")

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["pc", "termux"], default="pc")
    parser.add_argument("--once", action="store_true", help="Sync once and exit")
    args = parser.parse_args()
    
    daemon = SyncDaemon(mode=args.mode)
    
    if args.once:
        daemon.sync_now()
    else:
        daemon.run_daemon()

if __name__ == "__main__":
    main()
