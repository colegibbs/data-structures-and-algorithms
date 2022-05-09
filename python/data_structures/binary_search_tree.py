from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def add(self, value):
        def traverse(root, add_value):
            if root == None:
                return

            if add_value.value < root.value:
                if root.left != None:
                    traverse(root.left, add_value)
                else:
                    root.left = add_value

            else:
                if root.right != None:
                    traverse(root.right, add_value)
                else:
                    root.right = add_value

        adding_node = Node(value)

        if self.root == None:
            self.root = adding_node
        else:
            traverse(self.root, adding_node)

    def contains(self, search_value):
        def traverse(root):
            if not root:
                return False

            if search_value == root.value:
                return True

            if search_value > root.value:
                traverse(root.right)

            if search_value < root.value:
                traverse(root.left)

            return False

        return traverse(self.root)



