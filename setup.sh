#!/bin/bash
"""
Project: City-Council-Meeting-Analyzer
Version: V0.2.004
Security: GDPR-Ready (Privacy by Design)
Principles: NIST SP 800-122 Aligned (Salted Pseudonymization & Operational Autonomy)
"""

echo "🚀 Initializing NIST-Aligned Project Structure..."

# Create Directory Tree
mkdir -p configs data/raw_video data/transcripts reports jurisdictions analysis utils

# Create Placeholder Config with Examples
if [ ! -f configs/default.yaml ]; then
    cat <<EOT >> configs/default.yaml
"""
Project: City-Council-Meeting-Analyzer
Version: V0.2.004
Security: GDPR-Ready (Privacy by Design)
Principles: NIST SP 800-122 Aligned (Salted Pseudonymization & Operational Autonomy)
"""
paths:
  work_dir: "./data"
  raw_video: "./data/raw_video"
  transcripts: "./data/transcripts"
  archive_dir: "./reports"

force_skip: [] # Leave empty to process all discovered meetings

analysis_goals:
  topic: "General Meeting Summary"
  intent_to_detect: "Provide a neutral summary of all discussed agenda items."
  keywords: []
EOT
    echo "✅ Created default config."
fi

# Generate .env with a secure NIST-aligned salt
if [ ! -f .env ]; then
    SECURE_SALT=$(openssl rand -hex 16)
    echo "PSEUDO_SALT=$SECURE_SALT" >> .env
    echo "✅ Generated secure .env with unique salt."
fi

echo "✅ Setup Complete."
