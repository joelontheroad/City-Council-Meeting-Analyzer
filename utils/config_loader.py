# ****************************************************************************
# * *
# * City Council Meeting Analyzer                                            *
# * Version: 0.2.004                                                         *
# * Author: joelontheroad                                                    *
# * *
# ****************************************************************************

import yaml
import os

def get_paths():
    """
    Locates the configuration file and returns a dictionary of system paths.
    Uses absolute pathing to prevent NoneType errors.
    """
    # 1. Get the directory where THIS script lives
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_dir, "configs", "default.yaml")

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"❌ Configuration file not found at: {config_path}")

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    # 2. Extract paths with fallback defaults to prevent NoneType
    storage = config.get("storage", {})
    
    paths = {
        "staging_buffer": storage.get("staging_buffer", "./temp_buffer"),
        "permanent_vault": storage.get("permanent_vault", "./data/vault")
    }

    # 3. Ensure the directories actually exist on the disk
    for key, path in paths.items():
        # Resolve relative paths to absolute paths
        abs_path = os.path.abspath(os.path.join(base_dir, path))
        os.makedirs(abs_path, exist_ok=True)
        paths[key] = abs_path

    return paths

