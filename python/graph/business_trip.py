"""This module contains business_trip function"""

from graph.graph import Graph

def business_trip(graph, array):
    """
    business_trip calculates if trips between cities are possible and calculates their total cost.

    Arguments:
        graph: graph of available flights and their costs
        array: an array containing destinations

    Return: Str, the cost or None
    """
    try:
        cost = 0
        for city in range(len(array)):
            edges = graph.get_neighbors(array[city])

            if city + 1 <= len(array) -1:

                cost_check = cost

                for neighbor in edges:
                    if array[city + 1] == neighbor.vertex:
                        cost += neighbor.weight

                if cost == cost_check:
                    return None

        return f'${cost}'

    except:
        raise Exception("Please check your inputs and try again.")
