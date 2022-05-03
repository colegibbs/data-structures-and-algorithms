from data_structures.linked_list import TargetError
from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.first = Stack()
        self.second = Stack()

    def enqueue(self, value):
        if self.second.top != None:
            while self.second.top:
                self.first.push(self.second.pop())

        self.first.push(value)

    def dequeue(self):
        if self.first.top == None and self.second.top == None:
            raise TargetError("Method cannot be called on an empty queue.")
        if self.first.top == None:
            while self.second.top:
                self.first.push(self.second.pop())

        while self.first.top:
            self.second.push(self.first.pop())

        return self.second.pop()
