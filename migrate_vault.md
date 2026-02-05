# """
# Project: City-Council-Meeting-Analyzer
# Version: V0.2.004
# Security: NIST-Aligned Privacy Protection
# Principles: NIST SP 800-122 Aligned (Salted Pseudonymization & Operational Autonomy)
# """

# 📦 Data Migration Guide: V0.1 -> V0.2.004

This guide handles the transition of your historical data (October 2023–Present) into the new tiered storage architecture.

## 📋 Instructions
1. Ensure your RAID 6 drive is mounted and recognized by the VM.
2. Ensure you have already run `python3 configure_paths.py` to set up your `default.yaml`.
3. Open `ingest_legacy.py` and update the `LEGACY_SOURCE` variable with the path to your old data.
4. Run the script:
   ```bash
   python3 ingest_legacy.py
   ```

## ✅ What this does
- Moves `.mp4` files to `[vault_path]/raw_video`
- Moves `.txt` files to `[vault_path]/transcripts`
- Clears the processing buffer to ensure a clean start for the new V0.2.004 logic.
