import matplotlib.pyplot as plt

def print_memory(memory):
    """
    Displays the current state of memory with allocated blocks and free spaces.
    """
    memory_rep = ' | '.join([str(x) if x != 0 else '_' for x in memory])
    print(f"Memory: [{memory_rep}]")

def plot_memory_graph(fragmentation_values):
    """
    Plots a graph of fragmentation percentages over time.
    """
    plt.plot(fragmentation_values, marker='o')
    plt.title("Memory Fragmentation Over Time")
    plt.xlabel("Allocation Attempts")
    plt.ylabel("Fragmentation (%)")
    plt.show()

def plot_fragmentation_comparison(best_fit_data, smart_defrag_data):
    """
    Plots a bar graph comparing fragmentation percentages for Best Fit and Smart Defragmentation.
    """
    attempts = range(1, len(best_fit_data) + 1)
    bar_width = 0.35

    plt.figure(figsize=(10, 6))
    bars1 = plt.bar(attempts, best_fit_data, bar_width, label='Best Fit', alpha=0.7)
    bars2 = plt.bar([x + bar_width for x in attempts], smart_defrag_data, bar_width, label='Smart Defrag', alpha=0.7)

    plt.title("Comparison of Fragmentation Over Time")
    plt.xlabel("Allocation Attempts")
    plt.ylabel("Fragmentation (%)")
    plt.xticks([x + bar_width / 2 for x in attempts], attempts)
    plt.legend()
    plt.tight_layout()
    plt.show()