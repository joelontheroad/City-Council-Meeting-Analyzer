# City-Council-Meeting-Analyzer (V0.2.004)
**Author:** Joel Greenberg ([joelontheroad](https://github.com/joelontheroad))

A secure, local-first AI pipeline for transcribing and analyzing city council meetings. I developed this program to analyze the intent of public speakers addressing the Austin, TX City Council during regular meetings as they commented on a contentious issue. 

## 🔒 Private AI Intent
This project serves as a reference implementation for **Private AI**. I designed this tool to prove that local government transparency does not have to come at the cost of resident privacy. 

Unlike traditional transcription services that require uploading sensitive local data to the cloud, this pipeline ensures:
* **Zero Cloud Leakage:** No audio, video, or text data is sent to external APIs (OpenAI, Google, etc.). All transcription and analysis are performed locally.
* **Data Sovereignty:** You maintain your own archive of council proceedings. The program is designed to download data **once**, allowing for multiple analysis passes on the local copy without further network requests.

## ✨ Features
* **Local-First Architecture:** The program runs entirely on **Pop!_OS / Ubuntu**, keeping data on your local hardware.
* **Configurable Analysis:** The logic is configurable via YAML files, allowing the program to be tuned to look for different specific issues or keywords within a meeting.
* **Modular Connectors:** Video downloading is modular. While only one connector is currently included, the program is designed to pull from various video archives using custom connectors.
* **Salted Pseudonymization:** I have implemented deterministic masking of speaker identities using SHA-256 salted hashing (GDPR Article 25 - Privacy by Design).
* **Force-Skip Control:** I included a "Force Skip" flag in `configs/default.yaml` to manually ignore specific meeting IDs, saving processing time.
* **Environment Integrity:** A built-in diagnostic tool verifies hardware acceleration (CUDA) and dependency health.

## 🚀 Quick Start
1. **Clone the repo:**
   `git clone https://github.com/joelontheroad/City-Council-Meeting-Analyzer.git`
2. **Run the hardened installer:**
   `chmod +x setup.sh && ./setup.sh`
3. **Execute the program:**
   `python3 main.py`

## 💻 Usage & Command Line Examples
For a full list of available flags and parameters, run:
`python3 main.py --help`

* **Standard Pass:**
  `python3 main.py`
* **Masked Export (PII Protection):**
  `python3 main.py --mask`

## 🖥️ Hardware Requirements
To maintain privacy without sacrificing performance, the following hardware is recommended:
* **OS:** Pop!_OS / Ubuntu 22.04+
* **GPU:** NVIDIA GPU with 8GB+ VRAM (for CUDA acceleration).
* **RAM:** 16GB Minimum.
* **Storage:** SSD for handling video/audio meeting archives.

## ⚖️ License
Distributed under the MIT License. See `LICENSE` for more information.
