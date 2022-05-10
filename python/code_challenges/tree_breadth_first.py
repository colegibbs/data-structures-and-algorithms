from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    if tree.root == None:
        return []
    tree_queue = Queue()
    tree_queue.enqueue(tree.root)
    values = []
    while not tree_queue.is_empty():
        front = tree_queue.dequeue()
        values.append(front.value)
        if front.left:
            tree_queue.enqueue(front.left)
        if front.right:
            tree_queue.enqueue(front.right)
    return values
