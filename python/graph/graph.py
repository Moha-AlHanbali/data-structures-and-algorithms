"""This module contains Graph class"""

from graph.vertex import Vertex
from graph.edge import Edge
from graph.queue import Queue
from graph.stack import Stack



class Graph:
    """
    Graph class creates Graph instances.

    Arguments:None

    Methods:

        size

            This method returns the length of the graph.

            Arguments: None

            Return: int


        add_vertex

            This method adds a vertex to the graph.

            Arguments: vertex value

            Return: vertex


        add_edge

            This method adds an edge between two graph vertices.

            Arguments:
                start_vertex: Vertex
                end_vertex: Vertex
                weight: int

            Return: None

        get_vertices

            This method returns graph vertices

            Arguments: None

            Return: list of keys

        get_neighbors

            This method returns vertix neighbors

            Arguments: vertex

            Return: list of vertices

        breadth_first_search

            This method traverses a graph in breadth first order performing an action on each vertex.

            Arguments:

                start_vertex: Vertex

                action: a function

            Return: None


        depth_first_search

            This method traverses a graph in depth first order performing an action on each vertex.

            Arguments:

                start_vertex: Vertex

                action: a function

            Return: None
    """
    def __init__(self):
        self.__adjacency_list = dict()


    def size(self):
        return len(self.__adjacency_list)


    def add_vertex(self, value):
        vertex = Vertex(value)
        self.__adjacency_list[vertex] = []
        return vertex


    def add_edge(self, start_vertex, end_vertex, weight = 0):
        if start_vertex not in self.__adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self.__adjacency_list:
            raise KeyError("End Vertex not found in graph")

        edge = Edge(end_vertex , weight)
        self.__adjacency_list[start_vertex].append(edge)


    def get_vertices(self):
        return self.__adjacency_list.keys()


    def get_neighbors(self, vertex):
        return self.__adjacency_list.get(vertex, [])


    def breadth_first_search(self, start_vertex):
        try:
            vertices= []
            queue = Queue()
            visited = set()

            queue.enqueue(start_vertex)
            visited.add(start_vertex)

            while len(queue):

                current_vertex = queue.dequeue()

                vertices +=  [current_vertex.value]

                neighbors = self.get_neighbors(current_vertex)
                for edge in neighbors:
                    neighbor = edge.vertex

                    if neighbor not in visited:
                        visited.add(neighbor)

                        queue.enqueue(neighbor)

            return vertices

        except:
            raise Exception("Pease check your inputs and try again.")


    #NOTE: ALTERNATIVE TO PERFORM ACTIONS ON EACH GRAPH VERTEX
    # def breadth_first_search(self, start_vertex, action = (lambda vertes:None)):

    #     queue = Queue()
    #     visited = set()

    #     queue.enqueue(start_vertex)
    #     visited.add(start_vertex)

    #     while len(queue):
    #         current_vertex = queue.dequeue()
    #         action(current_vertex)

    #         neighbors = self.get_neighbors(start_vertex)
    #         for edge in neighbors:
    #             neighbor = edge.vertex

    #             if neighbor not in visited:
    #                 visited.add(neighbor)
    #                 queue.enqueue(neighbor)


    def depth_first_search(self, start_vertex):

        try:
            vertices= []
            stack = Stack()
            visited = set()

            stack.push(start_vertex)
            while len(stack):
                current_vertex = stack.pop()

                if current_vertex not in visited:
                    visited.add(current_vertex)
                    vertices += [current_vertex.value]

                    neighbors = self.get_neighbors(current_vertex)

                    for edge in neighbors:
                        neighbor = edge.vertex
                        if neighbor not in visited:
                            stack.push(neighbor)

            return vertices

        except:
            raise Exception("Pease check your inputs and try again.")


    #NOTE: ALTERNATIVE TO PERFORM ACTIONS ON EACH GRAPH VERTEX
    # def depth_first_search(self, start_vertex, action = (lambda vertes:None)):
        # vertices= []
        # stack = Stack()
        # visited = set()

        # stack.push(start_vertex)
        # while len(stack):
        #     current_vertex = stack.peek()

        #     if current_vertex not in visited:
        #         visited.add(current_vertex)
        #         action(current_vertex)

        #         neighbors = self.get_neighbors(current_vertex)

        #         for edge in neighbors:
        #             neighbor = edge.vertex
        #             if neighbor not in visited:
        #                 stack.push(neighbor)


        #     else:
        #         stack.pop()

        # return vertices

    def connected_vertices(self, start_vertex, end_vertix, adjacency_list):
        try:

            if end_vertix in adjacency_list[start_vertex]:
                return True

            queue = Queue()
            visited = set()

            queue.enqueue(start_vertex)
            visited.add(start_vertex)

            while len(queue):

                current_vertex = queue.dequeue()

                for neighbor in adjacency_list[current_vertex]:

                    if neighbor is end_vertix:
                        return True

                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.enqueue(neighbor)

            return False

        except:
            raise Exception("Pease check your inputs and try again.")


# graph = Graph()

# vertex_1 = graph.add_vertex(1)

# vertex_2 = graph.add_vertex(2)

# vertex_3 = graph.add_vertex(3)

# vertex_4 = graph.add_vertex(4)

# vertex_5 = graph.add_vertex(5)

# vertex_6 = graph.add_vertex(6)

# graph.add_edge(vertex_1,vertex_5)

# graph.add_edge(vertex_1,vertex_2)

# graph.add_edge(vertex_1,vertex_3)

# graph.add_edge(vertex_5,vertex_3)

# graph.add_edge(vertex_3,vertex_4)

# a_l = {
#        vertex_1:[vertex_2, vertex_3, vertex_5],
#        vertex_2:[vertex_1],
#        vertex_5:[vertex_1, vertex_3],
#        vertex_3:[vertex_1,vertex_5, vertex_4],
#        vertex_4:[vertex_3],
#        }


# print(graph.connected_vertices(vertex_1, vertex_4, a_l))
# print(graph.connected_vertices(vertex_1, vertex_6, a_l))
