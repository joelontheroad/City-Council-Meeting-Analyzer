"""
Project: City-Council-Meeting-Analyzer
Version: V0.2.004
Security: NIST-Aligned Privacy Protection
Principles: NIST SP 800-122 Aligned (Salted Pseudonymization & Operational Autonomy)
"""

import torch
import os
import gc

def verify_environment():
    """Checks for .env and basic requirements."""
    if not os.path.exists(".env"):
        print("❌ Error: .env file missing. NIST-aligned salt required.")
        return False
    return True

def get_optimal_model(config):
    """
    Programmer's Logic: Prevents OOM 'Killed' errors by matching 
    model size to available VRAM.
    """
    if not config['processing']['auto_hardware_check']:
        return config['processing']['model_size']

    if not torch.cuda.is_available():
        return "tiny"

    # Get total VRAM in GB
    vram = torch.cuda.get_device_properties(0).total_memory / 1e9
    
    # 12GB Safety Logic (Your Hardware)
    if vram >= 11:
        return "medium"  
    elif vram >= 7:
        return "small"
    else:
        return "base"

def clear_memory():
    """Forces GPU and RAM to release unused data."""
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
