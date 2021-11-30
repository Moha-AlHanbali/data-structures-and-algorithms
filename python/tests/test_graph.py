"""This module tests graph module"""

import pytest

from graph.graph import  Graph
from graph.vertex import Vertex
from graph.business_trip import business_trip

# Test Graph
# ------------------------------------------------
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


# Test breadth_first_search
# ------------------------------------------------

def test_breadth_first_search_case1(simple_graph):
    # Arrange
    expected = [1, 5 ,2 ,3, 4]

    # Act
    actual = simple_graph[0].breadth_first_search(simple_graph[1])

    # Assert
    assert actual == expected


def test_breadth_first_search_case2(example_graph):
    # Arrange
    expected = ['Pandora', 'Arandelle', 'Metroville', 'Monstropolis', 'Naboo', 'Narnia']

    # Act
    actual = example_graph[0].breadth_first_search(example_graph[1])

    # Assert
    assert actual == expected

def test_breadth_first_search_single():
    # Arrange
    graph = Graph()
    vertex_1 = graph.add_vertex(1)

    expected = [1]

    # Act
    actual = graph.breadth_first_search(vertex_1)

    # Assert
    assert actual == expected

def test_breadth_first_search_empty():
    # Arrange
    graph = Graph()

    # Assert
    with pytest.raises(Exception):
        graph.breadth_first_search(vertex_1)


# Test business_trip
# ------------------------------------------------
def test_business_trip(travel_graph):
    # Arrange
    expected = '$82'

    # Act
    actual = business_trip(travel_graph[0], travel_graph[1])

    # Assert
    assert actual == expected


def test_business_trip_case2(travel_graph):
    # Arrange
    expected = '$115'

    # Act
    actual = business_trip(travel_graph[0], travel_graph[2])

    # Assert
    assert actual == expected

def test_business_trip_none(travel_graph):
    # Arrange
    expected = None

    # Act
    actual = business_trip(travel_graph[0], travel_graph[3])

    # Assert
    assert actual == expected


def test_business_trip_none2(travel_graph):
    # Arrange
    expected = None

    # Act
    actual = business_trip(travel_graph[0], travel_graph[4])

    # Assert
    assert actual == expected

def test_business_trip_none_transit(travel_graph):
    # Arrange
    expected = None

    # Act
    actual = business_trip(travel_graph[0], travel_graph[5])

    # Assert
    assert actual == expected

def test_business_trip_error():
    # Arrange
    graph = Graph()

    # Assert
    with pytest.raises(Exception):
        graph.business_trip(graph, [])


# Test depth_first_search
# ------------------------------------------------

def test_depth_first_search_example(depth_graph):
    # Arrange
    expected = ['a', 'b', 'c', 'g', 'd', 'e', 'h', 'f']

    # Act
    actual = depth_graph[0].depth_first_search(depth_graph[1])

    # Assert
    assert actual == expected


def test_depth_first_search_single():
    # Arrange
    graph = Graph()
    vertex_1 = graph.add_vertex(1)

    expected = [1]

    # Act
    actual = graph.depth_first_search(vertex_1)

    # Assert
    assert actual == expected

def test_depth_first_search_empty():
    # Arrange
    graph = Graph()

    # Assert
    with pytest.raises(Exception):
        graph.depth_first_search(vertex_1)


# Fixtures
# ------------------------------------------------
@pytest.fixture
def simple_graph():
    graph = Graph()

    vertex_1 = graph.add_vertex(1)

    vertex_2 = graph.add_vertex(2)

    vertex_3 = graph.add_vertex(3)

    vertex_4 = graph.add_vertex(4)

    vertex_5 = graph.add_vertex(5)

    graph.add_edge(vertex_1,vertex_5)

    graph.add_edge(vertex_1,vertex_2)

    graph.add_edge(vertex_1,vertex_3)

    graph.add_edge(vertex_5,vertex_3)

    graph.add_edge(vertex_3,vertex_4)

    return graph, vertex_1

@pytest.fixture
def example_graph():
    graph = Graph()

    pandora = graph.add_vertex('Pandora')
    arandelle = graph.add_vertex('Arandelle')
    metroville = graph.add_vertex('Metroville')
    monstropolis = graph.add_vertex('Monstropolis')
    narnia = graph.add_vertex('Narnia')
    naboo = graph.add_vertex('Naboo')

    graph.add_edge(pandora, arandelle)
    graph.add_edge(arandelle, pandora)

    graph.add_edge(arandelle, metroville)
    graph.add_edge(metroville, arandelle)

    graph.add_edge(arandelle, monstropolis)
    graph.add_edge(monstropolis, arandelle)

    graph.add_edge(metroville, naboo)
    graph.add_edge(naboo, metroville)

    graph.add_edge(monstropolis, naboo)
    graph.add_edge(naboo, monstropolis)

    graph.add_edge(metroville, narnia)
    graph.add_edge(narnia, metroville)

    graph.add_edge(narnia, naboo)
    graph.add_edge(naboo, narnia)

    return graph, pandora



@pytest.fixture
def travel_graph():
    graph = Graph()

    pandora = graph.add_vertex('Pandora')
    arendelle = graph.add_vertex('Arendelle')
    metroville = graph.add_vertex('Metroville')
    monstropolis = graph.add_vertex('Monstropolis')
    narnia = graph.add_vertex('Narnia')
    naboo = graph.add_vertex('Naboo')

    graph.add_edge(pandora, arendelle, 150)
    graph.add_edge(arendelle, pandora, 150)

    graph.add_edge(pandora, metroville, 82)
    graph.add_edge(metroville, pandora, 82)

    graph.add_edge(arendelle, metroville, 99)
    graph.add_edge(metroville, arendelle, 99)

    graph.add_edge(arendelle, monstropolis, 42)
    graph.add_edge(monstropolis, arendelle, 42)

    graph.add_edge(metroville, monstropolis, 105)
    graph.add_edge(monstropolis, metroville, 105)

    graph.add_edge(metroville, naboo, 26)
    graph.add_edge(naboo, metroville, 26)

    graph.add_edge(monstropolis, naboo, 73)
    graph.add_edge(naboo, monstropolis, 73)

    graph.add_edge(metroville, narnia, 37)
    graph.add_edge(narnia, metroville, 37)

    graph.add_edge(narnia, naboo, 250)
    graph.add_edge(naboo, narnia, 250)

    list1 = [metroville, pandora]
    list2 = [arendelle, monstropolis, naboo]
    list3 = [naboo, pandora]
    list4 = [narnia, arendelle, naboo]
    list5 = [narnia, naboo, pandora]

    return graph, list1, list2, list3, list4, list5


@pytest.fixture
def depth_graph():

    graph = Graph()

    vertex_a = graph.add_vertex('a')

    vertex_b = graph.add_vertex('b')

    vertex_c = graph.add_vertex('c')

    vertex_d = graph.add_vertex('d')

    vertex_e = graph.add_vertex('e')

    vertex_f = graph.add_vertex('f')

    vertex_g = graph.add_vertex('g')

    vertex_h = graph.add_vertex('h')

    graph.add_edge(vertex_a, vertex_d)
    graph.add_edge(vertex_d, vertex_a)

    graph.add_edge(vertex_b, vertex_d)
    graph.add_edge(vertex_d, vertex_b)

    graph.add_edge(vertex_d, vertex_f)
    graph.add_edge(vertex_f, vertex_d)

    graph.add_edge(vertex_d, vertex_h)
    graph.add_edge(vertex_h, vertex_d)

    graph.add_edge(vertex_d, vertex_e)
    graph.add_edge(vertex_e, vertex_d)

    graph.add_edge(vertex_f, vertex_h)
    graph.add_edge(vertex_h, vertex_f)

    graph.add_edge(vertex_a, vertex_b)
    graph.add_edge(vertex_b, vertex_a)

    graph.add_edge(vertex_b, vertex_c)
    graph.add_edge(vertex_c, vertex_b)

    graph.add_edge(vertex_c, vertex_g)
    graph.add_edge(vertex_g, vertex_c)

    return graph, vertex_a
