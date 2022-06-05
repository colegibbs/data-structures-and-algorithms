from multiprocessing.sharedctypes import Value


class Graph:
    """
    Put docstring here
    """

    def __init__(self):
        self.adjacent_list = {}

    def add_node(self, value):
        node = Vertex(value)
        self.adjacent_list[node] = []
        return node

    def size(self):
        return len(self.adjacent_list)

    def add_edge(self, start, end, weight = 0):
        if start in self.adjacent_list and end in self.adjacent_list:
            edge = Edge(end, weight)
            self.adjacent_list[start].append(edge)
        else:
            raise KeyError

    def get_neighbors(self, vertex):
        return self.adjacent_list[vertex]

    def get_nodes(self):
        return self.adjacent_list.keys()


class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
