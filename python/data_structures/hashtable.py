from data_structures.linked_list import LinkedList

class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size = 1024):
        # initialization here
        self.size = size
        self.buckets = [None] * self.size
        self.keys_list = []

    def set(self, key, value):
        index = self.hash(key)
        if self.buckets[index] == None:
            bucket = LinkedList()
            self.buckets[index] = bucket
        else:
            self.buckets[index].insert([key, value])

        if key in self.keys_list:
            current = self.buckets[index].head
            while current:
                if current.value[0] == key:
                    current.value[1] = value
                current = current.next
        else:
            self.keys_list.append(key)

        self.buckets[index].insert([key, value])


    def get(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        if bucket == None:
            return None
        else:
            current = bucket.head
            while current:
                if current.value[0] == key:
                    return current.value[1]
                current = current.next

    def contains(self, key):
        if self.get(key) == None:
            return False
        else:
            return True

    def keys(self):
        return self.keys_list

    def hash(self, key):
        char_ord_sum = 0
        for char in key:
            char_ord_sum += ord(char)
        primified = char_ord_sum * 769
        index = primified % self.size
        return index
