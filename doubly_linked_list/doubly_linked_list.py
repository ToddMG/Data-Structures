"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if not self.head:
            return None
        else:
            value = self.head.value
            # If list only contains 1 node
            if self.length == 1:
                self.head = None
                self.tail = None
                self.length -= 1
            else:
                self.head = self.head.next
                self.head.prev = None
                self.length -= 1

        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if not self.tail:
            return None
        else:
            value = self.tail.value

            if self.length == 1:
                self.head = None
                self.tail = None
                self.length -= 1
            else:
                self.tail = self.tail.prev
                self.tail.next = None
                self.length -= 1

        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if not self.head or self.length == 1 or node is self.head:
            return None
        else:
            if node is self.tail:
                node.prev.next = None
                self.tail = node.prev
            else:
                node.next.prev = node.prev
                node.prev.next = node.next

            self.head.prev = node
            node.next = self.head
            node.prev = None
            self.head = node

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if not self.head or self.length == 1 or node is self.tail:
            return None
        else:
            if node is self.head:
                node.next.prev = None
                self.head = node.next
            else:
                node.next.prev = node.prev
                node.prev.next = node.next

            self.tail.next = node
            node.next = None
            node.prev = self.tail
            self.tail = node

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # Empty list
        if not self.head:
            return None
        # Node is head and tail
        elif node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        # Node is head
        elif node is self.head:
            node.next.prev = None
            self.head = node.next
        # Node is tail
        elif node is self.tail:
            node.prev.next = None
            self.tail = node.prev
        # Node is neither head or tail
        else:
            node.next.prev = node.prev
            node.prev.next = node.next

        self.length -= 1

    """Returns the highest value currently in the list"""
    def get_max(self):
        if not self.head:
            return None
        else:
            current = self.head
            max_val = current.value
            while current.next:
                current = current.next
                if current.value > max_val:
                     max_val = current.value

        return max_val


