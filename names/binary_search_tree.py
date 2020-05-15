"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Less then we go left
        if value < self.value:
            # we know we need to go left
            if not self.left:
                # we park our value here:
                self.left = BSTNode(value)
            else:
                # we cannot park here:
                # continue searching
                self.left.insert(value)
        # Greater or equal we go right:
        else:
            # we know we need to go right
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

                # Return True if the tree contains the value
                # False if it does not

    def contains(self, target):
        """
    To search a given key within our
    binary search tree, we should first compare
    with root. If the key is present at the root, we will return root. If key
    is greater than our roots key, we will head right to our subtree of our
     root node.
        """
        # when we start searching, self will be the root
        # compare the target against self
        #
        # Criteria for returning False: we know we need to go in one direction
        # but there's nothing in the left or right direction
        if target == self.value:
            return True
        if target > self.value:
            # go right if right is a BSTNode
            if not self.right:
                return False
            return self.right.contains(target)
        else:
            # go left if left is a BSTNode
            if not self.left:
                return False
            return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # will go right of our root until infinity
        if not self.right:
            return self.value
            # otherwise, keep going right
        return self.right.get_max()

    def iterative_get_max(self):
        current_max = self.value
        current = self
        # traverse our structure
        while current is not None:
            if current.value > current_max:
                current_max = current.value
            # update our current_max variable if we see a larger value
            current = current.right
        return current_max

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        # each node at once
        # Search left
        # Seart right
        # call the fn on the value at this node
        fn(self.value)
        # pass this function to the left child
        if self.left:
            self.left.for_each(fn)
        if self.right:
            # pass this function to the right child
            self.right.for_each(fn)
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # To get our traversal results in sorted list: left ~>root~> right:
        # Will start at the left node and go through our sub-trees:
        if node.left:
            self.in_order_print(node.left)
            # root node
            print(node.value)
            # Our right node and now go through our sub-trees
            if node.right:
                self.in_order_print(node.right)

    # # Print the value of every node, starting with the given node,
    # case he node is none
    # return
    # *****
    # try without print statments
    #
    # # in an iterative breadth first traversal
    def bft_print(self, node):
        # create queue
        queue = queue()
        # add root to queue
        queue.append(self)
        # while queue is not empty
        while len(queue) > 0:
            node = queue.popleft()
            print(node.value)
            # add children of node to queue
            if node.left:
                queue.queue(node.left)
            if node.right:
                queue.append(node.right)

    #  Print the value of every node, starting with the given node,
    #  in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        current_node = node
        # add root to the node
        stack.append(current_node)
        # look so long as our stack still has elements
        # while stack is not empty
        while len(stack) > 0:
            # node = pop top of stack
            current_node = stack.pop()
            # check if the right child exists
            # add children of node to stack
            if current_node.right:
                stack.append(current_node.right)
            # check if the left child exists
            if current_node.left:
                stack.append(current_node.left)
            # print(current_node.value)
    #
    #     # Stretch Goals -------------------------
    #     # Note: Research may be required
    #
    #     # Print Pre-order recursive DFT
    #
    # def pre_order_dft(self, node):
    #     pass
    #
    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass
