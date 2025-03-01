import os

def defragment(memory):
    # Move all allocated blocks to the start
    allocated_blocks = [block for block in memory if block is not None]
    free_blocks = [None] * (len(memory) - len(allocated_blocks))
    return allocated_blocks + free_blocks

def reorganize_files():
    # Reorganize files in the MemoryBlocks folder
    files = os.listdir("MemoryBlocks")
    allocated_files = [f for f in files if not f.startswith("free")]
    free_files = [f for f in files if f.startswith("free")]

    # Rename files to reflect their new positions
    for i, file in enumerate(allocated_files + free_files):
        os.rename(f"MemoryBlocks/{file}", f"MemoryBlocks/block{i+1}.txt")
