"""
Project: City-Council-Meeting-Analyzer
File: utils/pseudonymize.py
Version: V0.2.004
Author: Joel Greenberg (joelontheroad)

Compliance: GDPR Article 25 (Pseudonymization)
Description: SHA-256 salted hashing for deterministic speaker ID masking.
"""

import hashlib

class Pseudonymizer:
    def __init__(self, salt: str):
        self.salt = salt

    def mask_name(self, name: str) -> str:
        """Transforms a name into a unique ID like [PERSON_a1b2c3]"""
        if not name: return "[UNKNOWN]"
        # Salted hashing ensures raw names never reach the public export
        payload = f"{name.strip().lower()}{self.salt}"
        hash_result = hashlib.sha256(payload.encode()).hexdigest()
        return f"[PERSON_{hash_result[:6]}]"
