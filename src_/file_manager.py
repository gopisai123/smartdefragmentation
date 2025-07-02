# src_/file_manager.py
# import os
# def allocate_file_to_memory(memory, file_name, size):
#     """Allocate a file to memory, used during file creation."""
#     for i in range(len(memory) - size + 1):
#         if all(memory[i + j] == 0 for j in range(size)):  # Check if all blocks are empty
#             memory[i:i + size] = [file_name] * size  # Store the actual file name in memory
#             return True
#     return False



import os
import queue
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileEventHandler(FileSystemEventHandler):
    def __init__(self, event_queue):
        self.event_queue = event_queue
    
    def on_created(self, event):
        if not event.is_directory:
            self.event_queue.put(('create', os.path.basename(event.src_path)))
    
    def on_deleted(self, event):
        if not event.is_directory:
            self.event_queue.put(('delete', os.path.basename(event.src_path)))

def start_file_watcher(folder_path, event_queue):
    """Initialize file system watcher"""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    event_handler = FileEventHandler(event_queue)
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=False)
    observer.start()
    return observer

def preload_memory(folder_path, memory):
    """Load existing files into memory"""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    files = sorted(os.listdir(folder_path))
    for i, filename in enumerate(files):
        if i < len(memory):
            memory[i]['content'] = filename
            memory[i]['size'] = 1  # Default size for preloaded files