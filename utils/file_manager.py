# ****************************************************************************
# * *
# * City Council Meeting Analyzer                                            *
# * Version: 0.2.029                                                         *
# * Component: File Manager (Vault Discovery Logic)                          *
# * Author: joelontheroad                                                    *
# * *
# ****************************************************************************

import os
import glob
import shutil

class FileManager:
    def __init__(self, buffer_dir, vault_root):
        self.buffer_dir = buffer_dir
        self.vault_root = vault_root
        
        # Define flat vault structure
        self.vault_dirs = {
            "videos": os.path.join(self.vault_root, "videos"),
            "transcripts": os.path.join(self.vault_root, "transcripts"),
            "reports": os.path.join(self.vault_root, "reports")
        }
        
        # Ensure directories exist
        for d in self.vault_dirs.values():
            os.makedirs(d, exist_ok=True)

        self.force_skip_ids = [] 

    def get_pending_work(self, force=False):
        """Finds text in buffer OR videos in vault missing transcripts."""
        pending = []
        
        # 1. Check Buffer for ready-to-process transcripts
        buffer_transcripts = glob.glob(os.path.join(self.buffer_dir, "*.txt"))
        for ts_path in buffer_transcripts:
            base_id = os.path.basename(ts_path).replace(".txt", "")
            if base_id in self.force_skip_ids: continue
            
            report_path = os.path.join(self.vault_dirs["reports"], f"{base_id}_report.md")
            if force or not os.path.exists(report_path):
                pending.append({"id": base_id, "type": "summarize", "path": ts_path})

        # 2. Check Vault for videos that need transcription
        vault_videos = glob.glob(os.path.join(self.vault_dirs["videos"], "*.*"))
        for v_path in vault_videos:
            # Skip non-media files
            if v_path.lower().endswith(('.txt', '.md', '.json', '.yaml')): continue
            
            base_id = os.path.splitext(os.path.basename(v_path))[0]
            if base_id in self.force_skip_ids: continue
            
            ts_vault_path = os.path.join(self.vault_dirs["transcripts"], f"{base_id}.txt")
            
            # If transcript doesn't exist in vault, it's a 'transcribe' job
            if not os.path.exists(ts_vault_path):
                # Check if we are already summarizing it from the buffer
                if not any(item['id'] == base_id for item in pending):
                    pending.append({"id": base_id, "type": "transcribe_and_summarize", "path": v_path})
                
        return pending

    def move_to_vault(self, base_id, video_path):
        """Moves assets from staging to respective vault folders."""
        print(f"📦 Vaulting assets for: {base_id}")
        
        # Move Video (if it's in buffer; if it's already in vault/videos, skip)
        if video_path and os.path.exists(video_path):
            if self.vault_dirs["videos"] not in video_path:
                dest = os.path.join(self.vault_dirs["videos"], os.path.basename(video_path))
                if os.path.exists(dest): os.remove(dest)
                shutil.move(video_path, dest)
            
        # Move Transcript from buffer to vault/transcripts
        ts_src = os.path.join(self.buffer_dir, f"{base_id}.txt")
        if os.path.exists(ts_src):
            dest = os.path.join(self.vault_dirs["transcripts"], f"{base_id}.txt")
            if os.path.exists(dest): os.remove(dest)
            shutil.move(ts_src, dest)

    def save_report(self, filename, content):
        """Saves the final AI analysis to vault/reports."""
        target_path = os.path.join(self.vault_dirs["reports"], filename)
        with open(target_path, 'w') as f:
            f.write(content)
        print(f"💾 Report saved to Vault: {target_path}")
