# Trees

Trees are another type of data structure that with a root Node the references two other Nodes. Each node can reference two other Nodes and creates the tree shape.

## Challenge

write a class for both a binary tree and a child class for a binary search tree. Allow for lists of the Node values in pre-order, in order, and post order form from respective methods. In the binary search tree, create an add method that will correctly add values to the tree. Also include a contains method that will return True or False based on wether or not a passed value is contained within the tree.

## Approach & Efficiency

Big O:
Time: O(n)
Space: O(n)
It takes time and space for the tree to be traversed and the list being returned to be appended to.

## API
<!-- Description of each method publicly available in each of your trees -->
- in_order -> returns a list of the Node values in order
- pre_order -> returns a list of the Node values in pre order
- post_order -> returns a list of the Node values in post order
- add -> adds a value to the tree based on its binary search location
- contains -> returns a boolean based on weather or not the value passed is in the tree or not
