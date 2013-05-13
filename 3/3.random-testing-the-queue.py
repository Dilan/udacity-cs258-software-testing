# TASK:
#
# Write a random tester for the Queue class.
# The random tester should repeatedly call
# the Queue methods on random input in a
# semi-random fashion. for instance, if
# you wanted to randomly decide between
# calling enqueue and dequeue, you would
# write something like this:
#
# q = Queue(500)
# if (random.random() < 0.5):
#     q.enqueue(some_random_input)
# else:
#     q.dequeue()
#
# You should call the enqueue, dequeue,
# and checkRep methods several thousand
# times each.

import array
import random


class Queue:
    def __init__(self, size_max):
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

    def enqueue(self, x):
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
            assert (self.size == 0) or (self.size == self.max)


# Write a random tester for the Queue class.
def test():

    num_iterations = 100000
    queue_size = 500
    helper_queue = []
    queue_under_test = Queue(queue_size)

    for i in (random.randint(0, 1) for x in range(num_iterations)):

        # test state of helper queue against state of queue under test
        if len(helper_queue) == queue_size:
            assert queue_under_test.full() is True
        if len(helper_queue) == 0:
            assert queue_under_test.empty() is True

        # enqueue
        if i == 0:
            thing_to_enqueue = random.randint(0, 100000)
            # before attempting to queue, is the queue already full?
            queue_was_full_before_enqueue = True if (len(helper_queue) == queue_size) else False
            result = queue_under_test.enqueue(thing_to_enqueue)

            if queue_was_full_before_enqueue:
                assert result is False
                assert queue_under_test.full() is True

            else:
                assert result is True
                helper_queue.append(thing_to_enqueue)

        # dequeue
        if i == 1:
            size_before_dequeue = len(helper_queue)

            result = queue_under_test.dequeue()

            if len(helper_queue) > 0:
                helper_result = helper_queue.pop(0)
            else:
                helper_result = None

            assert result == helper_result

            if size_before_dequeue == 0:
                assert result is None

        queue_under_test.checkRep()

test()
