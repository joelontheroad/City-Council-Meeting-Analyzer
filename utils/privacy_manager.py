# ****************************************************************************
# * *
# * City Council Meeting Analyzer                                            *
# * Version: 0.2.006                                                         *
# * Component: Privacy & Identity Masking Utility                            *
# * Author: joelontheroad                                                    *
# * *
# ****************************************************************************

import re

class PrivacyManager:
    def __init__(self):
        # Dictionary to keep track of identified names to ensure consistency
        # e.g., "John Doe" always becomes "[PERSON_1]" in the same transcript
        self.identity_map = {}
        self.counter = 1

    def mask_identities(self, text):
        """
        Identifies and redacts names using pattern matching.
        In a production environment, this would integrate with a 
        Natural Language Processing (NLP) library like spaCy.
        """
        if not text:
            return text

        # A robust regex for common name patterns (Title Case names)
        # Note: This is our 'Version 1' heuristic logic.
        name_pattern = r"\b([A-Z][a-z]+ [A-Z][a-z]+)\b"
        
        found_names = re.findall(name_pattern, text)
        
        masked_text = text
        for name in set(found_names):
            if name not in self.identity_map:
                self.identity_map[name] = f"[PERSON_{self.counter}]"
                self.counter += 1
            
            # Replace name with the assigned placeholder
            masked_text = masked_text.replace(name, self.identity_map[name])
            
        return masked_text
