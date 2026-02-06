# ****************************************************************************
# * *
# * City Council Meeting Analyzer                                            *
# * Version: 0.2.006                                                         *
# * Jurisdiction: Austin, TX (Swagit Connector)                              *
# * Author: joelontheroad                                                    *
# * *
# ****************************************************************************

import os

class Connector:
    def __init__(self):
        self.name = "Austin, TX"
        self.domain_hint = "austintx.new.swagit.com"

    def can_handle(self, url):
        """Claims the URL if it belongs to Austin's Swagit portal."""
        return self.domain_hint in url

    def resolve_video_id(self, url):
        """Extracts the unique Swagit ID from the URL."""
        parts = url.strip("/").split("/")
        if "videos" in parts:
            idx = parts.index("videos")
            if len(parts) > idx + 1:
                return parts[idx + 1]
        return "unknown_meeting"

    def get_standardized_filename(self, url, mode="audio"):
        """Standardized name based on the ID and requested media mode."""
        meeting_id = self.resolve_video_id(url)
        extension = "m4a" if mode == "audio" else "mp4"
        return f"austin_meeting_{meeting_id}.{extension}"
