# ****************************************************************************
# * *
# * City Council Meeting Analyzer                                            *
# * Version: 0.2.004                                                         *
# * Author: joelontheroad                                                    *
# * License: As-Is / Experimental                                            *
# * *
# ****************************************************************************

import os
import gc
import torch

def clear_memory():
    """
    Forces garbage collection and clears the CUDA cache to prevent 
    memory leaks during long batch processes.
    """
    print("🧹 System Check: Clearing memory...")
    
    # Force Python's garbage collector
    gc.collect()
    
    # Clear NVIDIA VRAM if a GPU is being used
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    
    return True

def check_system_requirements():
    """Verifies that external tools like ffmpeg are installed."""
    # Logic for checking ffmpeg exists
    ffmpeg_check = os.system("ffmpeg -version > /dev/null 2>&1")
    if ffmpeg_check == 0:
        print("✅ FFmpeg is installed.")
        return True
    else:
        print("❌ FFmpeg not found. Please install ffmpeg.")
        return False

if __name__ == "__main__":
    check_system_requirements()

