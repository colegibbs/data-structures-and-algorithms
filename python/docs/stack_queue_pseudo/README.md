# Challenge Summary

Write a class called pseudo queue that contains an enqueue and dequeue method. This class will be a queue that is built of two stacks.

## Whiteboard Process

[Whiteboard](./code-challenge-11-whiteboard.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
For the Enqueue method I used the Stack class's push method to add the Nodes to the first stack. For the Dequeue method I moved all the Nodes from the first stack to the second. I then removed the last node on the second stack and returned it.

Big O:

Enqueue:

Time: O(1)
This method is constant time because it takes only one action to add to the top of the stack.
Space: O(1)
This method is constant space because you will always be adding one Node to the top of the stack.

Dequeue:

Time: O(n)
This method is linear time because the execution time depends on the the number of items in the original stack because they must be moved to the second stack.

Space: O(1)
This method is constant space because nothing is being added to the stack or duplicated to another stack. They are only being moved from one stack to another.

## Solution

- create a instance of PseudoQueue
- to add `value` -> `instance_name.enqueue(value)`
- to remove from the front of the queue -> `instance_name.dequeue()`

## Link To Code

[Code](https://github.com/colegibbs/data-structures-and-algorithms/blob/main/python/code_challenges/stack_queue_pseudo.py)
