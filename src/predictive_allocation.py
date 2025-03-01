def predict_allocation(memory, history):
    # Simple heuristic: allocate at the end of the last allocated block
    last_allocated_index = len(memory) - 1
    while last_allocated_index >= 0 and memory[last_allocated_index] is None:
        last_allocated_index -= 1
    return last_allocated_index + 1
