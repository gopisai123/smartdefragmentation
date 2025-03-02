import matplotlib.pyplot as plt

def visualize_memory(memory, title="Memory Blocks"):
    plt.bar(range(len(memory)), [1 if block is not None else 0 for block in memory], color='blue')
    plt.title(title)
    plt.xlabel("Memory Address")
    plt.ylabel("Allocated (1) / Free (0)")
    plt.show()
