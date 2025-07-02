# test/test_performance.py (Benchmarking)
import timeit
import matplotlib.pyplot as plt

class PerformanceBenchmark:
    @staticmethod
    def run_comparison():
        strategies = ['FIRST_FIT', 'BEST_FIT', 'SMART_AI']
        results = {s: [] for s in strategies}
        
        # Test with different workload patterns
        patterns = [
            [1,3,1,3,1,3],  # Alternating
            [1,2,3,4,1,2],  # Increasing
            [random.randint(1,4) for _ in range(20)]  # Random
        ]
        
        for pattern in patterns:
            for strategy in strategies:
                time = timeit.timeit(
                    f"run_workload({pattern}, AllocationStrategy.{strategy})",
                    setup="from main import run_workload; from allocator import AllocationStrategy",
                    number=100
                )
                results[strategy].append(time)
        
        # Plot results
        plt.figure(figsize=(10, 6))
        for strategy in strategies:
            plt.plot(patterns, results[strategy], label=strategy)
        plt.title('Allocation Strategy Performance')
        plt.xlabel('Workload Pattern')
        plt.ylabel('Execution Time (ms)')
        plt.legend()
        plt.show()