

import time
import random
import threading
import os
import queue
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from src_.defragmenter import defragment_memory, allocate_block, calculate_fragmentation, allocate_best_fit
from src_.predictor import predict_allocation
from src_.visualizer import print_memory, plot_fragmentation_comparison
from src_.file_manager import allocate_file_to_memory

# Global memory and block ID
memory = [0] * 20
block_id = 1

# Thread-safe queue to handle file events
file_event_queue = queue.Queue()

def preload_memory_from_folder(folder_path):
    global memory, block_id
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    files = os.listdir(folder_path)
    files.sort()
    idx = 0
    for file in files:
        if idx < len(memory):
            memory[idx] = file  # Store the actual file name in memory
            block_id += 1
            idx += 1
        else:
            break
    print(f"Preloaded {idx} files from {folder_path}.")

def clear_screen():
    print("\033[H\033[J", end="")

class FileCreationHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"DEBUG: File detected: {event.src_path}")
            file_event_queue.put(("create", event.src_path))  # Add file path to queue with "create" action

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"DEBUG: File deleted: {event.src_path}")
            file_event_queue.put(("delete", event.src_path))  # Add file path to queue with "delete" action

def start_file_watcher():
    path_to_watch = "MemoryBlocks"
    if not os.path.exists(path_to_watch):
        os.makedirs(path_to_watch)
    event_handler = FileCreationHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=False)
    observer.start()
    print(f"Watching folder: {path_to_watch}")
    return observer

def main():
    global memory, block_id
    best_fit_fragmentation = []
    smart_defrag_fragmentation = []

    # Start watcher in a background thread
    observer = start_file_watcher()

    try:
        while True:
            clear_screen()
            print("==== SMART DEFRAG SYSTEM ====")
            print("Current Memory State: ")
            print_memory(memory)

            # Check file event queue
            while not file_event_queue.empty():
                action, file_path = file_event_queue.get()
                file_name = os.path.basename(file_path)  # Extract file name from path

                if action == "create":
                    try:
                        size = int(input(f"Enter block size for the file '{file_name}': "))
                        if size <= 0 or size > len(memory):
                            print("Invalid block size. Defaulting to 1.")
                            size = 1
                    except ValueError:
                        print("Invalid input. Defaulting to 1.")
                        size = 1

                    # Allocate file to memory using its actual name
                    allocated = False
                    for i in range(len(memory)):
                        if memory[i] == 0:  # Find free blocks
                            memory[i:i + size] = [file_name] * size  # Store the actual file name
                            allocated = True
                            break
                    if allocated:
                        print(f"New file created: {file_name} (Size: {size} blocks)")
                    else:
                        print(f"Not enough contiguous memory to allocate file '{file_name}'.")
                    time.sleep(1)

                elif action == "delete":
                    # Remove the file from memory
                    file_found = False
                    for i in range(len(memory)):
                        if memory[i] == file_name:
                            memory[i] = 0  # Free the block
                            file_found = True
                    if file_found:
                        print(f"DEBUG: File '{file_name}' deleted from memory.")
                    else:
                        print(f"DEBUG: File '{file_name}' not found in memory.")

            print("\n==== MENU ====")
            print("1. View Memory")
            print("2. Allocate Memory Block (Smart Defrag)")
            print("3. Predict Upcoming Allocation")
            print("4. Defragment Memory")
            print("5. View Fragmentation Graph")
            print("6. Simulate File Creation")
            print("7. Exit")
            print("8. Allocate Memory Block (Best Fit)")

            choice = input("\nEnter your choice: ")

            if choice == '1':
                print_memory(memory)

            elif choice == '2':
                try:
                    size = int(input("Enter block size to allocate: "))
                    if size <= 0 or size > len(memory):
                        print("Invalid block size.")
                        continue
                    memory, block_id = allocate_block(memory, block_id, size)
                    fragmentation = calculate_fragmentation(memory)
                    smart_defrag_fragmentation.append(fragmentation['fragmentation_percent'])
                except ValueError:
                    print("Please enter a valid integer.")
                time.sleep(1)

            elif choice == '3':
                pred = predict_allocation()
                print(f"Predicted upcoming allocation size: {pred}")
                time.sleep(1)

            elif choice == '4':
                print("Defragmenting memory...")
                memory = defragment_memory(memory)
                print("Defragmentation done!")
                time.sleep(1)

            elif choice == '5':
                fragmentation = calculate_fragmentation(memory)
                smart_defrag_fragmentation.append(fragmentation['fragmentation_percent'])
                plot_fragmentation_comparison(best_fit_fragmentation, smart_defrag_fragmentation)
                time.sleep(2)

            elif choice == '6':
                size = random.randint(1, 4)
                memory, block_id, file_name = allocate_file_to_memory(memory, block_id, size)
                print(f"File {file_name} allocated to memory.")
                time.sleep(1)

            elif choice == '7':
                print("Exiting Smart Defragment System...")
                observer.stop()
                observer.join()
                break

            elif choice == '8':
                try:
                    size = int(input("Enter block size to allocate using Best Fit: "))
                    if size <= 0 or size > len(memory):
                        print("Invalid block size.")
                        continue
                    memory, block_id = allocate_best_fit(memory, block_id, size)
                    fragmentation = calculate_fragmentation(memory)
                    best_fit_fragmentation.append(fragmentation['fragmentation_percent'])
                except ValueError:
                    print("Please enter a valid integer.")
                time.sleep(1)

            else:
                print("Invalid choice, please try again.")
                time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()

if __name__ == "__main__":
    preload_memory_from_folder("MemoryBlocks")
    main()


