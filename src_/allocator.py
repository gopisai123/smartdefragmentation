# from enum import Enum, auto
# import random

# class AllocationStrategy(Enum):
#     FIRST_FIT = auto()
#     BEST_FIT = auto()
#     WORST_FIT = auto()
#     SMART_AI = auto()

# class AdvancedAllocator:
#     def __init__(self, memory_size=20):
#         self.memory = [{
#             'content': None,
#             'size': 0,
#             'timestamp': 0,
#             'access_count': 0
#         } for _ in range(memory_size)]
#         self.clock = 0
        
#     def allocate(self, file_name, size, strategy, predictor=None):
#         self.clock += 1
        
#         if strategy == AllocationStrategy.SMART_AI and predictor:
#             return self._smart_allocate(file_name, size, predictor)
#         elif strategy == AllocationStrategy.BEST_FIT:
#             return self._best_fit(file_name, size)
#         elif strategy == AllocationStrategy.FIRST_FIT:
#             return self._first_fit(file_name, size)
#         elif strategy == AllocationStrategy.WORST_FIT:
#             return self._worst_fit(file_name, size)
#         return False
    
#     def _smart_allocate(self, file_name, size, predictor):
#         prediction = predictor.predict_next()
        
#         if prediction > size * 1.5:
#             position = self._find_high_position(size)
#         else:
#             position = self._find_low_position(size)
            
#         if position != -1:
#             self._place_allocation(position, file_name, size)
#             return True
#         return False
    
#     def _best_fit(self, file_name, size):
#         best_idx = -1
#         min_remaining = float('inf')
        
#         for i in range(len(self.memory)):
#             if self._check_contiguous(i, size):
#                 remaining = self._find_free_blocks(i) - size
#                 if 0 <= remaining < min_remaining:
#                     best_idx = i
#                     min_remaining = remaining
        
#         if best_idx != -1:
#             self._place_allocation(best_idx, file_name, size)
#             return True
#         return False
    
#     def _first_fit(self, file_name, size):
#         for i in range(len(self.memory)):
#             if self._check_contiguous(i, size):
#                 self._place_allocation(i, file_name, size)
#                 return True
#         return False
    
#     def _worst_fit(self, file_name, size):
#         worst_idx = -1
#         max_remaining = -1
        
#         for i in range(len(self.memory)):
#             if self._check_contiguous(i, size):
#                 remaining = self._find_free_blocks(i) - size
#                 if remaining > max_remaining:
#                     worst_idx = i
#                     max_remaining = remaining
        
#         if worst_idx != -1:
#             self._place_allocation(worst_idx, file_name, size)
#             return True
#         return False
    
#     def _check_contiguous(self, start, size):
#         end = start + size
#         if end > len(self.memory):
#             return False
#         return all(block['content'] is None for block in self.memory[start:end])
    
#     def _find_free_blocks(self, start):
#         count = 0
#         while start + count < len(self.memory) and self.memory[start + count]['content'] is None:
#             count += 1
#         return count
    
#     # def _place_allocation(self, position, file_name, size):
#     #     for i in range(position, position + size):
#     #         self.memory[i] = {
#     #             'content': file_name,
#     #             'size': size,
#     #             'timestamp': self.clock,
#     #             'access_count': 0
#     #         }
    

#     import os

# def _place_allocation(self, position, file_name, size):
#     for i in range(position, position + size):
#         self.memory[i] = {
#             'content': file_name,
#             'size': size,
#             'timestamp': self.clock,
#             'access_count': 0
#         }

#     # Save allocated file data to MemoryBlocks/ folder
#     if not os.path.exists("MemoryBlocks"):
#         os.makedirs("MemoryBlocks")
    
#     file_path = os.path.join("MemoryBlocks", file_name)
#     with open(file_path, "w") as f:
#         f.write(f"Allocated {size} block(s)\n")
#         f.write(f"Start block: {position}\n")
#         f.write(f"Timestamp: {self.clock}\n")


#     def _find_high_position(self, size):
#         for i in reversed(range(len(self.memory))):
#             if self._check_contiguous(i, size):
#                 return i
#         return -1
    
#     def _find_low_position(self, size):
#         for i in range(len(self.memory)):
#             if self._check_contiguous(i, size):
#                 return i
#         return -1





# from enum import Enum, auto
# import random
# import os  # move this to the top

# class AllocationStrategy(Enum):
#     FIRST_FIT = auto()
#     BEST_FIT = auto()
#     WORST_FIT = auto()
#     SMART_AI = auto()

# class AdvancedAllocator:
#     def __init__(self, memory_size=20):
#         self.memory = [{
#             'content': None,
#             'size': 0,
#             'timestamp': 0,
#             'access_count': 0
#         } for _ in range(memory_size)]
#         self.clock = 0

#     def allocate(self, file_name, size, strategy, predictor=None):
#         self.clock += 1

#         if strategy == AllocationStrategy.SMART_AI and predictor:
#             return self._smart_allocate(file_name, size, predictor)
#         elif strategy == AllocationStrategy.BEST_FIT:
#             return self._best_fit(file_name, size)
#         elif strategy == AllocationStrategy.FIRST_FIT:
#             return self._first_fit(file_name, size)
#         elif strategy == AllocationStrategy.WORST_FIT:
#             return self._worst_fit(file_name, size)
#         return False

#     def _smart_allocate(self, file_name, size, predictor):
#         prediction = predictor.predict_next()

#         if prediction > size * 1.5:
#             position = self._find_high_position(size)
#         else:
#             position = self._find_low_position(size)

#         if position != -1:
#             self._place_allocation(position, file_name, size)
#             return True
#         return False

#     def _best_fit(self, file_name, size):
#         best_idx = -1
#         min_remaining = float('inf')

#         for i in range(len(self.memory)):
#             if self._check_contiguous(i, size):
#                 remaining = self._find_free_blocks(i) - size
#                 if 0 <= remaining < min_remaining:
#                     best_idx = i
#                     min_remaining = remaining

#         if best_idx != -1:
#             self._place_allocation(best_idx, file_name, size)
#             return True
#         return False

#     def _first_fit(self, file_name, size):
#         for i in range(len(self.memory)):
#             if self._check_contiguous(i, size):
#                 self._place_allocation(i, file_name, size)
#                 return True
#         return False

#     def _worst_fit(self, file_name, size):
#         worst_idx = -1
#         max_remaining = -1

#         for i in range(len(self.memory)):
#             if self._check_contiguous(i, size):
#                 remaining = self._find_free_blocks(i) - size
#                 if remaining > max_remaining:
#                     worst_idx = i
#                     max_remaining = remaining

#         if worst_idx != -1:
#             self._place_allocation(worst_idx, file_name, size)
#             return True
#         return False

#     def _check_contiguous(self, start, size):
#         end = start + size
#         if end > len(self.memory):
#             return False
#         return all(block['content'] is None for block in self.memory[start:end])

#     def _find_free_blocks(self, start):
#         count = 0
#         while start + count < len(self.memory) and self.memory[start + count]['content'] is None:
#             count += 1
#         return count

#     def _place_allocation(self, position, file_name, size):
#         for i in range(position, position + size):
#             self.memory[i] = {
#                 'content': file_name,
#                 'size': size,
#                 'timestamp': self.clock,
#                 'access_count': 0
#             }

#         # Save allocated file data to MemoryBlocks/ folder
#         if not os.path.exists("MemoryBlocks"):
#             os.makedirs("MemoryBlocks")

#         file_path = os.path.join("MemoryBlocks", file_name)
#         with open(file_path, "w") as f:
#             f.write(f"Allocated {size} block(s)\n")
#             f.write(f"Start block: {position}\n")
#             f.write(f"Timestamp: {self.clock}\n")

#     def _find_high_position(self, size):
#         for i in reversed(range(len(self.memory))):
#             if self._check_contiguous(i, size):
#                 return i
#         return -1

#     def _find_low_position(self, size):
#         for i in range(len(self.memory)):
#             if self._check_contiguous(i, size):
#                 return i
#         return -1



from enum import Enum, auto
import random
import os  # move this to the top

class AllocationStrategy(Enum):
    FIRST_FIT = auto()
    BEST_FIT = auto()
    WORST_FIT = auto()
    SMART_AI = auto()

class AdvancedAllocator:
    def __init__(self, memory_size=20):
        self.memory = [{
            'content': None,
            'size': 0,
            'timestamp': 0,
            'access_count': 0
        } for _ in range(memory_size)]
        self.clock = 0

    def allocate(self, file_name, size, strategy, predictor=None):
        self.clock += 1

        if strategy == AllocationStrategy.SMART_AI and predictor:
            success = self._smart_allocate(file_name, size, predictor)
        elif strategy == AllocationStrategy.BEST_FIT:
            success = self._best_fit(file_name, size)
        elif strategy == AllocationStrategy.FIRST_FIT:
            success = self._first_fit(file_name, size)
        elif strategy == AllocationStrategy.WORST_FIT:
            success = self._worst_fit(file_name, size)
        else:
            success = False
        
        self.print_memory_blocks()  # Print the memory blocks after allocation
        return success

    def _smart_allocate(self, file_name, size, predictor):
        prediction = predictor.predict_next()

        if prediction > size * 1.5:
            position = self._find_high_position(size)
        else:
            position = self._find_low_position(size)

        if position != -1:
            self._place_allocation(position, file_name, size)
            return True
        return False

    def _best_fit(self, file_name, size):
        best_idx = -1
        min_remaining = float('inf')

        for i in range(len(self.memory)):
            if self._check_contiguous(i, size):
                remaining = self._find_free_blocks(i) - size
                if 0 <= remaining < min_remaining:
                    best_idx = i
                    min_remaining = remaining

        if best_idx != -1:
            self._place_allocation(best_idx, file_name, size)
            return True
        return False

    def _first_fit(self, file_name, size):
        for i in range(len(self.memory)):
            if self._check_contiguous(i, size):
                self._place_allocation(i, file_name, size)
                return True
        return False

    def _worst_fit(self, file_name, size):
        worst_idx = -1
        max_remaining = -1

        for i in range(len(self.memory)):
            if self._check_contiguous(i, size):
                remaining = self._find_free_blocks(i) - size
                if remaining > max_remaining:
                    worst_idx = i
                    max_remaining = remaining

        if worst_idx != -1:
            self._place_allocation(worst_idx, file_name, size)
            return True
        return False

    def _check_contiguous(self, start, size):
        end = start + size
        if end > len(self.memory):
            return False
        return all(block['content'] is None for block in self.memory[start:end])

    def _find_free_blocks(self, start):
        count = 0
        while start + count < len(self.memory) and self.memory[start + count]['content'] is None:
            count += 1
        return count

    def _place_allocation(self, position, file_name, size):
        for i in range(position, position + size):
            self.memory[i] = {
                'content': file_name,
                'size': size,
                'timestamp': self.clock,
                'access_count': 0
            }

        # Save allocated file data to MemoryBlocks/ folder
        if not os.path.exists("MemoryBlocks"):
            os.makedirs("MemoryBlocks")

        file_path = os.path.join("MemoryBlocks", file_name)
        with open(file_path, "w") as f:
            f.write(f"Allocated {size} block(s)\n")
            f.write(f"Start block: {position}\n")
            f.write(f"Timestamp: {self.clock}\n")

    def _find_high_position(self, size):
        for i in reversed(range(len(self.memory))):
            if self._check_contiguous(i, size):
                return i
        return -1

    def _find_low_position(self, size):
        for i in range(len(self.memory)):
            if self._check_contiguous(i, size):
                return i
        return -1

    # Method to print memory blocks
    def print_memory_blocks(self):
        memory_display = []
        for block in self.memory:
            if block['content'] is not None:
                memory_display.append(f"{block['content'][:5]}...")  # Display first 5 characters of filename
            else:
                memory_display.append('_')
        
        memory_str = ' | '.join(memory_display)
        print(f"\nMemory Blocks: [{memory_str}]")

