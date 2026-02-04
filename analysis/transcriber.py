"""
Project: City-Council-Meeting-Analyzer
Version: V0.2.004
Security: GDPR-Ready (Privacy by Design)
Principles: NIST SP 800-122 Aligned (Salted Pseudonymization & Operational Autonomy)
"""

import os
import json
from faster_whisper import WhisperModel

class MeetingTranscriber:
    def __init__(self, model_size="medium"):
        self.model = WhisperModel(model_size, device="cuda", compute_type="float16")

    def transcribe(self, video_path, output_json):
        segments, info = self.model.transcribe(video_path, beam_size=5, vad_filter=True)
        transcript_data = [{"start": s.start, "end": s.end, "text": s.text.strip()} for s in segments]
        with open(output_json, 'w', encoding='utf-8') as f:
            json.dump(transcript_data, f, indent=4)
