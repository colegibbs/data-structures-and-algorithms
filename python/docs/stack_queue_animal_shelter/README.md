# Challenge Summary

Problem Domain:

Create a class called AnimalShelter that has two methods. The first is enqueue. This method will add Nodes to correct queue based on the species of the animal it is passed. The second method is dequeue. This method will remove animals from the correct queue based on the species type that the user passes.

Enqueue
Input: animal as an instantiation of a class
Output: None
Result: the animal class passed is added to the correct queue

Dequeue
Input: species that should be removed from the species class
Output: the value of the Node removed
Result: the species specified by the user will have one Node removed from the queue

## Whiteboard Process

[Whiteboard](./code-challenge-12-whiteboard.png)

## Approach & Efficiency

Algorithm:

Enqueue

- if the class is a Cat class, then add it to the cat queue
- if the class is a Dog, then add it to the dog queue

Dequeue

- if the value passed is not "cat" or "dog" then return None
- if the value is "dog" then remove a node from the dog queue
- if the value is "cat" then remove a node from the cat queue

Big O:

Time: O(1)
The time for both methods is constant. There is only one action performed when a Node is removed from the queue

Space: 0(1)
The space for both functions is constant because it takes one action.

## Solution

- to add to the AnimalShelter class use `instantiation.enqueue(catOrDogInstantiation)`
- to remove from the AnimalShelter clas use `instatiation.deque("cat"Or"dog")`
