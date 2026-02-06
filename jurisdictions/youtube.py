# ****************************************************************************
# * *
# * City Council Meeting Analyzer                                            *
# * Version: 0.2.006                                                         *
# * Component: YouTube Jurisdiction Plugin                                   *
# * Author: joelontheroad                                                    *
# * *
# ****************************************************************************

import re

class Connector:
    def __init__(self):
        self.name = "YouTube (Generic)"
        # Regex to capture the 11-character YouTube ID from various URL formats
        # Supports: watch?v=, shorts/, youtu.be/, and embed/
        self.yt_regex = r"(?:v=|\/shorts\/|embed\/|youtu\.be\/)([A-Za-z0-9_-]{11})"

    def can_handle(self, url):
        """Claims the URL if it contains YouTube domain signatures."""
        return "youtube.com" in url or "youtu.be" in url

    def get_standardized_filename(self, url, mode="audio"):
        """
        Parses the Video ID and applies the correct extension.
        Defaults to .m4a for the product manager's audio-first requirement.
        """
        match = re.search(self.yt_regex, url)
        video_id = match.group(1) if match else "unknown_yt_video"
        
        extension = "m4a" if mode == "audio" else "mp4"
        return f"youtube_{video_id}.{extension}"
