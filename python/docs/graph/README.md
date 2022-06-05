# Graphs

A graph is a data structure that is made up of vertexes connected by edges that can be unidirectional or bidirectional.

## Challenge

The challenge was to create a graph class that could pass all of the tests.

## Approach & Efficiency

The largest big O efficenty for time and space is O(n) for this function. However, each method has it's own big O.

## API
<!-- Description of each method publicly available in your Graph -->
1. add_node - adds a vertex to the graph and returns the node added
2. add_edge - adds an edge between two nodes. The edge weight can be adjusted, but it defaulted to zero. arguments - (start_vertex, end_vertex, weight(optionl)). No return
3. get_nodes - No arguments. Returns a list of all of the nodes in the graph.
4. get_neighbors - arguments - (node). Returns a list of the nodes neighbors and edge weight in an Edge instantiation
5. size - No arguments. Returns the total number of nodes in the graph.
