
class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
        self.root = None

    def pre_order(self):

        def traverse(root, node_values):
            if root == None:
                return

            node_values.append(root.value)
            traverse(root.left, node_values)
            traverse(root.right, node_values)

        all_values = []
        traverse(self.root, all_values)

        return all_values

    def in_order(self):
        def traverse(root, node_values):
            if root == None:
                return

            traverse(root.left, node_values)
            node_values.append(root.value)
            traverse(root.right, node_values)

        all_values = []
        traverse(self.root, all_values)

        return all_values

    def post_order(self):
        def traverse(root, node_values):
            if root == None:
                return

            traverse(root.left, node_values)
            traverse(root.right, node_values)
            node_values.append(root.value)

        all_values = []
        traverse(self.root, all_values)

        return all_values

    def find_maximum_value(self):
        def traverse(root, maximum):
            if root == None:
                return maximum
            if root.value > maximum:
                maximum = root.value
            maximum = traverse(root.left, maximum)
            maximum = traverse(root.right, maximum)
            return maximum
        if self.root == None:
            raise ValueError("This tree is empty.")
        return traverse(self.root, 0)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
