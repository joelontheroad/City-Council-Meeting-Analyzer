"""
Project: City-Council-Meeting-Analyzer
Version: V0.2.004
Security: GDPR-Ready (Privacy by Design)
Principles: NIST SP 800-122 Aligned (Salted Pseudonymization & Operational Autonomy)

Workflow Logic:
1. Initialize environment (Local/SMB storage paths).
2. [Online Mode]: Fetch media via Austin ATXN Scraper.
3. [Air-Gap Capability - if desired]: Run Transcription & Intent Engine 100% 
   offline using local GPU (NVIDIA) and local LLM inference server.
"""

import argparse
import sys
import os
import yaml
from utils.system_checks import verify_environment
from jurisdictions.austin_tx import AustinScraper
from analysis.transcriber import MeetingTranscriber
from analysis.intent_engine import IntentEngine

def load_config():
    config_path = "configs/default.yaml"
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def ensure_paths(paths):
    for key, path in paths.items():
        os.makedirs(path, exist_ok=True)

def main():
    parser = argparse.ArgumentParser(description="City-Council-Meeting-Analyzer (V0.2.004)")
    parser.add_argument("--download-only", action="store_true", help="Online: Fetch raw media.")
    parser.add_argument("--local-only", action="store_true", help="Offline: Process local media.")
    parser.add_argument("--mask", action="store_true", help="Enable NIST-aligned pseudonymization.")
    args = parser.parse_args()

    config = load_config()
    paths = config.get("paths", {})
    ensure_paths(paths)
    
    if not verify_environment():
        sys.exit(1)

    if args.download_only:
        scraper = AustinScraper(storage_path=paths['raw_video'])
        scraper.run(skip_list=config.get('force_skip', []))
        return

    if args.local_only:
        transcriber = MeetingTranscriber()
        engine = IntentEngine()

        video_files = [f for f in os.listdir(paths['raw_video']) if f.endswith(".mp4")]
        for filename in video_files:
            m_id = filename.replace(".mp4", "")
            if m_id in config.get('force_skip', []):
                print(f"⏭️ Skipping ID: {m_id} (per config)")
                continue

            v_path = os.path.join(paths['raw_video'], filename)
            t_path = os.path.join(paths['transcripts'], f"{m_id}.json")
            
            transcriber.transcribe(v_path, t_path)
            engine.analyze_transcript(
                meeting_id=m_id,
                transcript_path=t_path,
                output_dir=paths['archive_dir'],
                mask_enabled=args.mask
            )

if __name__ == "__main__":
    main()
