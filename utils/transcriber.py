# ****************************************************************************
# * *
# * City Council Meeting Analyzer                                            *
# * Version: 0.2.016                                                         *
# * Component: AI Transcriber (Whisper with Live Feed)                       *
# * Author: joelontheroad                                                    *
# * *
# ****************************************************************************

import os
import whisper
import torch

class MeetingTranscriber:
    def __init__(self, model_size="base"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"🎙️ Initializing Whisper on: {self.device}")
        self.model = whisper.load_model(model_size, device=self.device)

    def transcribe(self, file_path):
        if not os.path.exists(file_path):
            return None

        print(f"🎙️ Transcribing: {os.path.basename(file_path)}")
        try:
            # THE CHANGE IS HERE: Added verbose=True
            result = self.model.transcribe(
                file_path, 
                fp16=(self.device == "cuda"),
                verbose=True  
            )
            return result["text"]
        except Exception as e:
            print(f"❌ Whisper transcription failed: {e}")
            return None
