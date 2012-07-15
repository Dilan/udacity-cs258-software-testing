# CORRECT SPECIFICATION:
#
# the Queue class provides a fixed-size FIFO queue of integers
#
# the constructor takes a single parameter: an integer > 0 that
# is the maximum number of elements the queue can hold.
#
# empty() returns True if and only if the queue currently 
# holds no elements, and False otherwise.
#
# full() returns True if and only if the queue cannot hold 
# any more elements, and False otherwise.
#
# enqueue(i) attempts to put the integer i into the queue; it returns
# True if successful and False if the queue is full.
#
# dequeue() removes an integer from the queue and returns it,
# or else returns None if the queue is empty.
#
# Example:
# q = Queue(1)
# is_empty = q.empty()
# succeeded = q.enqueue(10)
# is_full = q.full()
# value = q.dequeue()
#
# 1. Should create a Queue q that can only hold 1 element
# 2. Should then check whether q is empty, which should return True
# 3. Should attempt to put 10 into the queue, and return True
# 4. Should check whether q is now full, which should return True
# 5. Should attempt to dequeue and put the result into value, which 
#    should be 10
#
# Your test function should run assertion checks and throw an 
# AssertionError for each of the 5 incorrect Queues. Pressing 
# submit will tell you how many you successfully catch so far.


import array

class Queue:
    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        if self.size == self.max:
            return False
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

def test():
    q = Queue(3)
    assert q.empty()
    assert not q.full()
    
    res = q.dequeue()
    assert res == None
    assert q.empty()
    
    res = q.enqueue(1)
    assert res == True
    assert not q.full()
    assert not q.empty()
    
    res = q.enqueue(2)
    assert res == True
    assert not q.full()
    
    el = q.dequeue()
    assert el == 1
    assert not q.full()
    assert not q.empty()
    
    res = q.enqueue(3)
    assert res == True
    assert not q.full()

    res = q.enqueue(4)
    assert res == True
    assert q.full()
    
    res = q.enqueue(999)
    assert res == False
    assert q.full()
    
    el = q.dequeue()
    assert el == 2
    assert not q.full()
    assert not q.empty()
    
    el = q.dequeue()
    assert el == 3
    assert not q.full()
    assert not q.empty()
    
    el = q.dequeue()
    assert el == 4
    assert not q.full()
    assert q.empty()
    
    el = q.dequeue()
    assert el == None
    assert not q.full()
    assert q.empty()

    res = q.enqueue(21)
    assert res == True
    assert not q.empty()
    assert not q.full()
    
    el = q.dequeue()
    assert el == 21
    assert q.empty()
    assert not q.full()
    
    q.enqueue(31)
    q.enqueue(32)
    q.dequeue()
    q.enqueue(33)
    el = q.dequeue()
    assert el == 32
    
    q.enqueue(34)
    q.enqueue(35)
    q.enqueue(36)
    q.enqueue(37)
    assert q.full()
    
    el = q.dequeue()
    assert el == 33
    assert not q.full()
    
    q = Queue(1000)
    for i in range(1,1500):
        q.enqueue(i)
    assert q.full()
    
    res = q.enqueue(12345)
    assert res == False
    assert q.full()
    
    while not q.empty():
        el = q.dequeue()
    assert el == 1000
    assert q.empty()
    
    q.enqueue(1234123412341234)
    el = q.dequeue()
    assert el == 1234123412341234

test()