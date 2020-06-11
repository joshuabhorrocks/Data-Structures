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

from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # 1. Check if there is no root,
        if self is None:
            # If there isn't, create the node and park it there
            self = BSTNode(value)
        # 2. Otherwise, there is a root
        else:
            # Compare the value to the root's value to determine which direction we're gonna go in
            # If the value < root's value
            if value < self.value:
                # Go left
                # How do we go left?
                if self.left:
                    # Then self.left is a Node
                    self.left.insert(value)
                else:
                    # Then we can park the value here
                    self.left = BSTNode(value)
            # else the value >= root's value
            else:
                # Go right
                # How do we go right?
                if self.right:
                    # Then self.right is a Node
                    self.right.insert(value)
                else:
                    # Then we can park the value here
                    self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        while self != None:
            if target < self.value:
                self = self.left
            elif target > self.value:
                self = self.right
            else:
                return True
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        rCurrent = self
        lCurrent = self
        while(lCurrent.left):
            lCurrent = lCurrent.left
        while(rCurrent.right):
            rCurrent = rCurrent.right
        if rCurrent.value > lCurrent.value:
            return rCurrent.value
        else:
            return lCurrent.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # def iter_depth_first_for_each(self, fn):
    #     # With depth-first traversall there's a certain order when visiting nodes (LIFO)
    #     # Init a stack to keep track of the order of nodes we visited
    #     stack = []
    #     # Add the first node to our stack
    #     stack.append(self)
    #     # Continue traversing until our stack is empty
    #     while len(stack) > 0:
    #         # Pop off the stack 
    #         current_node = stack.pop()
    #         # Add it's children to the stack
    #         # Call the fn function on self.value
    #         if current_node.right:
    #             stack.append(current_node.right)
    #         if current_node.left:
    #             stack.append(current_node.left)
    #         # Call the fn function on self.value
    #         fn(self.value)

    #     def iter_breadth_first_search(self, fn):
    #         # Breadth first traversal follows FIFO ordering of it's nodes
    #         # Init a deque
    #         q = deque()
    #         # Add the first node to our q
    #         q.append(self)

    #         while len(q) > 0:
    #             current_node = q.popleft()
    #             if current_node.left:
    #                 q.append(current_node.left)
    #             if current_node.right:
    #                 q.append(current_node.right)
    #             fn(self.value)


    # Part 2 -----------------------


    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):
        if self.left:
            self.left.in_order_print(self)
        print(self.value)
        if self.right:
            self.right.in_order_print(self)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal (Hits all nodes that are on the same level)
    def bft_print(self, node=None):
        q = deque()
        q.append(self)
        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            print(current_node.value)
            if current_node.right:
                q.append(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal (Prioritizes reaching leaves first)
    def dft_print(self, node):
        stack = []
        stack.append(self)
        while len(stack) > 0:
            current_node = stack.pop()
            if current_node.right:
                stack.append(current_node.right)
            print(current_node.value)
            if current_node.left:
                stack.append(current_node.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
