from src.memory_simulator import Memory
from src.defragmenter import defragment, reorganize_files
from src.predictive_allocation import predict_allocation
from src.visualizer import visualize_memory

def main():
    # Initialize memory
    memory_size = 20
    mem = Memory(memory_size)

    # Allocate some processes
    mem.allocate("P1", 5)
    mem.allocate("P2", 3)
    mem.deallocate("P1")

    # Visualize memory before defragmentation
    print("Memory before defragmentation:")
    visualize_memory(mem.get_memory(), "Before Defragmentation")

    # Defragment memory
    mem.memory = defragment(mem.get_memory())
    reorganize_files()

    # Visualize memory after defragmentation
    print("Memory after defragmentation:")
    visualize_memory(mem.get_memory(), "After Defragmentation")

    # Predict allocation
    predicted_index = predict_allocation(mem.get_memory(), [])
    print(f"Predicted allocation index: {predicted_index}")

if __name__ == "__main__":
    main()
