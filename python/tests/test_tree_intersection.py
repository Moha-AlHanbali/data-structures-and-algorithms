"""This module tests tree_intersection function"""

import pytest

from trees.node import Node
from trees.binary_tree import BinaryTree
from tree_intersection.tree_intersection import tree_intersection


def test_tree_intersection_full(tree):
    # Arrange
    expected = {1,2,3,4,5,6}

    # Act
    actual = tree_intersection(tree, tree)

    # Assert
    assert actual == expected


def test_tree_intersection_case_1(tree, tree2):
    # Arrange
    expected = {2,4,6}

    # Act
    actual = tree_intersection(tree, tree2)

    # Assert
    assert actual == expected



def test_tree_intersection_None(tree, tree3):
    # Arrange
    expected = {}

    # Act
    actual = tree_intersection(tree, tree3)

    # Assert
    assert actual == expected


def test_tree_intersection_characters(tree, mixed_tree):
    # Arrange
    expected = {1, 2, 3, 4, 5, 6}

    # Act
    actual = tree_intersection(tree, mixed_tree)

    # Assert
    assert actual == expected

def test_tree_intersection_empty_tree(tree):
    # Arrange
    empty_tree = BinaryTree()

    # Assert
    with pytest.raises(Exception):
        assert tree_intersection(tree, empty_tree)

def test_tree_intersection_example_trees(example_1, example_2):
    # Arrange
    expected = {100,160,125,175,200,350,500}

    # Act
    actual = tree_intersection(example_1, example_2)

    # Assert
    assert actual == expected

# Fixtures
# -------------------------------------------------------------------
@pytest.fixture
def tree():
    node = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    node.left = node2
    node.right = node3
    node3.left = node4
    node3.right = node5
    node5.left = node6

    tree = BinaryTree()
    tree.root = node

    return tree

@pytest.fixture
def tree2():
    node2 = Node(2)
    node4 = Node(4)
    node6 = Node(6)

    node2.left = node4
    node2.right = node6


    tree2 = BinaryTree()
    tree2.root = node2

    return tree2

@pytest.fixture
def tree3():
    node9 = Node(9)
    node10 = Node(10)
    node12 = Node(12)

    node10.left = node9
    node10.right = node12


    tree3 = BinaryTree()
    tree3.root = node10

    return tree3

@pytest.fixture
def mixed_tree():
    node = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node10 = Node(10)
    nodea = Node("a")
    nodeb = Node("b")


    nodea.left = node
    nodea.right = nodeb
    nodeb.right = node10
    node.left = node2
    node.right = node3
    node3.left = node4
    node3.right = node5
    node5.left = node6

    mixed_tree = BinaryTree()
    mixed_tree.root = nodea

    return mixed_tree

@pytest.fixture
def example_1():
    node150 = Node(150)
    node100 = Node(100)
    node75 = Node(75)
    node160 = Node(160)
    node125 = Node(125)
    node175 = Node(175)
    node250 = Node(250)
    node200 = Node(200)
    node350 = Node(350)
    node300 = Node(300)
    node500 = Node(500)


    node150.left = node100
    node100.left = node75
    node100.left = node160
    node160.left = node125
    node160.right = node175
    node150.right = node250
    node250.left = node200
    node250.right = node350
    node350.left = node300
    node350.right = node500

    example_tree1 = BinaryTree()
    example_tree1.root = node150

    return example_tree1

@pytest.fixture
def example_2():
    node42 = Node(42)
    node100 = Node(100)
    node15 = Node(15)
    node160 = Node(160)
    node125 = Node(125)
    node175 = Node(175)
    node600 = Node(600)
    node200 = Node(200)
    node350 = Node(350)
    node4 = Node(4)
    node500 = Node(500)

    node42.left = node100
    node100.left = node15
    node100.right = node160
    node160.left = node125
    node125.right = node175
    node42.right = node600
    node600.left = node200
    node600.right = node350
    node350.left = node4
    node350.right = node500


    example_tree2 = BinaryTree()
    example_tree2.root = node42

    return example_tree2
