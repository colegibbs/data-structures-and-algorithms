# Challenge Summary

Write a function called validate_brackets that accepts a string as parameter and returns a boolean based on wether or not the brackets in the string are have an opening and closing bracket and are in the correct order.

## Whiteboard Process

[whiteboard](code-challenge-13-whiteboard.png)

## Approach & Efficiency

I could not figure out how to use a stack for this problem. It seemed better to me while writting the code to do it without a stack.

Big O:

Time: O(n)
The time depends on the length of the string that the for loop is looping through

Space: O(n)
The space is dependent on how many opening brackets are in the string. Even though they are removed in ideal situations, it still takes an O(n) space to add them to the list.

## Solution

- Put a string in the parameters of this function to validate if the brackets are balanced and in the right order. A boolean will be returned.
- Syntax: `multi_bracket_validation(string)`

## Link to [Code](https://github.com/colegibbs/data-structures-and-algorithms/blob/main/python/code_challenges/stack_queue_brackets.py)
