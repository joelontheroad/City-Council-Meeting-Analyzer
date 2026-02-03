"""
Project: City-Council-Meeting-Analyzer
File: utils/check_env.py
Version: V0.2.004
Author: Joel Greenberg (joelontheroad)
Description: Verifies environment integrity and hardware acceleration.
"""

import sys
import importlib.util

def run_checks():
    packages = ['faster_whisper', 'spacy', 'openai', 'dotenv', 'yaml']
    print("\n[Diagnostic] Checking dependencies...")
    
    missing = []
    for pkg in packages:
        if importlib.util.find_spec(pkg) is None:
            missing.append(pkg)
            print(f" ❌ {pkg} is missing.")
        else:
            print(f" ✅ {pkg} installed.")
            
    if missing:
        print("\n[!] Please run 'pip install -r requirements.txt'")
        sys.exit(1)
    
    print("[Diagnostic] Environment is healthy.\n")

if __name__ == "__main__":
    run_checks()
    
