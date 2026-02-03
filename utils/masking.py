import hmac
import hashlib
import os
from dotenv import load_dotenv

def mask_name(name):
    """
    Converts a speaker's name into a salted SHA-256 hash.
    This provides deterministic pseudonymization (same name + same salt = same ID).
    """
    # 1. Load the secret salt from your .env file
    load_dotenv()
    salt = os.getenv("PSEUDO_SALT")

    if not salt:
        # Fallback to a warning if salt is missing, but don't stop the program
        # In a production air-gap, verify_environment() would have caught this.
        return f"UNMASKED_{name}"

    if not name:
        return "UNKNOWN_SPEAKER"

    # 2. Clean the input (standardize to lowercase to avoid hash mismatches)
    clean_name = name.strip().lower()

    # 3. Perform HMAC-SHA256
    # We use HMAC because it's the professional standard for 'Keyed' hashing.
    hash_object = hmac.new(
        salt.encode('utf-8'), 
        clean_name.encode('utf-8'), 
        hashlib.sha256
    )
    
    # 4. Return a 'Slug' (First 12 characters are usually enough for uniqueness)
    # Full hash is 64 chars, but that's overkill for city council meetings.
    return hash_object.hexdigest()[:12]

if __name__ == "__main__":
    # Test Logic
    test_name = "John Doe"
    print(f"Original: {test_name}")
    print(f"Masked:   {mask_name(test_name)}")
