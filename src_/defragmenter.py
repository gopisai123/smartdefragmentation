# src_/defragmenter.py

# def defragment_memory(memory):
#     # Defragment memory: Move all files to the left, leaving no gaps
#     defragmented_memory = [block for block in memory if block != 0]  # Keep only non-zero blocks (files)
#     # Fill the rest of memory with 0 to simulate empty spaces
#     defragmented_memory += [0] * (len(memory) - len(defragmented_memory))
#     return defragmented_memory

def defragment_memory(memory):
    """Defragment memory by moving all allocated blocks to the front."""
    # Separate allocated blocks from free blocks
    allocated = [block for block in memory if block['content'] is not None]
    free = [{'content': None, 'size': 0} for _ in range(len(memory) - len(allocated))]
    
    # Combine allocated blocks and free blocks
    return allocated + free

def allocate_block(memory, file_name, size):
    # Allocate a block of memory for the file, this can be used in both Smart Defrag and Best Fit
    for i in range(len(memory) - size + 1):
        if all(memory[i + j] == 0 for j in range(size)):  # Check if all blocks are empty
            memory[i:i + size] = [file_name] * size  # Allocate the file
            return True
    return False

def calculate_fragmentation(memory):
    # Calculate fragmentation as the percentage of unfilled blocks
    total_blocks = len(memory)
    used_blocks = len([block for block in memory if block != 0])
    fragmentation_percent = ((total_blocks - used_blocks) / total_blocks) * 100
    return {'fragmentation_percent': fragmentation_percent}

def allocate_best_fit(memory, file_name, size):
    # Best Fit allocation logic: Allocate memory in the smallest possible gap
    best_fit_index = -1
    best_fit_size = len(memory) + 1
    for i in range(len(memory) - size + 1):
        gap_size = sum(1 for j in range(i, i + size) if memory[j] == 0)
        if gap_size == size and gap_size < best_fit_size:
            best_fit_index = i
            best_fit_size = gap_size
    if best_fit_index != -1:
        memory[best_fit_index:best_fit_index + size] = [file_name] * size
        return True
    return False
