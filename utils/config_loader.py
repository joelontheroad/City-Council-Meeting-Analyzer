# ****************************************************************************
# * *
# * City Council Meeting Analyzer                                            *
# * Version: 0.2.028                                                         *
# * Component: Config Loader (Fixed Scope & Clean RAID Check)                *
# * Author: joelontheroad                                                    *
# * *
# ****************************************************************************

import yaml
import os
import sys

def get_paths():
    config_path = os.path.join("configs", "default.yaml")
    
    if not os.path.exists(config_path):
        print(f"❌ Config file not found at {config_path}")
        sys.exit(1)

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    
    # Extract from the 'storage' nested key in default.yaml
    storage_cfg = config.get('storage', {})
    staging = storage_cfg.get('staging_buffer')
    vault = storage_cfg.get('permanent_vault')

    # RAID DRIVE SAFETY CHECK
    # We verify the path exists to ensure the drive is mounted.
    if not vault or not os.path.exists(vault):
        print("\n" + "!"*60)
        print(f"🚨 RAID DRIVE ERROR: The vault path does not exist!")
        print(f"Path: {vault}")
        print("Please ensure your RAID 6 array is MOUNTED.")
        print("!"*60 + "\n")
        sys.exit(1)

    # Return the flattened dictionary for use in main.py
    return {
        "staging_buffer": staging,
        "permanent_vault": vault
    }
