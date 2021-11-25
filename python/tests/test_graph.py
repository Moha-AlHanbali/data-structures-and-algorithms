"""This module tests graph module"""

import pytest

from graph.graph import  Graph
from graph.vertex import Vertex


def test_add_vertex():
  graph = Graph()
  expected = "test"
  actual = graph.add_vertex('test').value
  assert actual == expected


def test_size_empty():

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected


def test_size():

    graph = Graph()

    graph.add_vertex('spam')

    expected = 1

    actual = graph.size()

    assert actual == expected


def test_add_edge_interloper_start():

    graph = Graph()

    start = Vertex('start')

    end = graph.add_vertex('end')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_add_edge_interloper_end():

    graph = Graph()

    end = Vertex('end')

    start = graph.add_vertex('start')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_get_vertices():

    graph = Graph()

    banana = graph.add_vertex('banana')

    apple = graph.add_vertex('apple')

    loner = Vertex('loner')

    expected = 2

    actual = len(graph.get_vertices())

    assert actual == expected


def test_get_vertices_single():

    graph = Graph()

    banana = graph.add_vertex('banana')

    expected = 1

    actual = len(graph.get_vertices())

    assert actual == expected


def test_get_neighbors():

    graph = Graph()

    banana = graph.add_vertex('banana')

    apple = graph.add_vertex('apple')

    graph.add_edge(apple, banana, 44)

    neighbors = graph.get_neighbors(apple)

    assert len(neighbors) == 1

    neighbor_edge = neighbors[0]

    assert neighbor_edge.vertex.value == 'banana'

    assert neighbor_edge.weight == 44
