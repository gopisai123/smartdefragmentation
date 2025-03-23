

# import os
# import random
# import matplotlib.pyplot as plt

# # Ensure MemoryBlocks directory exists
# if not os.path.exists("MemoryBlocks"):
#     os.makedirs("MemoryBlocks")

# # Function to load memory state from the number of files
# def load_memory_from_files():
#     memory_size = 10  # Total memory size
#     memory = [0] * memory_size  # Start with all free blocks

#     # Count all files in the directory (any file type)
#     files = os.listdir("MemoryBlocks")
#     allocated_blocks = min(len(files), memory_size)  # Allocate up to memory_size

#     print(f"Total files found: {len(files)} -> Allocating {allocated_blocks} blocks.")
    
#     # Randomly distribute allocated blocks (simulate fragmentation)
#     allocated_indices = random.sample(range(memory_size), allocated_blocks)
#     for i in allocated_indices:
#         memory[i] = 1  # Mark as allocated

#     print("Loaded Memory State:", memory)  
#     return memory

# # Function to plot memory
# def plot_memory(memory, title):
#     plt.figure()
#     plt.bar(range(len(memory)), memory, color='blue')
#     plt.xlabel("Memory Address")
#     plt.ylabel("Allocated (1) / Free (0)")
#     plt.title(title)
#     plt.show(block=False)

# # Load memory state from files
# memory = load_memory_from_files()

# # Show Before Defragmentation
# print("Showing memory state before defragmentation...")
# plot_memory(memory, "Before Defragmentation")

# # Perform Defragmentation
# def defragment_memory(memory):
#     memory.sort(reverse=True)  # Move allocated blocks (1s) to the left

# defragment_memory(memory)

# # Show After Defragmentation
# print("Showing memory state after defragmentation...")
# plot_memory(memory, "After Defragmentation")

# plt.show()


# //new one 
import os
import random
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

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

# Function to calculate fragmentation percentage
def fragmentation_percentage(memory):
    return (memory.count(0) / len(memory)) * 100  # % of free blocks

# Standard Defragmentation (Best Fit Approach)
def defragment_memory(memory):
    memory.sort(reverse=True)  # Move allocated blocks (1s) to the left
    return memory

# Smart Defragmentation using Machine Learning (Predictive Allocation)
def smart_defragment_memory(memory):
    memory_array = np.array(memory).reshape(-1, 1)

    # Apply KMeans clustering (2 clusters: Allocated vs. Free)
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    labels = kmeans.fit_predict(memory_array)

    # Reorder memory: Cluster 1 (allocated) first, then Cluster 0 (free)
    sorted_memory = [x for _, x in sorted(zip(labels, memory), reverse=True)]
    
    return sorted_memory

# Load memory state from files
print("Loading memory...")
memory = load_memory_from_files()

# Show Before Defragmentation
plot_memory(memory, "Before Defragmentation")

# Perform Standard Defragmentation
print("\nPerforming standard defragmentation (Best Fit)...")
before_frag_standard = fragmentation_percentage(memory)
memory_standard = defragment_memory(memory[:])  # Copy to preserve original
after_frag_standard = fragmentation_percentage(memory_standard)

# Show After Standard Defragmentation
plot_memory(memory_standard, "After Standard Defragmentation")

# Perform Smart Defragmentation
print("\nPerforming smart defragmentation (Predictive Allocation)...")
before_frag_smart = fragmentation_percentage(memory)
memory_smart = smart_defragment_memory(memory[:])  # Copy to preserve original
after_frag_smart = fragmentation_percentage(memory_smart)

# Show After Smart Defragmentation
plot_memory(memory_smart, "After Smart Defragmentation")

# Print Fragmentation Comparison
print("\nFragmentation Comparison:")
print(f"Standard Defragmentation (Best Fit) - Before: {before_frag_standard:.2f}%, After: {after_frag_standard:.2f}%")
print(f"Smart Defragmentation (Predictive)  - Before: {before_frag_smart:.2f}%, After: {after_frag_smart:.2f}%")

plt.show()
