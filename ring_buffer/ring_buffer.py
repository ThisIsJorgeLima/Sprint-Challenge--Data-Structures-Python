# Task 1. Implement a Ring Buffer Data Structure

"""
Our ring buffer is a non-groable buffer with a fixed size.
When it fills up, adding another element overwrites the oldest one that was still being kept.
"""
# Example:
# buffer = RingBuffer(3)
#
# buffer.get()   # should return []
#
# buffer.append('a')
# buffer.append('b')
# buffer.append('c')
#
# buffer.get()   # should return ['a', 'b', 'c']
#
# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')
#
# buffer.get()   # should return ['d', 'b', 'c']
#
# buffer.append('e')
# buffer.append('f')
#
# buffer.get()   # should return ['d', 'e', 'f']


class RingBuffer:
    # class that implements a not-yet-full buffer
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # add item to storage list
        """
        The append method adds the given element to the buffer.
        Which will overwrite the oldest one.
        """
        self.storage[self.current] = item
        # lenght of list
        # if self.current >=len(self.storage)-1
        if self.current < (self.capacity-1):
            self.current += 1
        else:
            self.current = 0

    def get(self):
        """
        The get method returns all of the elements in the buffer in a list in their given order. It should not return any None values in the list even if they are present in the ring buffer.

        Should return a list of elements from the oldest to the newest.
        """
        # Our list:
        list = [item for item in self.storage if item]
        return list
