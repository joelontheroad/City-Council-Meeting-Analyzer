"""
Project: City-Council-Meeting-Analyzer
Version: V0.2.004
Security: NIST-Aligned Privacy Protection
Principles: NIST SP 800-122 Aligned (Salted Pseudonymization & Operational Autonomy)
"""

import os
import yaml
import shutil
from utils.system_checks import verify_environment, get_optimal_model, clear_memory
from analysis.transcriber import Transcriber

def load_config():
    with open("configs/default.yaml", "r") as f:
        return yaml.safe_load(f)

def main():
    if not verify_environment():
        return

    config = load_config()
    buffer_dir = config['storage']['buffer_path']
    vault_dir = config['storage']['vault_path']
    transcript_dir = os.path.join(vault_dir, "transcripts")
    video_vault = os.path.join(vault_dir, "raw_video")

    # Determine Model
    selected_model = get_optimal_model(config)
    
    # Example Loop Logic
    meeting_id = "austin_305483"
    final_video_path = os.path.join(video_vault, f"{meeting_id}.mp4")
    final_transcript_path = os.path.join(transcript_dir, f"{meeting_id}.txt")

    # 1. Check Force Skip
    if meeting_id in config['processing']['force_skip']:
        print(f"⚠️ Force Skip triggered for {meeting_id}")
        return

    # 2. Check if already analyzed
    if config['processing']['skip_existing_transcripts'] and os.path.exists(final_transcript_path):
        print(f"✅ Already processed {meeting_id}. Jumping to Intent Engine.")
    else:
        # Perform Transcription
        ts = Transcriber(selected_model, config['processing']['compute_type'])
        ts.run(final_video_path, final_transcript_path)

    print("🏁 Phase complete.")

if __name__ == "__main__":
    main()
