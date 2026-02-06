# 🏛️ City Council Meeting Analyzer
**Version 0.2.006**

An AI-powered tool designed to download, transcribe, and analyze city council meetings. 

## 🚀 Key Philosophy: Audio-First
To maximize processing speed and minimize bandwidth, this tool defaults to **Audio-Only** processing. It targets high-quality M4A streams which are ~90% smaller than video files but perfect for AI transcription.

## 🛠️ Installation
1. Ensure you have `ffmpeg` and `yt-dlp` installed on your system.
2. Install Python dependencies:
   ```bash
   pip install yt-dlp faster-whisper
   ```

## 💻 Usage
### Basic (Audio-Only)
```bash
python main.py --url "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

### Video Modes
- `--video`: Downloads a standard MP4 file.
- `--highqualityvideo`: Downloads the best available resolution (requires ffmpeg for merging).

### Forced Audio
- `--audio`: Explicitly requests audio-only (redundant but available).

## 🔌 Plugin Architecture (Adding Jurisdictions)
This tool uses a dynamic discovery system. To add a new city:
1. Create a new `.py` file in the `jurisdictions/` folder.
2. Implement the `Connector` class with the following methods:
   - `can_handle(url)`: Returns True if the URL belongs to that city.
   - `get_standardized_filename(url, mode)`: Returns the output filename.

The system will automatically detect and use your new connector.

## 📁 Project Structure
- `main.py`: The orchestrator.
- `jurisdictions/`: Plug-and-play city connectors.
- `utils/`: Core logic for downloading and AI processing.
- `temp_buffer/`: Staging area for active downloads.
