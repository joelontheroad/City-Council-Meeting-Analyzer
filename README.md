# """
# Project: City-Council-Meeting-Analyzer
# Version: V0.2.004
# Security: NIST-Aligned Privacy Protection
# Principles: NIST SP 800-122 Aligned (Salted Pseudonymization & Operational Autonomy)
# """

# City-Council-Meeting-Analyzer (V0.2.004)

A privacy-first, local-only pipeline for analyzing city council meetings. This project uses salted HMAC pseudonymization to protect PII while leveraging local NVIDIA GPUs for transcription and intent analysis.

## 🛡️ Privacy & Compliance (NIST 800-122)
This project is built on the principle of **Operational Autonomy**. 
- **No Cloud PII:** All transcripts and raw videos remain on local or private network storage (RAID).
- **Salted Masking:** Personal names are transformed into consistent hex-IDs using a local secret salt.
- **Git Safety:** Sensitive configuration (`.env`) and data directories are strictly excluded from version control via `.gitignore`.

## 💾 Tiered Storage Architecture
To handle massive video files (12GB+) in a virtualized environment (Proxmox), the system uses a dual-tier storage strategy:
1. **RAID 1 Buffer (Fast):** Used for initial downloads and `ffmpeg` fixups to maximize I/O speed.
2. **RAID 6 Vault (Archival):** Used for long-term storage of MP4s and generated transcripts.

## 🚀 Getting Started

### Prerequisites
- **OS:** Ubuntu / Pop!_OS (Optimized for NVIDIA/CUDA)
- **Hardware:** NVIDIA GPU (12GB+ VRAM recommended)
- **Software:** FFmpeg, Python 3.10+, CUDA Toolkit

### Installation (The "Dog Food" Run)
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/joelontheroad/City-Council-Meeting-Analyzer.git](https://github.com/joelontheroad/City-Council-Meeting-Analyzer.git)
   cd City-Council-Meeting-Analyzer
   ```
2. **Run the setup script:**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```
3. **Configure your Environment:**
   Create a `.env` file in the root directory and add your secret salt:
   ```text
   PSEUDO_SALT=your_random_string_here
   ```

## ⚙️ Configuration (`configs/default.yaml`)
You can tune the system performance by adjusting the YAML:
- `buffer_path`: Point this to your fast VM disk (RAID 1).
- `vault_path`: Point this to your high-capacity mount (RAID 6).
- `model_size`: Default is `medium` to ensure stability on 12GB GPUs.
- `force_skip`: Add meeting IDs here to blacklist them from processing.

## 🛠️ Usage
- **Full Run:** `python3 main.py`
- **Download Only:** `python3 main.py --download-only`
- **Re-Analyze Historical Data:** `python3 main.py --local-only`
  *(Note: This skips transcription if a .txt file already exists in the Vault)*
