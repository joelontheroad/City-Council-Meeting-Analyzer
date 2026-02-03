import shutil
import os
from dotenv import load_dotenv

def check_disk_space(path=".", min_gb=20):
    """Checks if the SSD has enough 'runway' to process high-res video."""
    total, used, free = shutil.disk_usage(path)
    free_gb = free // (2**30) 
    
    if free_gb < min_gb:
        print(f"❌ CRITICAL: Low disk space ({free_gb}GB).")
        print(f"This program requires at least {min_gb}GB to handle video/audio transients.")
        return False
    
    print(f"✅ SSD Capacity: {free_gb}GB available.")
    return True

def verify_environment():
    """Ensures the .env file and Salt exist before processing starts."""
    load_dotenv()
    if not os.getenv("PSEUDO_SALT"):
        print("⚠️ WARNING: No PSEUDO_SALT found in .env.")
        print("PII masking will not be deterministic. Please check your setup.")
        return False
    return True
    
