import argparse
import sys
import yaml
from utils.system_checks import check_disk_space, verify_environment

def load_config():
    with open("configs/default.yaml", "r") as f:
        return yaml.safe_load(f)

def main():
    # Setup CLI Arguments
    parser = argparse.ArgumentParser(description="City-Council-Meeting-Analyzer: Private AI Pipeline")
    parser.add_argument("--download-only", action="store_true", help="Online Phase: Fetch video/audio and exit.")
    parser.add_argument("--local-only", action="store_true", help="Offline Phase: Process local cache only (Air-Gap mode).")
    parser.add_argument("--mask", action="store_true", help="Enable SHA-256 salted pseudonymization.")
    args = parser.parse_args()

    # Load configuration (Force Skip IDs, etc)
    config = load_config()
    force_skip_ids = config.get("force_skip", [])

    # Run System Integrity Checks
    if not check_disk_space() or not verify_environment():
        sys.exit(1)

    # WORKFLOW LOGIC
    if args.download_only:
        print("🌐 PHASE 1: Online Ingestion Started...")
        # Your Scraper Logic here
        # Example: download_from_austin(skip_list=force_skip_ids)
        print("✅ Ingestion Complete. It is now safe to disconnect your pfSense router.")
        return

    if args.local_only:
        print("🛡️ PHASE 2: Offline Analysis (Air-Gapped Mode)...")
        # Your Analysis Logic here
        # Example: transcribe_local_files(mask=args.mask)
        return

    # Default: Run everything sequentially
    print("🚀 Running full pipeline (Standard Mode)...")

if __name__ == "__main__":
    main()
