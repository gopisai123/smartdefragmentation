def allocate_file_to_memory(memory, block_id, file_size):
    for i in range(len(memory) - file_size + 1):
        if all(x == 0 for x in memory[i:i + file_size]):
            file_name = f"File-{block_id}"
            for j in range(i, i + file_size):
                memory[j] = file_name
            block_id += 1
            return memory, block_id, file_name
    print("Not enough contiguous memory to allocate file.")
    return memory, block_id, None