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
from stack import Stack
from queue import Queue


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # Insert doesn't need return statement since it doesn't need to return and value our of the function.  recursion will just pop off in the call stack
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # if there is right node, run the for each again
        # if there is left node, run the for each again
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        # Lowest number is always the furthest to the left
        # base case:
        if node is None:
            return
        # if left is none & right is none
            # print node.value
        if node.left is None and node.right is None:
            print(node.value)
        # if left is none and right is not none
            # print node.value
            # point to right
        if node.left is None and node.right is not None:
            print(node.value)
            self.in_order_print(node.right)
        # if left is not none and right is none
            # point to node.left
            # print node.value
        if node.left is not None and node.right is None:
            self.in_order_print(node.left)
            print(node.value)
        # if left is not none and right is not none
            # point to node.left
            # print node.value
            # point to node.right
        if node.left is not None and node.right is not None:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # use a queue
        # start queue with root node
        queue = Queue()
        queue.enqueue(node)
        # while loop that checks size of queue
        # pointer variable that updates at the begining of each loop
        # while the queue exists, drop a node from the queue and print its value
        while queue.size > 0:
            node = queue.dequeue()
            print(node.value)
            # there is a left branch, add the left node to the queue
            if node.left:
                queue.enqueue(node.left)
            # same for the right
            if node.right:
                queue.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # stack
        # start stack with the root node
        stack = Stack()
        stack.push(node)
        # while loop that check stack size
        # pointer
        while stack.size > 0:
            node = stack.pop()
            print(node.value)
            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
