# ****************************************************************************
# * *
# * City Council Meeting Analyzer                                           *
# * Version: 0.2.004                                                        *
# * Author: joelontheroad                                                   *
# * License: As-Is / Experimental                                           *
# * *
# ****************************************************************************

import argparse
import os
import sys
from utils.config_loader import get_paths
from utils.privacy_manager import PrivacyManager
from utils.downloader import CityCouncilDownloader
from utils.processor import MeetingProcessor

def main():
    parser = argparse.ArgumentParser(description="Analyze City Council Meetings for Austin, TX.")
    
    # Input group: URL or File
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("--url", type=str, help="Single Swagit video URL to analyze")
    input_group.add_argument("--file", type=str, help="Text file containing a list of URLs")
    
    # Flags
    parser.add_argument("--mask", action="store_true", help="Enable NIST-compliant speaker anonymization")
    parser.add_argument("--keywords", type=str, help="Comma-separated list of topics to highlight in summary")
    
    args = parser.parse_args()

    # 1. Load Environment & Paths
    try:
        paths = get_paths()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # 2. Initialize Components
    privacy = PrivacyManager() if args.mask else None
    downloader = CityCouncilDownloader(staging_path=paths['staging'], vault_path=paths['vault'])
    processor = MeetingProcessor(vault_path=paths['vault'], keywords=args.keywords)

    # 3. Handle Input
    urls = []
    if args.url:
        urls.append(args.url)
    elif args.file:
        if os.path.exists(args.file):
            with open(args.file, 'r') as f:
                urls = [line.strip() for line in f if line.strip()]
        else:
            print(f"Error: Input file {args.file} not found.")
            sys.exit(1)

    # 4. Processing Loop
    print(f"--- Starting analysis on {len(urls)} meeting(s) ---")
    for url in urls:
        print(f"\nTarget: {url}")
        
        # Smart Check: Is it already in the vault?
        video_path = downloader.check_vault(url)
        
        if not video_path:
            print("Action: Video not found in vault. Starting download...")
            video_path = downloader.run(url)
        else:
            print("Action: Video found in vault. Skipping download.")

        # AI Analysis Phase
        if video_path:
            transcript = processor.transcribe(video_path)
            
            if args.mask:
                print("Action: Applying privacy masks to speaker names...")
                transcript = privacy.anonymize_transcript(transcript)
            
            summary = processor.summarize(transcript)
            processor.save_results(url, transcript, summary)
            print("Success: Analysis complete.")
        else:
            print(f"Failed: Could not retrieve video for {url}")

    print("\n--- All tasks completed ---")

if __name__ == "__main__":
    main()
