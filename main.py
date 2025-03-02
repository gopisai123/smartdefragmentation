# from src.memory_simulator import Memory
# from src.defragmenter import defragment, reorganize_files
# from src.predictive_allocation import predict_allocation
# from src.visualizer import visualize_memory

# def main():
#     # Initialize memory
#     memory_size = 20
#     mem = Memory(memory_size)

#     # Allocate some processes
#     mem.allocate("P1", 5)
#     mem.allocate("P2", 3)
#     mem.deallocate("P1")

#     # Visualize memory before defragmentation
#     print("Memory before defragmentation:")
#     visualize_memory(mem.get_memory(), "Before Defragmentation")

#     # Defragment memory
#     mem.memory = defragment(mem.get_memory())
#     reorganize_files()

#     # Visualize memory after defragmentation
#     print("Memory after defragmentation:")
#     visualize_memory(mem.get_memory(), "After Defragmentation")

#     # Predict allocation
#     predicted_index = predict_allocation(mem.get_memory(), [])
#     print(f"Predicted allocation index: {predicted_index}")

# if __name__ == "__main__":
#     main()




import os
import random
import matplotlib.pyplot as plt

# Ensure MemoryBlocks directory exists
if not os.path.exists("MemoryBlocks"):
    os.makedirs("MemoryBlocks")

# Function to load memory state from the number of files
def load_memory_from_files():
    memory_size = 10  # Total memory size
    memory = [0] * memory_size  # Start with all free blocks

    # Count all files in the directory (any file type)
    files = os.listdir("MemoryBlocks")
    allocated_blocks = min(len(files), memory_size)  # Allocate up to memory_size

    print(f"Total files found: {len(files)} -> Allocating {allocated_blocks} blocks.")
    
    # Randomly distribute allocated blocks (simulate fragmentation)
    allocated_indices = random.sample(range(memory_size), allocated_blocks)
    for i in allocated_indices:
        memory[i] = 1  # Mark as allocated

    print("Loaded Memory State:", memory)  
    return memory

# Function to plot memory
def plot_memory(memory, title):
    plt.figure()
    plt.bar(range(len(memory)), memory, color='blue')
    plt.xlabel("Memory Address")
    plt.ylabel("Allocated (1) / Free (0)")
    plt.title(title)
    plt.show(block=False)

# Load memory state from files
memory = load_memory_from_files()

# Show Before Defragmentation
print("Showing memory state before defragmentation...")
plot_memory(memory, "Before Defragmentation")

# Perform Defragmentation
def defragment_memory(memory):
    memory.sort(reverse=True)  # Move allocated blocks (1s) to the left

defragment_memory(memory)

# Show After Defragmentation
print("Showing memory state after defragmentation...")
plot_memory(memory, "After Defragmentation")

plt.show()
