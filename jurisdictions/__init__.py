# ****************************************************************************
# * *
# * City Council Meeting Analyzer                                            *
# * Component: Dynamic Connector Loader                                      *
# * Author: joelontheroad                                                    *
# * *
# ****************************************************************************

import os
import importlib
import inspect

def get_connector(url):
    """
    Scans all .py files in this directory to find a Connector class
    that can handle the provided URL.
    """
    current_dir = os.path.dirname(__file__)
    
    for filename in os.listdir(current_dir):
        # Skip init files, non-python files, and hidden files
        if filename.startswith("_") or not filename.endswith(".py"):
            continue
            
        module_name = f"jurisdictions.{filename[:-3]}"
        try:
            module = importlib.import_module(module_name)
            
            # Look for a class named 'Connector' in the module
            if hasattr(module, "Connector"):
                connector_class = getattr(module, "Connector")
                
                # Instantiate and check if it can handle the URL
                instance = connector_class()
                if instance.can_handle(url):
                    return instance
        except Exception as e:
            print(f"⚠️ Error loading connector from {filename}: {e}")
            
    return None

