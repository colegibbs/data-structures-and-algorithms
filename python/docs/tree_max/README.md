# Challenge Summary

Write a method inside of the binary tree class that returns the max value in the tree. Assume that all values are numbers.

## Whiteboard Process

[Whiteboard](./code-challenge-16-whiteboard.png)

## Approach & Efficiency

Big O:

Time: O(n)
In order to find the largest value with this algorithm, the tree must be traversed which means the time it will take depends on how many Nodes are in the tree.

Space: O(1)
One variable is being saved and no matter how many Nodes exist in the tree, there will always be only one variable saved.

## Solution
<!-- Show how to run your code, and examples of it in action -->
- instantiate BinaryTree class
- to use the method: BinaryTree.find_maximum_value()
