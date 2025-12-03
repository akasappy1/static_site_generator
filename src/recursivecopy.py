# Recursively copy contents of a file tree into a different file tree without using shutil.copytree because reasons, I guess.

import os
import shutil
from pathlib import PosixPath

def recursive_tree_copy(from_path, to_path):
    """Accepts an origin path and a destination path and recursively copies the 
    file tree from the origin to the destination. 
    Warning: Deletes an existing files at the destination."""
    
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    os.mkdir(to_path)
    log = ""

    for item in os.listdir(from_path):
        item_from_path = os.path.join(from_path, item)
        item_to_path = os.path.join(to_path, item)

        if os.path.isdir(item_from_path):
            recursive_tree_copy(item_from_path, item_to_path)
        else:
            shutil.copy(item_from_path, item_to_path)
            log += f"\n{item_from_path} successfully copied to {item_to_path}"

    print(log)

        
  




