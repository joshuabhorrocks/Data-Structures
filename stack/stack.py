"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.value = value
#         self.storage.append(value)

#     def pop(self):
#         if self.storage == []:
#             return None
#         else:
#             return self.storage.pop()

# Linked List

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next_node = next

    # def get_data(self):
    #     # returns the node's data 
    #     return self.data

    # def get_next(self):
    #     # returns the thing pointed at by this node's `next` reference 
    #     return self.next_node

    # def set_next(self, new_next):
    #     # sets this node's `next` reference to `new_next`
    #     self.next_node = new_next

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        total = 0
        current_node = self.head
        while current_node is not None:
            total = total + 1
            current_node = current_node.next_node
        return total

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next_node = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next_node
            return popped