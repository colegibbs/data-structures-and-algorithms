from data_structures.linked_list import LinkedList

class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size = 1024):
        # initialization here
        self.size = size
        self.buckets = [None] * self.size
        self.keys = []

    def set(self, key, value):
        index = self.hash(key)
        if self.buckets[index] == None:
            bucket = LinkedList()
            self.buckets[index] = bucket
        else:
            self.buckets[index].insert([key, value])

        if key in self.keys:
            current = self.buckets[index].head
            while current:
                if current.value[0] == key:
                    current.value[1] = value
                current = current.next
        else:
            self.keys.append(key)

        self.buckets[index].insert([key, value])


    def get(self):
        # method body here
        pass

    def contains(self):
        # method body here
        pass

    def keys(self):
        # method body here
        pass

    def hash(self, key):
        char_ord_sum = 0
        for char in key:
            char_ord_sum += ord(char)
        primified = char_ord_sum * 769
        index = primified % self.size
        return index
