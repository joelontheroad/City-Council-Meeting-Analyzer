"""
Project: City-Council-Meeting-Analyzer
Version: V0.2.004
Security: NIST-Aligned Privacy Protection
Principles: NIST SP 800-122 Aligned (Salted Pseudonymization & Operational Autonomy)
"""

import os
from faster_whisper import WhisperModel
from utils.system_checks import clear_memory

class Transcriber:
    def __init__(self, model_size, compute_type):
        self.model_size = model_size
        self.compute_type = compute_type

    def run(self, input_path, output_path):
        """Transcribes video to text using memory-efficient settings."""
        if os.path.exists(output_path):
            return True

        print(f"🎙️ Loading Whisper {self.model_size}...")
        model = WhisperModel(self.model_size, device="cuda", compute_type=self.compute_type)
        
        segments, info = model.transcribe(input_path, beam_size=5)
        
        with open(output_path, "w") as f:
            for segment in segments:
                f.write(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}\n")
        
        # Programmer's Safety: Force release of model from VRAM
        del model
        clear_memory()
        return True
