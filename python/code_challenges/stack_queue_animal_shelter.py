from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.cat_queue = Queue()
        self.dog_queue = Queue()

    def enqueue(self, animal):
        if isinstance(animal, Cat):
            self.cat_queue.enqueue(animal)
        elif isinstance(animal, Dog):
            self.dog_queue.enqueue(animal)

    def dequeue(self, species):
        if species != "cat" and species != "dog":
            return None
        elif species == "cat":
            removed = self.cat_queue.dequeue()
        elif species == "dog":
            removed = self.dog_queue.dequeue()

        return removed


class Dog:
    pass


class Cat:
    pass
