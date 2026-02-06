# ****************************************************************************
# * *
# * City Council Meeting Analyzer                                            *
# * Version: 0.2.007                                                         *
# * Component: AI Analysis & Privacy Processor                               *
# * Author: joelontheroad                                                    *
# * *
# ****************************************************************************

import requests
import json
import os

class MeetingProcessor:
    def __init__(self, endpoint="http://localhost:1234/v1"):
        self.endpoint = f"{endpoint}/chat/completions"
        self.config_path = os.path.join("config", "prompts.json")
        
    def _load_prompts(self):
        """Loads AI instructions from the config file."""
        default_prompts = {
            "system_analyst": "You are a policy analyst.",
            "privacy_directive": "Mask all PII."
        }
        
        if not os.path.exists(self.config_path):
            return default_prompts
            
        try:
            with open(self.config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️ Warning: Could not read prompts.json: {e}")
            return default_prompts

    def process(self, transcript_text, mask=False):
        """
        Sends transcript to LMStudio.
        Applies GDPR masking via the system prompt if 'mask' is True.
        """
        prompts = self._load_prompts()
        
        # Build the system instruction
        system_content = prompts.get("system_analyst", "")
        if mask:
            # Combine the analyst role with the strict GDPR requirements
            system_content += " " + prompts.get("privacy_directive", "")

        payload = {
            "messages": [
                {"role": "system", "content": system_content},
                {"role": "user", "content": f"Transcript to analyze:\n\n{transcript_text}"}
            ],
            "temperature": 0.2,
            "model": "local-model" # LMStudio usually ignores this, but it's required for the API
        }

        print(f"🧠 Analysis Started (GDPR Masking: {'ENABLED' if mask else 'DISABLED'})")
        
        try:
            response = requests.post(self.endpoint, json=payload, timeout=300) # 5 min timeout for long transcripts
            if response.status_code == 200:
                result = response.json()
                return result['choices'][0]['message']['content']
            else:
                return f"❌ LMStudio API Error: {response.status_code}"
        except Exception as e:
            return f"❌ Connection Error: Is LMStudio running at {self.endpoint}? {e}"
