# Stacks and Queues

I created a Stack and Queue with the appropriate methods and properties. A stack is a data structure that behaves the same way as the call stack. A queue behaves like a line would. You can only see the top/front of these data structures.

## Challenge

In this assignment I create classes that have Stack and Queue behaviors.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Stack:
  push method: Time - 0(1), Space - O(1)
  pop method: Time - O(1), Space - O(1)
  is_empty: Time - O(1), Space - O(1)
  peek: Time - O(1), Space - O(1)

Queue:
  push method: Time - 0(1), Space - O(1)
  pop method: Time - O(1), Space - O(1)
  is_empty: Time - O(1), Space - O(1)
  peek: Time - O(1), Space - O(1)

## API
<!-- Description of each method publicly available to your Stack and Queue-->
### pop
- removes a Node from the top of the Stack or the front of the Queue
- Syntax: Stack.pop() or Queue.pop()

## push
- adds a Node to the top of the Stack or the back of the Queue
- Syntax: Stack.push(node_added_value) or Queue.push(node_added_value)

## is_empty

- returns a boolean based on wether the Stack or Queue is empty
- Syntax: Stack.is_empty() or Queue.is_empty()

## peek

- return the value of the Node at the top of the Stack or the front of the Queue
- Syntax: Stack.peek() or Queue.peek()
