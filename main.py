# ****************************************************************************
# * *
# * City Council Meeting Analyzer                                            *
# * Version: 0.2.008 (Restored)                                              *
# * Component: Main Orchestrator                                             *
# * Author: joelontheroad                                                    *
# * *
# ****************************************************************************

import argparse
import os
import sys
from utils.config_loader import get_paths
from utils.downloader import CityCouncilDownloader
from utils.processor import MeetingProcessor
from jurisdictions import get_connector

def main():
    parser = argparse.ArgumentParser(
        description="Analyze City Council Meetings. Automatically skips downloads if files exist.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("--url", type=str, help="URL to analyze")
    input_group.add_argument("--file", type=str, help="Text file containing a list of URLs")
    
    parser.add_argument("--mask", action="store_true", help="Enable GDPR masking in report")
    parser.add_argument("--video", action="store_true", help="Download video instead of default audio")
    
    args = parser.parse_args()
    paths = get_paths()
    
    downloader = CityCouncilDownloader(staging_dir=paths['staging_buffer'])
    processor = MeetingProcessor()

    urls = [args.url] if args.url else []
    if args.file and os.path.exists(args.file):
        with open(args.file, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]

    for url in urls:
        connector = get_connector(url)
        if not connector:
            print(f"⚠️  No connector for: {url}")
            continue

        # Use the connector to determine the filename
        mode = "video" if args.video else "audio"
        target_name = connector.get_standardized_filename(url, mode=mode)
        expected_path = os.path.join(paths['staging_buffer'], target_name)

        # THE RESTORED LOGIC: Check disk before doing anything
        if os.path.exists(expected_path):
            print(f"♻️  Local file found: {target_name}. Skipping download/transcription.")
            final_media_path = expected_path
        else:
            print(f"🚀 File not found. Initiating {mode} download for {connector.name}...")
            final_media_path = downloader.download_video(url, target_filename=target_name, mode=mode)

        if final_media_path:
            # We assume transcription is handled or already cached in a .txt file
            # For this analysis sprint, we pass the content to LMStudio
            with open(final_media_path, 'r', errors='ignore') as f:
                content = f.read()
            
            report = processor.process(content, mask=args.mask)
            print(f"\n--- ANALYSIS REPORT ---\n{report}\n")

if __name__ == "__main__":
    main()
