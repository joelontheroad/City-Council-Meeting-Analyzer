#!/bin/bash
# """
# Project: City-Council-Meeting-Analyzer
# Version: V0.2.004
# Security: NIST-Aligned Privacy Protection
# Principles: NIST SP 800-122 Aligned (Salted Pseudonymization & Operational Autonomy)
# """

echo "🚀 Initializing V0.2.004 Environment..."

# 1. Create Directory Structure
mkdir -p temp_buffer
mkdir -p data/vault/raw_video
mkdir -p data/vault/transcripts
mkdir -p reports

# 2. Check for FFmpeg (Required for FixupM3u8)
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠️ FFmpeg not found. Installing..."
    sudo apt update && sudo apt install -y ffmpeg
else
    echo "✅ FFmpeg is installed."
fi

# 3. Install Python Dependencies
pip install -r requirements.txt

echo "✅ Setup complete. Ready for local-first analysis."
