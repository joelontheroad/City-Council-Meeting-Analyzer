# ****************************************************************************
# * *
# * City Council Meeting Analyzer                                            *
# * Version: 0.2.023                                                         *
# * Component: AI Processor (Metadata & Table Injection)                      *
# * Author: joelontheroad                                                    *
# * *
# ****************************************************************************

import requests
import json
import os

class MeetingProcessor:
    def __init__(self, api_url="http://localhost:1234/v1/chat/completions"):
        self.api_url = api_url
        self.prompts = self._load_prompts()

    def _load_prompts(self):
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'configs', 'prompts.json')
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except:
            return {"system_instruction": "Expert Analyst", "analysis_focus": "Gaza war", "segment_prompt": "{focus}", "synthesis_prompt": "Combine."}

    def process(self, text, mask=False, source_name="Unknown Source"):
        if len(text) > 15000:
            return self.summarize_recursive(text, source_name)
        
        focus = self.prompts['analysis_focus']
        # Inject source name into the prompt instruction
        full_instruction = f"SOURCE MATERIAL: {source_name}\n\n{self.prompts['segment_prompt'].format(focus=focus)}"
        return self._call_llm(text, full_instruction)

    def summarize_recursive(self, text, source_name):
        chunks = self.chunk_text(text)
        summaries = []
        focus = self.prompts['analysis_focus']
        segment_instr = f"SOURCE MATERIAL: {source_name}\n\n{self.prompts['segment_prompt'].format(focus=focus)}"

        for i, chunk in enumerate(chunks):
            print(f"🧠 Analyzing Chapter {i+1}/{len(chunks)}...")
            summaries.append(self._call_llm(chunk, segment_instr))

        print("📝 Synthesizing Final Master Report...")
        combined = "\n\n".join(summaries)
        return self._call_llm(combined, self.prompts['synthesis_prompt'])

    def chunk_text(self, text, max_chars=12000):
        chunks = []; current = ""
        for line in text.split('\n'):
            if len(current) + len(line) < max_chars: current += line + "\n"
            else: chunks.append(current); current = line + "\n"
        if current: chunks.append(current)
        return chunks

    def _call_llm(self, text, instruction):
        payload = {
            "messages": [
                {"role": "system", "content": self.prompts['system_instruction']},
                {"role": "user", "content": f"{instruction}\n\nTEXT:\n{text}"}
            ],
            "temperature": 0.1
        }
        try:
            r = requests.post(self.api_url, json=payload, timeout=300)
            return r.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"❌ Error: {e}"
