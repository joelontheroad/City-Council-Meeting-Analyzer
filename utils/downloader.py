# ****************************************************************************
# * *
# * City Council Meeting Analyzer                                           *
# * Version: 0.2.004                                                        *
# * Author: joelontheroad                                                   *
# * License: As-Is / Experimental                                           *
# * *
# ****************************************************************************

import os
import subprocess
import requests
import shutil
from utils import config_loader

def get_video_id(url):
    """
    Extracts the unique ID from a Swagit URL.
    Example: .../videos/300507/0/ -> 300507
    """
    parts = url.strip("/").split("/")
    return parts[-2] if "videos" in parts else "unknown_video"

def download_and_stitch(url):
    """
    Handles the heavy lifting of the 'Tiered Storage' process.
    """
    paths = config_loader.get_paths()
    staging_dir = os.path.join(paths['staging_buffer'], "temp_chunks/")
    vault_dir = paths['permanent_vault']
    
    video_id = get_video_id(url)
    final_filename = f"{video_id}.mp4"
    final_path = os.path.join(vault_dir, final_filename)

    # 1. Create staging area
    if not os.path.exists(staging_dir):
        os.makedirs(staging_dir)

    print(f"🏗️  Staging download in: {staging_dir}")

    # 2. Logic to fetch m3u8 playlist and segments
    # (Note: In a real implementation, we'd use 'yt-dlp' or 'ffmpeg' directly here)
    # This is a wrapper for the ffmpeg command that handles the HLS stitching
    try:
        print("🧵 Stitching segments via ffmpeg...")
        # ffmpeg merges segments into a single MP4. 
        # We target the staging buffer first.
        temp_output = os.path.join(staging_dir, final_filename)
        
        # Swagit uses HLS (.m3u8). ffmpeg can ingest the URL directly.
        # We use -c copy to avoid re-encoding (preserving quality & speed)
        cmd = [
            'ffmpeg', '-i', url, '-c', 'copy', '-bsf:a', 'aac_adtstoasc', 
            '-y', temp_output
        ]
        
        # This would be a subprocess call in production
        # subprocess.run(cmd, check=True)

        # 3. Move to Permanent Vault
        print(f"🚚 Moving finalized video to Vault: {final_path}")
        shutil.move(temp_output, final_path)

        # 4. Cleanup
        print("🧹 Cleaning up staging
