# ****************************************************************************
# * *
# * City Council Meeting Analyzer                                           *
# * Version: 0.2.004                                                        *
# * Author: joelontheroad                                                   *
# * License: As-Is / Experimental                                           *
# * *
# ****************************************************************************

# City Council Meeting Analyzer (V0.2.004)

## 📖 Overview
The **City Council Meeting Analyzer** is a configurable, private, AI-powered tool built to transcribe municipal meeting videos, summarize public testimony, and report on speaker sentiment.

### 🛡️ Privacy & Security by Design
Designed with **Security by Design** principles and inspired by **GDPR** and **NIST 800-122** specifications, this tool prioritizes local-first processing. To protect civil liberties, the system allows you to mask the names of speakers, enabling you to distribute findings while maintaining participant anonymity.

### 🧠 Intelligent Analysis
* **Modular Connectors:** Currently optimized for Austin City Council (Winter 2026).
* **Smart Re-analysis:** If a video is already in your vault, the program skips the download and moves straight to AI analysis.
* **Keywords:** Refine AI summaries by providing specific topics of interest.

---

## 🚀 Installation & Setup

### 1. Project Prep
```bash
git clone [https://github.com/joelontheroad/City-Council-Meeting-Analyzer.git](https://github.com/joelontheroad/City-Council-Meeting-Analyzer.git) .
chmod +x setup.sh
./setup.sh
```

### 2. Privacy Key (Essential for Masking)
The program uses a secret "salt" to generate consistent pseudonyms for speakers.
```bash
echo "PSEUDO_SALT=$(openssl rand -hex 32)" > .env
```

### 3. Storage Configuration
```bash
source venv/bin/activate
python3 configure_paths.py
```

#### 📂 Understanding the Two Paths
The script will ask for two distinct locations to optimize performance:
1.  **The Staging Buffer (Local Storage):** Used for downloading and "stitching" video chunks. Using your local disk (OS drive) is much faster than a network drive for this task.
2.  **The Permanent Vault (Large Storage):** Where the final .mp4 and transcripts are stored for AI analysis. Use your high-capacity drive here (e.g., /mnt/media-drive/).

---

## 🔌 Activate the Environment
Before running the analyzer, you must activate the virtual environment:
```bash
source venv/bin/activate
```
*(Type deactivate when you are finished to return to your normal terminal.)*

---

## 🎬 First Run: Analyze a Meeting

### Option A: Analyze a single URL
Run this to test the system with a live Austin meeting. **Note:** Do not use brackets or quotes around the URL.
```bash
python3 main.py --url [https://austintx.new.swagit.com/videos/300507/0/](https://austintx.new.swagit.com/videos/300507/0/) --mask
```

### Option B: Batch analysis
Create a text file (e.g., meetings.txt) with one URL per line. Do not include brackets, commas, or quotes in the file.
```bash
python3 main.py --file meetings.txt --mask
```

> [!TIP]
> **Smart Detection:** If you have already downloaded the video, simply ensure the .mp4 is in your vault/raw_video/ folder. The program will skip the download and go straight to work.

---

## ❓ Getting Help
To see all available command-line flags, including keyword filtering options:
```bash
python3 main.py --help
```
