"""
Project: City-Council-Meeting-Analyzer
Version: V0.2.004
Security: GDPR-Ready (Privacy by Design)
Principles: NIST SP 800-122 Aligned (Salted Pseudonymization & Operational Autonomy)
"""

import hmac
import hashlib
import os
from dotenv import load_dotenv

def mask_name(name):
    """
    Applies salted HMAC-SHA256 masking to a PII string.
    Aligned with NIST SP 800-122 De-identification standards.
    """
    load_dotenv()
    salt = os.getenv("PSEUDO_SALT")
    
    if not salt or not name:
        return "MASK_ERR_CHECK_ENV"

    hash_object = hmac.new(
        salt.encode('utf-8'), 
        name.strip().lower().encode('utf-8'), 
        hashlib.sha256
    )
    
    return hash_object.hexdigest()[:12]
