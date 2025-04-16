def defragment_memory(memory):
    """
    Defragments the memory by moving all allocated blocks to the beginning.
    """
    memory = [x for x in memory if x != 0]  # Remove empty blocks
    memory += [0] * (20 - len(memory))  # Add free blocks at the end
    return memory


def allocate_block(memory, block_id, size):
    """
    Allocates a block of given size in the first available space.
    Returns updated memory and new block ID.
    """
    consecutive_free = 0
    start_index = -1

    # Find the first contiguous free space of required size
    for i, block in enumerate(memory):
        if block == 0:
            if consecutive_free == 0:
                start_index = i
            consecutive_free += 1
            if consecutive_free == size:
                break
        else:
            consecutive_free = 0
            start_index = -1

    # If no space found, return unchanged memory
    if start_index == -1 or consecutive_free < size:
        print("Not enough contiguous memory to allocate.")
        return memory, block_id

    # Allocate the block
    for i in range(start_index, start_index + size):
        memory[i] = f"Block-{block_id}"
    block_id += 1
    return memory, block_id


def calculate_fragmentation(memory):
    """
    Calculates the percentage of fragmented memory.
    Fragmentation is defined as the number of free blocks divided by total memory size.
    """
    free_blocks = memory.count(0)
    total_blocks = len(memory)
    fragmentation_percent = (free_blocks / total_blocks) * 100
    return {
        "free_blocks": free_blocks,
        "total_blocks": total_blocks,
        "fragmentation_percent": round(fragmentation_percent, 2),
    }


def allocate_best_fit(memory, block_id, size):
    """
    Allocates memory using the Best Fit strategy.
    Finds the smallest free block that can accommodate the requested size.
    """
    best_start = -1
    best_size = float('inf')

    # Find the smallest free block that fits the requested size
    start = -1
    free_space = 0
    for i, block in enumerate(memory):
        if block == 0:
            if start == -1:
                start = i
            free_space += 1
        else:
            if free_space >= size and free_space < best_size:
                best_start = start
                best_size = free_space
            start = -1
            free_space = 0

    # Check the last free space at the end of the memory
    if free_space >= size and free_space < best_size:
        best_start = start
        best_size = free_space

    # Allocate the block if a suitable space is found
    if best_start != -1:
        for i in range(best_start, best_start + size):
            memory[i] = f"Block-{block_id}"
        block_id += 1
        return memory, block_id

    print("Not enough memory available!")
    return memory, block_id