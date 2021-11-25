"""This module contains Edge class"""


from graph.vertex import Vertex


class Edge:
    """
    Edge class creates Edge instances.

    Arguments:

        vertex: a Vertex instance
        weight: an integer
    """

    def __init__(self, vertex: Vertex, weight = 0):
        self.vertex = vertex
        self.weight = weight
