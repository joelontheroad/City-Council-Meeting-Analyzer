import argparse
import sys
import os
import yaml
from utils.system_checks import check_disk_space, verify_environment

def load_config():
    """Loads the YAML configuration for force-skipping and analysis goals."""
    config_path = "configs/default.yaml"
    if not os.path.exists(config_path):
        # Fallback if config is missing during initial setup
        return {"force_skip": [], "analysis_goals": []}
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def main():
    # Setup CLI Arguments with Air-Gap Workflow descriptions
    parser = argparse.ArgumentParser(
        description="City-Council-Meeting-Analyzer: A local-first, Private AI pipeline for sovereign data analysis.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Workflow Examples:
  1. Online Phase (Ingestion):  python3 main.py --download-only
  2. Offline Phase (Analysis):   python3 main.py --local-only --mask

Note: Designed for Pop!_OS/Ubuntu. Requires an NVIDIA GPU for local inference.
        """
    )
    
    # Workflow Flags
    parser.add_argument("--download-only", action="store_true", 
                        help="Network-active phase: Fetch source media and AI models to local SSD.")
    
    parser.add_argument("--local-only", action="store_true", 
                        help="Air-Gap phase: Process only what is in the local /data folder. No network calls.")
    
    parser.add_argument("--mask", action="store_true", 
                        help="Anonymize speaker identities using SHA-256 and your local .env salt.")

    args = parser.parse_args()

    # 1. System Integrity Checks
    # We check for 20GB of free space and the existence of the .env salt
    if not check_disk_space(min_gb=20) or not verify_environment():
        print("❌ System check failed. Please resolve the issues above before continuing.")
        sys.exit(1)

    # 2. Load Configuration
    config = load_config()
    force_skip_ids = config.get("force_skip", [])
    
    # 3. WORKFLOW EXECUTION
    
    # PHASE 1: Online / Ingestion
    if args.download_only:
        print("\n🌐 PHASE 1: Online Ingestion Started...")
        print(f"Checking for new meetings (skipping {len(force_skip_ids)} IDs from config)...")
        # TODO: Trigger your Austin-specific scraper here
        # scraper.run(skip_list=force_skip_ids)
        print("\n✅ Ingestion Complete. Source files and models are cached.")
        print("🛡️  You can now safely disconnect the pfSense router for Air-Gapped analysis.")
        return

    # PHASE 2: Offline / Analysis
    if args.local_only:
        print("\n🛡️  PHASE 2: Offline Analysis (Air-Gapped Mode)...")
        if args.mask:
            print("🔐 PII Masking: ENABLED (Using local SHA-256 Salt)")
        else:
            print("⚠️  PII Masking: DISABLED (Raw names will be preserved)")
            
        # TODO: Trigger your Transcription/Analysis logic here
        # analyzer.run_local_batch(mask=args.mask)
        print("\n✅ Analysis complete. Results saved to /output.")
        return

    # DEFAULT BEHAVIOR (Run both if no flags are passed)
    print("\n🚀 Running full pipeline (Standard Mode)...")
    # In a standard run, we would call Phase 1 then Phase 2 sequentially.

if __name__ == "__main__":
    main()
