from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.front = None
        self.back = None

    def enqueue(self, value):
        # method body here
        node = Node(value)

        if self.back:
            self.back.next = node

        self.back = node

        if self.front == None:
            self.front = self.back

    def dequeue(self):
        if self.front == None:
            raise InvalidOperationError

        old_front = self.front
        self.front = old_front.next
        old_front.next = None
        return old_front.value

    def peek(self):
        if self.front == None:
            raise InvalidOperationError
        return self.front.value

    def is_empty(self):
        if self.front == None:
            return True
        else:
            return False

