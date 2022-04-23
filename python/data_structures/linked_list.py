class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
       self.head = None

    def insert(self, value):
        self.head = Node(value)

    def __str__(self):
        if self.head:
            return f"{{ {self.head.value} }} -> NULL"
        return "NULL"

class Node:
    def __init__(self, value):
        self.value = value

class TargetError:
    pass
