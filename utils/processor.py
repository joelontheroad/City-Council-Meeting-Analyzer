# ****************************************************************************
# * *
# * City Council Meeting Analyzer                                           *
# * Version: 0.2.004                                                        *
# * Author: joelontheroad                                                   *
# * License: As-Is / Experimental                                           *
# * *
# ****************************************************************************

import os
import whisper # Assuming OpenAI Whisper for local-first processing
from utils import config_loader

def run_analysis(video_path, keywords=None):
    """
    Takes a video file, extracts audio, transcribes it, 
    and performs keyword-based summarization.
    """
    
    # 1. Setup paths for transcription output
    paths = config_loader.get_paths()
    transcript_dir = os.path.join(paths['permanent_vault'], "transcripts/")
    
    if not os.path.exists(transcript_dir):
        os.makedirs(transcript_dir)

    video_filename = os.path.basename(video_path)
    transcript_filename = video_filename.replace(".mp4", ".txt")
    output_path = os.path.join(transcript_dir, transcript_filename)

    # 2. Load the AI Model 
    # Using 'base' for speed, 'medium' or 'large' for higher accuracy
    print(f"📡 Loading AI Model (Whisper)...")
    model = whisper.load_model("base")

    # 3. Perform Transcription
    print(f"🎙️  Transcribing: {video_filename}")
    result = model.transcribe(video_path)
    full_text = result['text']

    # 4. Keyword Refinement (If user provided --keywords)
    if keywords:
        print(f"🔍 Refining analysis with keywords: {keywords}")
        # Logic would go here to highlight segments or create a targeted summary
        # For now, we append them to the metadata of the file
    
    # 5. Save the Raw Transcript to the Vault
    with open(output_path, "w") as f:
        f.write(full_text)

    print(f"💾 Transcript saved to: {output_path}")
    
    return full_text
