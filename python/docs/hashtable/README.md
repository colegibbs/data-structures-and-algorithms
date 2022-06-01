# Hashtables

A hashtable is an way of storing information in a structure that can be conceptiualized as a list without the need for looping through do to available indexes.

## Challenge

Implement a Hashtable class with methods set, get, contains, keys, and hash.

## Approach & Efficiency

I implement the methods as need. When I encounted a linked list, I loop through it. This only occurs in collision cases. different methods will have different efficiencies.

## API

1. set() takes a key and value as arguments; returns nothing; this method sets the key, value pair in the hashtable; if the key already exists it will be replaced.
2. get() takes in a key as an argument; returns the value of the key; if the key does not exit, the method will return None.
3. contains() takes in a key as an argument; returns a boolean based on the existence of the key in the hashtable.
4. keys() takes no arguments; returns a list of all of the keys in the hashtable.
5. hash() takes a key as an argument; returns the index for the key in the correct range.
