
#!/usr/bin/env python3
import os
import time
import queue
import threading
from enum import Enum
from datetime import datetime
from src_.predictor import AIPredictor
from src_.allocator import AdvancedAllocator, AllocationStrategy
from src_.visualizer import MemoryVisualizer
from src_.file_manager import start_file_watcher, preload_memory
from src_.defragmenter import defragment_memory

class SmartDefragSystem:
    def __init__(self, memory_size=20):
        self.memory_size = memory_size
        self.allocator = AdvancedAllocator(memory_size)
        self.predictor = AIPredictor(memory_size)
        self.file_queue = queue.Queue()
        self.history = []
        self.performance_stats = {
            'alloc_time': [],
            'fragmentation': [],
            'prediction_accuracy': []
        }
        self.running = True
        
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_banner(self):
        """Show system banner"""
        print("""
        ███████╗███╗   ███╗ █████╗ ██████╗ ████████╗███████╗
        ██╔════╝████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
        ███████╗██╔████╔██║███████║██████╔╝   ██║   █████╗  
        ╚════██║██║╚██╔╝██║██╔══██║██╔═══╝    ██║   ██╔══╝  
        ███████║██║ ╚═╝ ██║██║  ██║██║        ██║   ███████╗
        ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝   ╚══════╝
        """)
        print(f"{' SMART MEMORY DEFRAGMENTATION SYSTEM ':=^60}")
        print(f"Initialized: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Memory Size: {self.memory_size} blocks\n")

    def display_dashboard(self):
        """Show real-time system status"""
        print(f"\n{' MEMORY STATUS ':-^60}")
        print(f"Fragmentation: {self.calculate_fragmentation():.1f}%")
        print(f"Allocations: {len([b for b in self.allocator.memory if b['content']])}")
        print(f"Predictions: {len(self.predictor.X)} samples | Accuracy: {self.prediction_accuracy():.1f}%")
        
        print("\n{' COMMANDS '}")
        print("[1] Smart Allocate   [2] Defragment")
        print("[3] 3D Visualization  [4] Performance Test  [5] Simulate Workload")
        print("[6] Prediction Debug  [7] Memory Map  [8] System Status [Q] Quit")

    def start(self):
        """Initialize and run the system"""
        self.clear_screen()
        self.display_banner()
        
        # Initialize components
        self.watcher = start_file_watcher("MemoryBlocks", self.file_queue)
        preload_memory("MemoryBlocks", self.allocator.memory)
        
        try:
            self.main_loop()
        except KeyboardInterrupt:
            print("\nShutting down gracefully...")
        finally:
            self.running = False
            self.watcher.stop()
            self.watcher.join()
            self.generate_report()

    def print_memory_blocks(self):
        """Display the current state of memory blocks."""
        memory_display = []
        for block in self.allocator.memory:
            if block['content'] is not None:
                memory_display.append(f"{block['content'][:5]}...")  # Display first 5 characters of filename
            else:
                memory_display.append('_')  # Represent empty blocks with '_'
        
        memory_str = ' | '.join(memory_display)
        print(f"\nMemory Blocks: [{memory_str}]")

        

    def main_loop(self):
        """Main control loop"""
        while self.running:
            self.clear_screen()
            self.display_banner()
            self.display_dashboard()
            # input("\nPress Enter to continue...")
            
            self.print_memory_blocks()  # Display memory blocks here
            # Process file system events
            self.handle_file_events()
            
            # Get user command
            choice = input("\nCommand [1-9,Q]: ").strip().upper()
            
            if choice == '1':
                self.interactive_allocation(AllocationStrategy.SMART_AI)
                self.wait_for_continue()
            # elif choice == '2':
            #     self.interactive_allocation(AllocationStrategy.BEST_FIT)
            #     self.wait_for_continue()
            elif choice == '2':
                self.defragment_memory()
                self.print_memory_blocks()
                self.wait_for_continue()
            elif choice == '3':
                self.show_3d_visualization()
                self.wait_for_continue()
            elif choice == '4':
                self.run_performance_test()
                self.wait_for_continue() 
            elif choice == '5':
                self.simulate_workload()
                self.wait_for_continue()
            elif choice == '6':
                self.show_prediction_debug()
                self.wait_for_continue()
            elif choice == '7':
                self.display_memory_map()
                self.wait_for_continue()
            elif choice == '8':
                self.system_status()
                self.wait_for_continue()
            elif choice == 'Q':
                self.running = False
            else:
                print("Invalid choice!")
                time.sleep(1)

    def wait_for_continue(self):
        """Waits for the user to press Enter to continue."""
        input("\nPress Enter to continue...")                

    def display_formatted_files(self,files):
        # This function will format the list of files to match your example format
        formatted_output = ' | '.join(files)
        print(f"[{formatted_output}]")  



    def interactive_allocation(self, strategy):
        """Handle memory allocation with given strategy"""
        try:
            file_name = input("File name: ")
            size = int(input("Block size (1-4): "))
            if not 1 <= size <= 4:
                raise ValueError
                
            start_time = time.perf_counter()
            success = self.allocator.allocate(file_name, size, strategy, self.predictor)
            alloc_time = (time.perf_counter() - start_time) * 1000
            
            if success:
                frag = self.calculate_fragmentation()
                self.predictor.add_allocation(size, self.find_position(file_name), frag)
                self.performance_stats['alloc_time'].append(alloc_time)
                print(f"Allocated in {alloc_time:.2f}ms")
                self.record_history(strategy, frag)
            else:
                print("Allocation failed! Consider defragmentation.")
                
        except ValueError:
            print("Invalid input! Size must be integer between 1-4")
        time.sleep(1)


    # def handle_file_events(self):
    #     """Process file system events from the queue"""
    #     files = []  # Initialize a list to store filenames for display
    #     while not self.file_queue.empty():
    #         action, filename = self.file_queue.get()

    #         if action == 'create':
    #             print(f"\nNew file detected: {filename}")
    #             files.append(filename)  # Add filename to the list
    #             self.display_formatted_files(files)  # Call the method to display files

    #             # Continue the allocation process
    #             try:
    #                 size = int(input("Enter block size (1-4): "))
    #                 if not 1 <= size <= 4:
    #                     raise ValueError
                    
    #                 if self.allocator.allocate(filename, size, AllocationStrategy.SMART_AI, self.predictor):
    #                     frag = self.calculate_fragmentation()
    #                     self.predictor.add_allocation(size, self.find_position(filename), frag)
    #                     self.record_history(AllocationStrategy.SMART_AI, frag)
    #                     print(f"Allocated {filename} (size: {size})")
    #                 else:
    #                     print("Allocation failed! Not enough contiguous space.")
                
    #             except ValueError:
    #                 print("Invalid size! Please enter 1-4")
                    
    #         elif action == 'delete':
    #             print(f"\nFile deleted: {filename}")
    #             self.free_memory_blocks(filename)
    #             files.remove(filename)  # Remove the deleted file from the list
    #             self.display_formatted_files(files)  # Update the display


    def handle_file_events(self):
        """Process file system events from the queue"""
        while not self.file_queue.empty():
            action, filename = self.file_queue.get()
            
            if action == 'create':
                print(f"\nNew file detected: {filename}")
                try:
                    size = int(input("Enter block size (1-4): "))
                    if not 1 <= size <= 4:
                        raise ValueError
                        
                    if self.allocator.allocate(filename, size, AllocationStrategy.SMART_AI, self.predictor):
                        frag = self.calculate_fragmentation()
                        self.predictor.add_allocation(size, self.find_position(filename), frag)
                        self.record_history(AllocationStrategy.SMART_AI, frag)
                        print(f"Allocated {filename} (size: {size})")
                    else:
                        print("Allocation failed! Not enough contiguous space.")
                        
                except ValueError:
                    print("Invalid size! Please enter 1-4")
                
            elif action == 'delete':
                print(f"\nFile deleted: {filename}")
                freed = self.free_memory_blocks(filename)
                if freed > 0:
                    print(f"Freed {freed} blocks occupied by {filename}")
                else:
                    print(f"File '{filename}' not found in memory.")

    def find_position(self, filename):
        """Find the starting position of a file in memory"""
        for i, block in enumerate(self.allocator.memory):
            if block['content'] == filename:
                return i
        return -1

    def free_memory_blocks(self, filename):
        """Free all blocks occupied by a file"""
        freed = 0
        for block in self.allocator.memory:
            if block['content'] == filename:
                block['content'] = None
                block['size'] = 0
                freed += 1
        if freed > 0:
            print(f"Freed {freed} blocks occupied by {filename}")
        return freed

    def record_history(self, strategy, fragmentation):
        """Record operation in history"""
        self.history.append({
            'timestamp': datetime.now(),
            'strategy': strategy.name,
            'fragmentation': fragmentation,
            'memory_snapshot': [block.copy() for block in self.allocator.memory]
        })

    def defragment_memory(self):
        """Defragment memory and update history"""
        print("Starting defragmentation...")
        self.allocator.memory = defragment_memory(self.allocator.memory)
        frag = self.calculate_fragmentation()
        self.record_history(AllocationStrategy.SMART_AI, frag)
        print("Defragmentation complete!")
        time.sleep(1)

    def run_performance_test(self):
        """Run performance benchmark"""
        print("Running performance test...")
        # Simple test - allocate and free blocks
        test_file = "perf_test.dat"
        start_time = time.perf_counter()
        
        for size in range(1, 5):
            self.allocator.allocate(test_file, size, AllocationStrategy.SMART_AI, self.predictor)
            self.free_memory_blocks(test_file)
            
        elapsed = (time.perf_counter() - start_time) * 1000
        print(f"Performance test completed in {elapsed:.2f}ms")
        time.sleep(1)

    def simulate_workload(self):
        """Simulate a file workload pattern"""
        print("\nWorkload patterns:")
        print("1. Alternating (1,3,1,3)")
        print("2. Increasing (1,2,3,4)")
        print("3. Random")
        
        try:
            choice = int(input("Select pattern (1-3): "))
            patterns = [
                [1, 3, 1, 3],
                [1, 2, 3, 4],
                [2, 1, 4, 2, 3]  # Random pattern
            ]
            
            for i, size in enumerate(patterns[choice-1]):
                file_name = f"sim_{i}.dat"
                if self.allocator.allocate(file_name, size, AllocationStrategy.SMART_AI, self.predictor):
                    print(f"Allocated {file_name} (size: {size})")
                else:
                    print(f"Failed to allocate {file_name}")
                    
        except (ValueError, IndexError):
            print("Invalid pattern selection!")
        time.sleep(1)

    def show_prediction_debug(self):
        """Show prediction debugging information"""
        print("\nPrediction Debug Information:")
        print(f"Sample count: {len(self.predictor.X)}")
        if len(self.predictor.X) > 0:
            print(f"Last prediction: {self.predictor.predict_next()}")
            print(f"Last 5 allocations: {list(self.predictor.history)[-5:]}")
        time.sleep(2)

    def display_memory_map(self):
        """Display ASCII memory map"""
        print("\nMemory Map:")
        for i, block in enumerate(self.allocator.memory):
            status = 'F' if block['content'] else 'E'
            print(f"{i:02d}: {status}", end=' ')
            if (i+1) % 10 == 0:
                print()
        print("\n(F = Full, E = Empty)")
        time.sleep(2)

    def system_status(self):
        """Display detailed system status"""
        print("\nSystem Status:")
        print(f"Running: {'Yes' if self.running else 'No'}")
        print(f"Memory blocks: {self.memory_size}")
        print(f"Active allocations: {len([b for b in self.allocator.memory if b['content']])}")
        print(f"File watcher: {'Active' if hasattr(self, 'watcher') else 'Inactive'}")
        time.sleep(2)

    def show_3d_visualization(self):
        """Display advanced 3D memory visualization"""
        print("Generating 3D visualization...")
        history = [x['fragmentation'] for x in self.history[-20:]]
        MemoryVisualizer.show_3d_memory(self.allocator.memory, history)
        
    def generate_report(self):
        """Generate performance report"""
        print("\n=== SYSTEM PERFORMANCE REPORT ===")
        print(f"Total allocations: {len(self.performance_stats['alloc_time'])}")
        if self.performance_stats['alloc_time']:
            avg_time = sum(self.performance_stats['alloc_time'])/len(self.performance_stats['alloc_time'])
            print(f"Average allocation time: {avg_time:.2f}ms")
        print(f"Final fragmentation: {self.calculate_fragmentation():.1f}%")
        print(f"Prediction accuracy: {self.prediction_accuracy():.1f}%")
        print(f"Report generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    def calculate_fragmentation(self):
        """Calculate current fragmentation percentage"""
        free_blocks = sum(1 for block in self.allocator.memory if not block['content'])
        return (free_blocks / self.memory_size) * 100 if self.memory_size > 0 else 0

    def prediction_accuracy(self):
        # Calculate accuracy by comparing predicted and actual values
        correct = sum(1 for i in range(1, len(self.history))
                    if abs(self.history[i].get('predicted', 0) - self.history[i].get('actual', 0)) <= 1)
        total = len(self.history) - 1
        accuracy = (correct / total) * 100 if total > 0 else 0
        return accuracy


if __name__ == "__main__":
    system = SmartDefragSystem(memory_size=20)
    system.start()