# """
# Project: City-Council-Meeting-Analyzer
# Version: V0.2.004
# Security: NIST-Aligned Privacy Protection
# Principles: NIST SP 800-122 Aligned (Salted Pseudonymization & Operational Autonomy)
# """

import os
import shutil
import yaml

def migrate():
    # 1. Load the configuration
    config_path = "configs/default.yaml"
    if not os.path.exists(config_path):
        print(f"❌ Error: {config_path} not found. Please run configure_paths.py first.")
        return

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    # 2. Define Destinations from Config
    vault_video = os.path.join(config['storage']['vault_path'], "raw_video")
    vault_text = os.path.join(config['storage']['vault_path'], "transcripts")

    # 3. UPDATE THIS: The path where your old meeting files are currently stored
    legacy_source = "/path/to/your/old/data" 

    if not os.path.exists(legacy_source):
        print(f"❌ Error: Source path '{legacy_source}' not found. Update the script with your correct path.")
        return

    # Ensure Vault directories exist
    os.makedirs(vault_video, exist_ok=True)
    os.makedirs(vault_text, exist_ok=True)

    print(f"🚀 Ingesting data from {legacy_source}...")

    # 4. Processing Loop
    files = os.listdir(legacy_source)
    for file in files:
        src_path = os.path.join(legacy_source, file)
        
        if file.endswith(".mp4"):
            shutil.move(src_path, os.path.join(vault_video, file))
            print(f"📦 Moved Video: {file}")
            
        elif file.endswith(".txt"):
            shutil.move(src_path, os.path.join(vault_text, file))
            print(f"📄 Moved Transcript: {file}")

    print("\n✅ Migration complete. The Vault is now populated and indexed.")

if __name__ == "__main__":
    migrate()
