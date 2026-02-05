"""
Project: City-Council-Meeting-Analyzer
Version: V0.2.004
Security: NIST-Aligned Privacy Protection
Principles: NIST SP 800-122 Aligned (Salted Pseudonymization & Operational Autonomy)
"""

import yaml
import os

def run_config():
    print("🛠️  City Council Analyzer: Path Configuration Helper")
    print("---------------------------------------------------")
    
    # 1. Get Buffer Path (RAID 1 / Fast Disk)
    default_buffer = "./temp_buffer"
    buffer = input(f"Enter path for Processing Buffer (Press Enter for '{default_buffer}'): ").strip()
    if not buffer: buffer = default_buffer

    # 2. Get Vault Path (RAID 6 / Archival)
    default_vault = "./data/vault"
    vault = input(f"Enter path for Archival Vault (Press Enter for '{default_vault}'): ").strip()
    if not vault: vault = default_vault

    # 3. Create the directories if they don't exist
    for p in [buffer, vault]:
        os.makedirs(p, exist_ok=True)
        print(f"✅ Verified Directory: {p}")

    # 4. Update the YAML
    config_path = "configs/default.yaml"
    
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            data = yaml.safe_load(f)
        
        data['storage']['buffer_path'] = buffer
        data['storage']['vault_path'] = vault

        with open(config_path, 'w') as f:
            yaml.dump(data, f, default_flow_style=False)
        
        print(f"\n🚀 Configuration updated successfully in {config_path}!")
    else:
        print(f"❌ Error: {config_path} not found. Ensure you are in the project root.")

if __name__ == "__main__":
    run_config()
