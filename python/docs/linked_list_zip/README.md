# Challenge Summary

Write a function called zip_lists that takes two linked lists as its arguments. This function will return the two linked listed zipped together. This means that the returned linked list will have alternating values from the linked lists that were given as parameters.

## Whiteboard Process

[Whiteboard](./code-challenge-8-whiteboard.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

I used pointers to save the refernces to previously liniked nodes

Big O:

time: O(n)
The time depends on the lengths of the two linked lists passed as arguments. As the length of the lists increase, so will the time it takes to loop through them.

space: O(1)
No new space is being allocated for this task. There is only a change in how the space is referenced to each other.

## Solution
<!-- Show how to run your code, and examples of it in action -->
- create two linked lists by instantating the LinkedList class
- pass your two lists as arguments as parameters to the function zip_lists()
- create a variable to save its return
- the vairable will contain a reference to the first item in the new zipped list
