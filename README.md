# City-Council-Meeting-Analyzer (V0.2.004)

A local-first, privacy-centric pipeline for analyzing City Council meetings. Designed for researchers and policy analysts who require high-performance AI tools without sacrificing data sovereignty.

## 🛡️ Privacy & Security Framework

This repository provides a framework for the confidential processing of PII. It is built to be **GDPR-Ready** and **NIST SP 800-122 Aligned**.

* **User-Controlled Minimization:** Pipeline processes audio locally; users choose whether to archive raw data or move it to secure storage.
* **Optional Pseudonymization:** Use the `--mask` flag to apply HMAC-SHA256 salted hashing to speaker names.
* **Semantic Data Flagging:** Masked reports are automatically prefixed with `anon_` to prevent accidental PII disclosure.
* **Operational Autonomy:** The analysis engine is designed to run 100% offline (air-gap capability) once media is ingested.

## 🚀 Quick Start

### 1. Installation
Ensure you are on Pop!_OS (or similar Linux) with NVIDIA drivers installed.
```bash
chmod +x setup.sh
./setup.sh
pip install faster-whisper openai pyyaml python-dotenv
