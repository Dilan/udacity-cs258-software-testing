# Enhanced Queue class
class Queue:
    
    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = {}

    def __str__(self):
        return str(self.data)

    def clear(self):       
        self.__init__(self.max)

    def empty(self):       
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        if type(x) is not int and type(x) is not str and type(x) is not bool:
            return False
        if self.size == self.max:
            return False
        
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:           
            self.tail = 0
        return True

    def enqueueall(self, c):
        if type(c) is tuple or type(c) is list:
            if not self.size + len(c) > self.max:
                for itm in c:
                    self.enqueue(itm)
                return True
        return False

    def dequeue(self):
        if self.size == 0:           
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:           
            self.head = 0
        return x 

    def checkRep(self):
        assert self.tail >= 0
        assert self.tail < self.max
        assert self.head >= 0
        assert self.head < self.max
        if self.tail > self.head:
            assert (self.tail-self.head) == self.size
        if self.tail < self.head:
            assert (self.head-self.tail) == (self.max-self.size)
        if self.head == self.tail:
            assert (self.size==0) or (self.size==self.max)


# Provide full statement and parameter value coverage of the Queue class
def test():
    # overfill test; parameter coverage
    q = Queue(4)
    q.enqueue(1)
    q.enqueue('')
    q.enqueue('asdf')
    q.enqueue(False)
    q.enqueue(True)
    q.checkRep()

    # dequeue and dequeue empty
    q = Queue(10)
    q.enqueue(1)
    el = q.dequeue()
    assert el == 1
    el = q.dequeue()
    assert el is None

    # __str__
    print(q)

    q.clear()
    q.checkRep()

    q.empty()
    q.checkRep()

    q.enqueueall((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    assert q.full()
    q.clear()
    assert q.empty()
    q.checkRep()

    assert q.enqueue([1]) is False
    assert q.enqueueall(1) is False
    q.checkRep()

    q = Queue(1)
    q.enqueue(1)
    q.dequeue()
    q.checkRep()

    q = Queue(3)
    q.enqueue(0)
    q.checkRep()
    q.enqueue(1)
    q.enqueue(2)
    q.dequeue()
    q.checkRep()
    q.dequeue()
    q.dequeue()
    q.enqueue(2)
    q.enqueue(3)


test()

