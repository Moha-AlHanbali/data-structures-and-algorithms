import pytest

from navigator.navigator import Naviagtor
from navigator.stack import Stack
from navigator.node import Node

def test_navigator_back_empty():
    # Arrange
    navigator = Naviagtor()
    expected = None

    # Act
    actual = navigator.back()

    # Assert
    assert actual == expected


def test_navigator_forward_empty():
    # Arrange
    navigator = Naviagtor()
    expected = None

    # Act
    actual = navigator.back()

    # Assert
    assert actual == expected


def test_navigator_back(navigator):
    # Arrange
    expected = 2

    # Act
    actual = navigator.back()

    # Assert
    assert actual == expected


def test_navigator_forward(navigator):
    # Arrange
    expected = 4

    # Act
    actual = navigator.forward()

    # Assert
    assert actual == expected

def test_navigator_go(navigator):
    # Arrange
    expected = '5'

    # Act
    actual = navigator.go('5')

    # Assert
    assert actual == expected

@pytest.fixture
def navigator():
    navigator = Naviagtor()

    stack1 = Stack()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    stack1.push(node1)
    stack1.push(node2)
    stack1.push(node3)

    navigator.history = stack1

    stack2 = Stack()
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    stack2.push(node4)


    navigator.backtrack = stack2

    return navigator
