from optparse import Values
from turtle import setundobuffer


class LinkedList:
    """
    Put docstring here
    """
    def __init__(self):
       self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)


    def __str__(self):
        current = self.head
        str = ""
        while current:
            str += f"{{ {current.value} }} -> "
            current = current.next
        str += "NULL"
        return str


    def includes(self, search_value):
        current = self.head
        while current:
            if current.value == search_value:
                return True
            current = current.next
        return False

    def append(self, new_node_value):
        '''
        Inserts a new Node at the end of the linked list.
        '''
        current = self.head
        while current:
            if current.next == None:
                current.next = Node(new_node_value)
                break
            current = current.next

    def insert_before(self, before, new_value):
        '''
        Inserts a new Node with the value of the second arg, before an existing Node with the value of the first arg.
        '''
        if self.head == None:
            raise TargetError
        inserted = False
        current = self.head
        if current.next == None and current.value == before:
            self.insert(new_value)
            inserted = True
        # if current.next != None:
        else:
            while current:
                try:
                    if current.next.value == before:
                        current.next = Node(new_value, current.next)
                        inserted = True
                        break
                    current = current.next
                except:
                    raise TargetError
        if inserted == False:
            raise TargetError

    def insert_after(self, after, new_value):
        '''
        Inserts a new Node with the value of the second parameter after the existing Node with the value of the first parameter.
        '''
        current = self.head
        if current == None:
            raise TargetError
        inserted = False
        while current:
            if current.value == after:
                current.next = Node(new_value, current.next)
                inserted = True
                break
            current = current.next
        if inserted == False:
            raise TargetError

    def kth_from_end(self, back_index):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        loop_count = length - back_index

        if back_index >= length:
            raise TargetError
        elif back_index < 0:
            raise TargetError

        current = self.head
        for i in range(loop_count):
            if i == loop_count - 1:
                return current.value
            current = current.next




class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_

class TargetError(Exception):
    pass
