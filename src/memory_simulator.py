import os

class Memory:
    def __init__(self, size):
        self.size = size
        self.memory = [None] * size  # None represents free memory

    def allocate(self, process_id, size):
        # Find a free block and allocate
        for i in range(self.size - size + 1):
            if all(self.memory[i + j] is None for j in range(size)):
                for j in range(size):
                    self.memory[i + j] = process_id
                    self._create_file(process_id, i + j)
                return True
        return False  # No space available

    def deallocate(self, process_id):
        # Free memory occupied by the process
        for i in range(self.size):
            if self.memory[i] == process_id:
                self.memory[i] = None
                self._delete_file(process_id, i)

    def _create_file(self, process_id, index):
        # Create a file to represent an allocated block
        if not os.path.exists("MemoryBlocks"):
            os.makedirs("MemoryBlocks")
        with open(f"MemoryBlocks/{process_id}_block{index}.txt", "w") as file:
            file.write(f"Allocated to {process_id}")

    def _delete_file(self, process_id, index):
        # Delete a file to represent a freed block
        file_path = f"MemoryBlocks/{process_id}_block{index}.txt"
        if os.path.exists(file_path):
            os.remove(file_path)

    def get_memory(self):
        return self.memory
