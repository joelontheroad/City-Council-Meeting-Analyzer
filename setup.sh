#!/bin/bash
# Project: City-Council-Meeting-Analyzer
# File: setup.sh
# Version: V0.2.004
# Author: Joel Greenberg (joelontheroad)

echo "[*] Setting up Hardened Environment for City-Council-Meeting-Analyzer..."

# 1. Python Virtual Environment
python3 -m venv venv
source venv/bin/activate

# 2. Dependency Management
pip install --upgrade pip
pip install -r requirements.txt
python3 -m spacy download en_core_web_sm

# 3. Secure Salt Generation (GDPR Article 25 Compliance)
if [ ! -f .env ]; then
    cp .env.example .env
    # Generate a 32-character CSPRNG salt
    SALT=$(python3 -c 'import secrets; print(secrets.token_hex(16))')
    sed -i "s/replace-this-with-a-secure-random-string/$SALT/" .env
    echo "[+] Unique Secure Salt generated and saved to .env"
fi

# 4. Pre-flight Diagnostic
python3 utils/check_env.py
