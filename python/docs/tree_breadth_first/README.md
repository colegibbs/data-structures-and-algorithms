# Challenge Summary

Write a function called breadth_first that takes a tree as an argument and returns a list of the tree values in the order they were encountered; aka breadth order.

## Whiteboard Process

[Whiteboard](./code-challenge-17-whiteboard.png)

## Approach & Efficiency

I used a queue to save the Nodes in the order that I needed their values in.

Big O:

Time: O(n)
This function contains a while loop that works by iterating through the tree passed with a queue. The time depends on the number of nodes in the tree and has a time of O(n)

Space: O(n)
This function returns a list based on the number of Nodes in the tree passed. Because this list depends on the number of Nodes in the tree the space is O(n).

## Solution
<!-- Show how to run your code, and examples of it in action -->
Function use: breadth_first(tree)

Input: tree
		[2]
	[7]		[5]
[2]	  [6]		[9]
Output: [2, 7, 5, 2, 6, 9]
