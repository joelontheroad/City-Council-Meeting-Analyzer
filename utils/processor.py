# ****************************************************************************
# * *
# * City Council Meeting Analyzer                                            *
# * Version: 0.2.004                                                         *
# * Author: joelontheroad                                                    *
# * *
# ****************************************************************************

import os
from utils.transcriber import Transcriber
from utils.config_loader import get_paths

class MeetingProcessor:
    def __init__(self, model_size="base"):
        self.transcriber = Transcriber(model_size=model_size)
        self.paths = get_paths()

    def process(self, video_path, keywords=None):
        """Orchestrates the transcription and storage process."""
        base_name = os.path.splitext(os.path.basename(video_path))[0]
        output_path = os.path.join(self.paths['vault'], "transcripts", f"{base_name}.txt")
        
        success = self.transcriber.run(video_path, output_path)
        
        if success:
            with open(output_path, "r") as f:
                return f.read()
        return None
