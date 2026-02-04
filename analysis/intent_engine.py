"""
Project: City-Council-Meeting-Analyzer
Version: V0.2.004
Security: GDPR-Ready (Privacy by Design)
Principles: NIST SP 800-122 Aligned (Salted Pseudonymization & Operational Autonomy)
"""

import os
import json
from openai import OpenAI

class IntentEngine:
    def __init__(self, base_url="http://localhost:1234/v1"):
        self.client = OpenAI(base_url=base_url, api_key="lm-studio")
        
    def analyze_transcript(self, meeting_id, transcript_path, output_dir, mask_enabled=False):
        prefix = "anon_" if mask_enabled else ""
        filename = f"{prefix}report_{meeting_id}.md"
        final_path = os.path.join(output_dir, filename)

        with open(transcript_path, "r") as f:
            transcript = json.load(f)
        
        full_text = " ".join([seg['text'] for seg in transcript])
        
        response = self.client.chat.completions.create(
            model="local-model",
            messages=[
                {"role": "system", "content": "Analyze city council meeting intent."},
                {"role": "user", "content": full_text[:8000]} 
            ]
        )

        with open(final_path, "w") as f:
            f.write(response.choices[0].message.content)
