# Task 3. Reverse a Linked List

"""
Note:
Inside of the reverse directory, you'll find a basic implementation of a Singly Linked List. Without making it a Doubly Linked List (adding a tail attribute), complete the reverse_list() function within reverse/reverse.py reverse the contents of the list using recursion, not a loop.
"""


"""
Each element aka node of alist is comprising of two items:
the data nad a reference to the next node.
Our last node has a reference to null. Which the entry point
into a linked list is called the head of the list.
The head is not a seprate node, but references to our fist node.
If our list is empty then our head null is our reference.
"""

# Node class


class Node:
    # Function to initialize the node object
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        # default arguments:
        # value None
        # next_node None
        self.value = value
        # reference to the next node in our list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node to reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # This references to the head of our list:
        # in other words, the first node in the list
        self.head = None

        # O(1)
    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
            """
        This gets the reference to our node we're presently at.
        Will update this as we traverse the list
        Which is the process when we visit all the nodes of
        a tree and may print their values.
        All nodes are connected via links we always start
        """
        current = self.head
        # Lets check to see if we're at a valid node
        while current:
            # Will return True if the current value we're looking at
            # matches our target value
            if current.get_value() == value:
                return True
            # Will update our current node to the current,
            # to our node's next node
            current = current.get_next()
        # if we got here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        """
        We must use recursion for this solution
        base case: at end, return
        if node is None:
        return
        will swap pointers
        #temp = node.next_node
        # node.next_node = previous
        # return self.reverse_list(temp, node)

        Time complexity: O(n). Lets Assume that n is the
        ist's length, the time complexity is O(n).
        Space complexity: O(1) means that the space required to
        process data is constant; it does not grow with size  of our data.
        """
        cur = self.head
        try:
            new = cur.next_node
        except(AttributeError):
            return self
        cur.next = None

        while(new):
            previous = cur
            cur = new
            new = cur.next_node
            cur.next_node = previous
        self.head = cur

        return self
