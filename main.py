# ****************************************************************************
# * *
# * City Council Meeting Analyzer                                            *
# * Version: 0.2.031                                                         *
# * Component: Main Orchestrator (With Progress Tracking)                     *
# * Author: joelontheroad                                                    *
# * *
# ****************************************************************************

import argparse
import os
import glob
from utils.config_loader import get_paths
from utils.downloader import CityCouncilDownloader
from utils.processor import MeetingProcessor
from utils.transcriber import MeetingTranscriber
from utils.file_manager import FileManager
from jurisdictions import get_connector

def find_existing_video(buffer_dir, base_filename):
    name_without_ext = os.path.splitext(base_filename)[0]
    pattern = os.path.join(buffer_dir, f"{name_without_ext}.*")
    matches = glob.glob(pattern)
    video_matches = [m for m in matches if not m.endswith(('.txt', '.json'))]
    return video_matches[0] if video_matches else None

def process_single_meeting(transcript_data, processor, file_manager, mask, video_path):
    source_name = transcript_data['id']
    print(f"  └─ 🧠 AI Analysis in progress...")
    
    with open(transcript_data['transcript_path'], 'r') as f:
        raw_text = f.read().strip()

    if len(raw_text) > 100:
        report = processor.process(raw_text, mask=mask, source_name=source_name)
        file_manager.save_report(os.path.basename(transcript_data['report_path']), report)
        file_manager.move_to_vault(source_name, video_path)
    else:
        print(f"  ⚠️ Transcript too short for {source_name}. Skipping.")

def main():
    parser = argparse.ArgumentParser(description="Analyze City Council Meetings.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--url", type=str, help="Analyze a specific URL")
    group.add_argument("--summarize-all", action="store_true", help="Process all pending work")
    
    parser.add_argument("--force", action="store_true", help="Force overwrite/re-process")
    parser.add_argument("--mask", action="store_true", help="Enable PII masking")
    
    args = parser.parse_args()
    paths = get_paths()
    
    file_manager = FileManager(buffer_dir=paths['staging_buffer'], vault_root=paths['permanent_vault'])
    transcriber = MeetingTranscriber(model_size="medium")
    processor = MeetingProcessor()
    
    if args.summarize_all:
        work_queue = file_manager.get_pending_work(force=args.force)
        
        if not work_queue:
            print("\n📭 No pending work found in buffer or vault.")
            return

        total_jobs = len(work_queue)
        print(f"\n🚀 BATCH START: Processing {total_jobs} meetings")
        print("="*60)

        for index, job in enumerate(work_queue, 1):
            print(f"\n[Job {index}/{total_jobs}] ID: {job['id']}")
            
            t_path = ""
            v_path = ""
            
            if job['type'] == "transcribe_and_summarize":
                print(f"  └─ 🎙️ Transcribing audio/video from Vault...")
                v_path = job['path']
                raw_text = transcriber.transcribe(v_path)
                t_path = os.path.join(paths['staging_buffer'], f"{job['id']}.txt")
                with open(t_path, 'w') as f: f.write(raw_text)
            else:
                print(f"  └─ 📄 Using existing transcript found in Buffer.")
                t_path = job['path']
                v_path = find_existing_video(paths['staging_buffer'], job['id'])

            r_name = f"{job['id']}_report.md"
            process_single_meeting({
                "transcript_path": t_path, 
                "report_path": r_name, 
                "id": job['id']
            }, processor, file_manager, args.mask, v_path)

        print("\n" + "="*60)
        print("🏁 BATCH COMPLETE: All items vaulted.")

    elif args.url:
        # URL Logic...
        pass

if __name__ == "__main__":
    main()
