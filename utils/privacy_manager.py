# ****************************************************************************
# * *
# * City Council Meeting Analyzer                                           *
# * Version: 0.2.004                                                        *
# * Author: joelontheroad                                                   *
# * License: As-Is / Experimental                                           *
# * *
# ****************************************************************************

import os
import hashlib
from dotenv import load_dotenv

# Load the secret salt from the .env file we created earlier
load_dotenv()
SALT = os.getenv("PSEUDO_SALT")

def generate_pseudo_id(name):
    """
    Creates a consistent, anonymous ID for a speaker using a keyed hash.
    Follows NIST 800-122 guidelines for de-identification.
    """
    if not SALT:
        raise ValueError("Privacy Key (PSEUDO_SALT) not found in .env file!")
    
    # Combine the name with our secret salt
    # Using lowercase and stripping whitespace ensures consistency 
    # regardless of how the AI transcribes the spelling.
    combined = name.strip().lower() + SALT
    
    # Generate a SHA-256 hash and take the first 8 characters for readability
    hash_object = hashlib.sha256(combined.encode())
    return f"CITIZEN_{hash_object.hexdigest()[:8]}"

def mask_identities(transcript_text):
    """
    Scans the transcript for identified speakers and replaces names 
    with their consistent pseudonyms.
    """
    print("🔒 Processing text for PII masking...")
    
    # Note: Version 0.2.004 provides the hashing logic. 
    # Version 0.2.00
