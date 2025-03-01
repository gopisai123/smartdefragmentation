from src.memory_simulator import Memory

def test_memory_allocation():
    mem = Memory(10)
    assert mem.allocate("P1", 3) == True
    assert mem.get_memory() == ["P1", "P1", "P1", None, None, None, None, None, None, None]

def test_memory_deallocation():
    mem = Memory(10)
    mem.allocate("P1", 3)
    mem.deallocate("P1")
    assert mem.get_memory() == [None] * 10
