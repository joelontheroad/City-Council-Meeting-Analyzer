# ****************************************************************************
# * *
# * City Council Meeting Analyzer                                           *
# * Version: 0.2.004                                                        *
# * Author: joelontheroad                                                   *
# * License: As-Is / Experimental                                           *
# * *
# ****************************************************************************

import yaml
import os

def get_paths(config_path='configs/default.yaml'):
    """
    Reads the staging and vault paths from the YAML configuration.
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found at {config_path}. Run configure_paths.py first.")
        
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
        
    paths = {
        'staging': config.get('staging_buffer'),
        'vault': config.get('permanent_vault')
    }
    
    # Ensure standard subdirectories exist in the vault
    # This keeps your raw data and AI outputs organized
    subdirs = ['raw_video', 'transcripts', 'summaries']
    for subdir in subdirs:
        full_path = os.path.join(paths['vault'], subdir)
        if not os.path.exists(full_path):
            os.makedirs(full_path)
            
    return paths
