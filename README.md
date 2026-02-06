# 🏛️ City Council Meeting Analyzer

An automated pipeline to download, transcribe, and analyze local government meetings using OpenAI Whisper and Local LLMs (via LM Studio).

## 🚀 Quick Start

1. **Analyze a Single Meeting** (Download + Transcribe + Summarize):
   `python3 main.py --url <URL>`

2. **Batch Process Everything** (Summarize all transcripts in buffer):
   `python3 main.py --summarize-all`

## 🛠️ Configuration & Customization

### 1. Analysis Focus (`configs/prompts.json`)
You can change what the AI looks for by editing the `analysis_focus` in the prompts file.
* **Default:** Zoning, infrastructure, and public safety.
* **Example:** Change to "Focus on environmental policy and public park funding."

### 2. Manual Skip (`utils/file_manager.py`)
If a specific meeting ID is corrupted or should be ignored, add it to the `self.force_skip_ids` list in the FileManager.

### 3. Masking
Use the `--mask` flag to trigger GDPR/PII masking logic (requires configuration in `processor.py`).

## 📁 Project Structure
* `temp_buffer/`: Raw media files and `.txt` transcripts.
* `reports/`: Final AI-generated analysis in Markdown format.
* `jurisdictions/`: Modular connectors for different city websites (Swagit, YouTube, etc.).
* `configs/`: Centralized prompts and settings.

## ⚙️ Requirements
* **Python 3.10+**
* **FFmpeg** (Required for Whisper audio processing)
* **LM Studio** (Running a local server at `http://localhost:1234`)
