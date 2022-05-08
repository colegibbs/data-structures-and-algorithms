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


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
