# # import matplotlib.pyplot as plt

# # def print_memory(memory):
# #     """
# #     Displays the current state of memory with allocated blocks and free spaces.
# #     """
# #     memory_rep = ' | '.join([str(x) if x != 0 else '_' for x in memory])
# #     print(f"Memory: [{memory_rep}]")

# # def plot_memory_graph(fragmentation_values):
# #     """
# #     Plots a graph of fragmentation percentages over time.
# #     """
# #     plt.plot(fragmentation_values, marker='o')
# #     plt.title("Memory Fragmentation Over Time")
# #     plt.xlabel("Allocation Attempts")
# #     plt.ylabel("Fragmentation (%)")
# #     plt.show()

# # def plot_fragmentation_comparison(best_fit_data, smart_defrag_data):
# #     """
# #     Plots a bar graph comparing fragmentation percentages for Best Fit and Smart Defragmentation.
# #     """
# #     attempts = range(1, len(best_fit_data) + 1)
# #     bar_width = 0.35

# #     plt.figure(figsize=(10, 6))
# #     bars1 = plt.bar(attempts, best_fit_data, bar_width, label='Best Fit', alpha=0.7)
# #     bars2 = plt.bar([x + bar_width for x in attempts], smart_defrag_data, bar_width, label='Smart Defrag', alpha=0.7)

# #     plt.title("Comparison of Fragmentation Over Time")
# #     plt.xlabel("Allocation Attempts")
# #     plt.ylabel("Fragmentation (%)")
# #     plt.xticks([x + bar_width / 2 for x in attempts], attempts)
# #     plt.legend()
# #     plt.tight_layout()
# #     plt.show()



# # import matplotlib.pyplot as plt

# # def print_memory(memory):
# #     """
# #     Displays the current state of memory with allocated blocks and free spaces.
# #     """
# #     memory_rep = ' | '.join([str(x) if x != 0 else '_' for x in memory])
# #     print(f"Memory: [{memory_rep}]")

# # def plot_memory_graph(fragmentation_values):
# #     """
# #     Plots a graph of fragmentation percentages over time.
# #     """
# #     if not fragmentation_values:
# #         print("No fragmentation data available to plot.")
# #         return

# #     plt.plot(fragmentation_values, marker='o')
# #     plt.title("Memory Fragmentation Over Time")
# #     plt.xlabel("Allocation Attempts")
# #     plt.ylabel("Fragmentation (%)")
# #     plt.grid(True)
# #     plt.show()

# # def plot_fragmentation_comparison(best_fit_data, smart_defrag_data):
# #     """
# #     Plots a bar graph comparing fragmentation percentages for Best Fit and Smart Defragmentation.
# #     """
# #     # Check if both datasets are non-empty
# #     if not best_fit_data or not smart_defrag_data:
# #         print("Error: Insufficient data to generate the comparison graph.")
# #         return

# #     # Ensure both datasets have the same length
# #     if len(best_fit_data) != len(smart_defrag_data):
# #         print("Error: Mismatched data lengths for Best Fit and Smart Defrag.")
# #         return

# #     attempts = range(1, len(best_fit_data) + 1)
# #     bar_width = 0.35

# #     plt.figure(figsize=(10, 6))
# #     bars1 = plt.bar(attempts, best_fit_data, bar_width, label='Best Fit', alpha=0.7)
# #     bars2 = plt.bar([x + bar_width for x in attempts], smart_defrag_data, bar_width, label='Smart Defrag', alpha=0.7)

# #     plt.title("Comparison of Fragmentation Over Time")
# #     plt.xlabel("Allocation Attempts")
# #     plt.ylabel("Fragmentation (%)")
# #     plt.xticks([x + bar_width / 2 for x in attempts], attempts)
# #     plt.legend()
# #     plt.tight_layout()
# #     plt.grid(axis='y', linestyle='--', alpha=0.7)
# #     plt.show()


# import matplotlib.pyplot as plt

# def print_memory(memory):
#     """
#     Prints the current state of memory in a readable format.
#     """
#     print("Memory State:")
#     print("[" + " | ".join(str(block) if block != 0 else "_" for block in memory) + "]")


# def plot_fragmentation_comparison(best_fit_data, smart_defrag_data):
#     """
#     Plots a bar graph comparing fragmentation percentages for Best Fit and Smart Defragmentation.
#     """
#     # Check if both datasets are non-empty
#     if not best_fit_data or not smart_defrag_data:
#         print("Error: Insufficient data to generate the comparison graph.")
#         return

#     # Ensure both datasets have the same length
#     if len(best_fit_data) != len(smart_defrag_data):
#         print("Error: Mismatched data lengths for Best Fit and Smart Defrag.")
#         return

#     attempts = range(1, len(best_fit_data) + 1)
#     bar_width = 0.35

#     plt.figure(figsize=(10, 6))
#     bars1 = plt.bar(attempts, best_fit_data, bar_width, label='Best Fit', alpha=0.7)
#     bars2 = plt.bar([x + bar_width for x in attempts], smart_defrag_data, bar_width, label='Smart Defrag', alpha=0.7)

#     plt.title("Comparison of Fragmentation Over Time")
#     plt.xlabel("Allocation Attempts")
#     plt.ylabel("Fragmentation (%)")
#     plt.xticks([x + bar_width / 2 for x in attempts], attempts)
#     plt.legend()
#     plt.tight_layout()  # Move this line before plt.show()

#     # Show the plot and wait until it's manually closed
#     plt.show()  # Blocking behavior, graph will stay open until manually closed


# def plot_memory_usage(memory_usage_data):
#     """
#     Plots a line graph of memory usage over time.
#     """
#     if not memory_usage_data:
#         print("Error: Insufficient data to generate the memory usage graph.")
#         return

#     attempts = range(1, len(memory_usage_data) + 1)

#     plt.figure(figsize=(10, 6))
#     plt.plot(attempts, memory_usage_data, marker='o', label='Memory Usage (%)', color='blue')

#     plt.title("Memory Usage Over Time")
#     plt.xlabel("Operations")
#     plt.ylabel("Memory Usage (%)")
#     plt.xticks(attempts)
#     plt.legend()
#     plt.tight_layout()

#     # Show the plot and wait until it's manually closed
#     plt.show()  # Blocking behavior, graph will stay open until manually closed



# src_/visualizer.py (3D Enhanced)
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class MemoryVisualizer:
    @staticmethod
    def show_3d_memory(memory, history):
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Create 3D blocks
        xpos, ypos, zpos = [], [], []
        dx, dy, dz = [], [], []
        colors = []
        
        for i, block in enumerate(memory):
            xpos.append(i)
            ypos.append(0)
            zpos.append(0)
            dx.append(0.8)
            dy.append(0.8)
            dz.append(0.8 if block else 0.2)
            colors.append('red' if block else 'green')
        
        ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors)
        ax.set_title('3D Memory Map')
        ax.set_xlabel('Block Address')
        ax.set_ylabel('Time')
        ax.set_zlabel('Usage Intensity')
        
        # Add fragmentation history
        ax.plot(np.arange(len(history)), history, zs=1, zdir='y', color='blue')
        plt.show()