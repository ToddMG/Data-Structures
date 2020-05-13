from node import Node

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


class Queue:
    def __init__(self):
        # first node in the stack
        self.head = None
        # Stack size
        self.size = 0

    def __len__(self):
        return self.size

    # Check if queue is empty
    def empty(self):
        if self.size == 0 and not self.head:
            return True
        else:
            return False

    # Return queue head
    def front(self):
        if not self.empty():
            return self.head
        else:
            return None

    # Add new node
    def enqueue(self, value):
        # Create new node
        new_node = Node(value)

        # If queue empty, set head to new node
        if self.empty():
            self.head = new_node
        # Else, find last node and add new node to tail
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)

        self.size += 1

    # Remove first node
    def dequeue(self):
        # If empty do nothing
        if self.empty():
            return None

        # If not empty, set new head to next node and remove current head
        else:
            current = self.head
            self.head = current.get_next()
            self.size -= 1
            return current.value
