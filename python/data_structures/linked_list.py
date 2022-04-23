class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
       self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)


    def __str__(self):
        str = "NULL"
        current = self.head
        while current:
            if current.next:
                str = f"{{ {current.value} }} -> {{ {current.next.value} }} -> " + str
            else:
                if str == "NULL":
                    str = f"{{ {current.value} }} -> " + str
            current = current.next
        return str

    def includes(self, search_value):
        current = self.head
        while current:
            if current.value == search_value:
                return True
            current = current.next
        return False

class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_

class TargetError:
    pass
