# def predict_allocation(memory, history):
#     # Simple heuristic: allocate at the end of the last allocated block
#     last_allocated_index = len(memory) - 1
#     while last_allocated_index >= 0 and memory[last_allocated_index] is None:
#         last_allocated_index -= 1
#     return last_allocated_index + 1



# src/predictive_allocation.py

# import os

# def predict_allocation(memory_folder):
#     # Check if the memory_folder exists
#     if not os.path.exists(memory_folder):
#         print(f"Error: The folder '{memory_folder}' does not exist.")
#         return 0
    
#     # Get all files in the MemoryBlocks folder
#     files = os.listdir(memory_folder)
    
#     # Filter out directories (if any) and only keep files
#     files = [f for f in files if os.path.isfile(os.path.join(memory_folder, f))]
    
#     # If there are no files, return the first index for allocation
#     if not files:
#         return 0
    
#     # Return the next index as the number of files
#     return len(files)+1

# # Example usage
# memory_folder = r"E:\SmartMemoryDefragmenter\MemoryBlocks"  # Use raw string for Windows paths
# next_index = predict_allocation(memory_folder)
# print(f"The next allocation index is: {next_index}")


import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Memory allocation settings
BASE_MEMORY_ADDRESS = 0x1000  # Starting memory address
BLOCK_SIZE = 4  # Size of each memory block in bytes

# Function to calculate the next memory address
def calculate_next_address(memory_folder):
    # Get all files in the MemoryBlocks folder
    files = os.listdir(memory_folder)
    print(f"Files in folder: {files}")  # Debug: Print all files
    
    # Filter out directories (if any) and only keep files
    files = [f for f in files if os.path.isfile(os.path.join(memory_folder, f))]
    print(f"Filtered files: {files}")  # Debug: Print filtered files
    
    # If there are no files, return the base memory address
    if not files:
        return hex(BASE_MEMORY_ADDRESS)
    
    # Calculate the next memory address
    next_address = BASE_MEMORY_ADDRESS + len(files) * BLOCK_SIZE
    print(f"Next memory address calculated: {hex(next_address)}")  # Debug: Print calculated address
    return hex(next_address)

# Event handler for file system changes
class MemoryFolderHandler(FileSystemEventHandler):
    def __init__(self, memory_folder):
        self.memory_folder = memory_folder
    
    def on_created(self, event):
        # When a new file is created, calculate and print the next memory address
        if not event.is_directory:
            print(f"New file detected: {event.src_path}")  # Debug: Print detected file
            next_address = calculate_next_address(self.memory_folder)
            print(f"Next memory address: {next_address}")  # Debug: Print next address

# Main function to monitor the folder in real-time
def monitor_memory_folder(memory_folder):
    # Create an event handler and observer
    event_handler = MemoryFolderHandler(memory_folder)
    observer = Observer()
    observer.schedule(event_handler, path=memory_folder, recursive=False)
    
    # Start the observer
    observer.start()
    print(f"Monitoring folder: {memory_folder}")
    
    try:
        while True:
            # Keep the script running
            time.sleep(1)
    except KeyboardInterrupt:
        # Stop the observer on keyboard interrupt
        observer.stop()
    
    # Wait for the observer to stop
    observer.join()

# Example usage
if __name__ == "__main__":
    memory_folder = r"E:\SmartMemoryDefragmenter\MemoryBlocks"  # Use raw string for Windows paths

    # Check if the folder exists
    if not os.path.exists(memory_folder):
        print(f"Error: The folder '{memory_folder}' does not exist.")
    else:
        # Start monitoring the folder in real-time
        monitor_memory_folder(memory_folder)