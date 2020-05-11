from node import Node, LinkedList

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


class Stack:
    def __init__(self):
        # first node in the stack
        self.head = None
        # Stack size
        self.size = 0

    def __len__(self):
        return self.size

    # Check if stack is empty
    def empty(self):
        if self.size == 0 and not self.head:
            return True
        else:
            return False

    # Find top of stack
    def top(self):
        if not self.empty():
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            return current.get_value()
        else:
            return None

    def push(self, value):
        new_node = Node(value)

        # If empty, new node is head
        if self.empty():
            self.head = new_node
        # Else, put new node and tail of stack
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)

        self.size += 1

    def pop(self):
        # If stack is empty, return None
        if self.empty():
            return None

        # If stack size is 1, pop head and return its value
        elif self.size == 1:
            pop_value = self.head.value
            self.head = None
            self.size -= 1
            return pop_value

        # If the stack isn't empty, and its size > 1, pop last node in Stack
        # and return its value.
        else:
            current = self.head
            while current.next_node:
                if current.next_node.next_node is None:
                    pop_value = current.next_node.value
                    current.next_node = None
                    self.size -= 1
                    return pop_value
                else:
                    current = current.next_node
