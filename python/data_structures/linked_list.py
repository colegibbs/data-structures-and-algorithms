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



        # str = "NULL"
        # current = self.head
        # while current:
        #     if current.next:
        #         str = f"{{ {current.value} }} -> {{ {current.next.value} }} -> " + str
        #     else:
        #         if str == "NULL":
        #             str = f"{{ {current.value} }} -> " + str
        #     current = current.next
        # return str

    def includes(self, search_value):
        current = self.head
        while current:
            if current.value == search_value:
                return True
            current = current.next
        return False

    def append(self, new_node_value):
        '''
        traverse through the list until the current.next === None.
        set current.next to the new node.
        ser the next of the new node to None.
        '''
        current = self.head
        while current:
            if current.next == None:
                current.next = Node(new_node_value)
                break
            current = current.next

    def insert_before(self, before, new_value):
        '''
        - traverse through the list until current.next == before
        - if conidtion is met :
        set current.next == Node(new_value, current.next)
        - outside if current = current.next
        '''
        if self.head == None:
            raise TargetError
        current = self.head
        if current.next != None:
            while current:
                if current.next.value == before:
                    current.next = Node(new_value, current.next)
                    break
                current = current.next
        else:
            self.insert(new_value)



    def insert_after(self, after, new_value):
        '''
        inserts new Node with "new_value" after Node with paramater "after" as a value
        '''
        current = self.head
        while current:
            if current.value == after:
                current.next = Node(new_value, current.next)
                break
            current = current.next


class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_

class TargetError(Exception):
    pass
