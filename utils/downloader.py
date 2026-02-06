# ****************************************************************************
# * *
# * City Council Meeting Analyzer                                            *
# * Version: 0.2.008                                                         *
# * Component: Audio-First Downloader                                        *
# * Author: joelontheroad                                                    *
# * *
# ****************************************************************************

import os
import yt_dlp

class CityCouncilDownloader:
    def __init__(self, staging_dir="temp_buffer"):
        self.staging_dir = staging_dir
        if not os.path.exists(self.staging_dir):
            os.makedirs(self.staging_dir)

    def download_video(self, url, target_filename, mode="audio"):
        """
        Downloads media based on requested mode. 
        Checks for existing file first to allow for rapid re-analysis.
        """
        output_path = os.path.join(self.staging_dir, target_filename)

        # 🛑 THE "GOLDEN RULE" CHECK
        if os.path.exists(output_path):
            # We don't return None; we return the path so the Orchestrator 
            # knows it can proceed straight to analysis/transcription.
            print(f"📦 Resource already exists locally: {target_filename}")
            return output_path

        print(f"📡 Requesting {mode} stream for: {url}...")

        # yt-dlp configuration based on mode
        ydl_opts = {
            'outtmpl': output_path,
            'quiet': True,
            'no_warnings': True,
        }

        if mode == "audio":
            # Target high-quality M4A for faster AI processing
            ydl_opts['format'] = 'bestaudio[ext=m4a]/bestaudio/best'
        elif mode == "video":
            # Standard MP4
            ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
        elif mode == "highquality":
            # Maximum resolution (may require ffmpeg merge)
            ydl_opts['format'] = 'bestvideo+bestaudio/best'

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            if os.path.exists(output_path):
                print(f"✅ Download Complete: {output_path}")
                return output_path
            return None
            
        except Exception as e:
            print(f"❌ Download Failed: {e}")
            return None
