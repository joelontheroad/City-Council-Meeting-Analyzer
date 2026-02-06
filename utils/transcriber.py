# ****************************************************************************
# * *
# * City Council Meeting Analyzer                                            *
# * Version: 0.2.004                                                         *
# * Security: NIST-Aligned Privacy Protection                                *
# * *
# ****************************************************************************

import os
import torch
from faster_whisper import WhisperModel
from utils.system_checks import clear_memory

class Transcriber:
    def __init__(self, model_size="base", compute_type="int8"):
        """
        Initializes the transcription engine with hardware-aware safety checks.
        """
        self.model_size = model_size
        
        # 1. Automatic Hardware Detection
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # 2. Automated Compatibility Override
        # float16 is a GPU-only optimization. On CPU, it causes an immediate crash.
        if self.device == "cpu" and compute_type == "float16":
            print("⚠️  Hardware Warning: float16 detected on CPU. Auto-correcting to int8.")
            self.compute_type = "int8"
        else:
            self.compute_type = compute_type
            
        print(f"📡 Transcriber initialized on device: {self.device} ({self.compute_type})")

    def run(self, input_path, output_path):
        """
        Transcribes the provided audio/video file and saves results to the vault.
        """
        if os.path.exists(output_path):
            print(f"⏭️  Transcript already exists at {output_path}. Skipping.")
            return True

        print(f"🎙️  Loading Whisper {self.model_size}...")
        
        try:
            model = WhisperModel(
                self.model_size, 
                device=self.device, 
                compute_type=self.compute_type
            )
            
            print(f"🎙️  Transcribing: {os.path.basename(input_path)}")
            segments, info = model.transcribe(input_path, beam_size=5)
            
            with open(output_path, "w") as f:
                for segment in segments:
                    # Formatting with timestamps for better record keeping
                    f.write(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}\n")
            
            # Programmer's Note: Explicit cleanup to free up VRAM/RAM for the next task
            del model
            clear_memory()
            return True

        except Exception as e:
            print(f"❌ Transcription failed: {e}")
            return False

