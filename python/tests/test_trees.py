from trees.node import Node
from trees.binary_tree import BinaryTree, BinarySearchTree
import pytest





# Trees Tests
# -------------------------------------------------------------------

def test_tree_create_tree():
    #Arrange
    tree = BinaryTree()
    expected = []

    #Act
    actual = tree.pre_order()

    #Assert
    assert actual == expected



def test_tree_add_root():
    #Arrange
    tree = BinaryTree()
    tree.root = Node(1)
    expected = 1

    #Act
    actual = tree.root.value

    #Assert
    assert actual == expected

def test_tree_add_children():
    #Arrange
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)

    expected_1 = 2
    expected_2 = 3


    #Act
    actual_1 = tree.root.left.value
    actual_2 = tree.root.right.value

    #Assert
    assert actual_1 == expected_1
    assert actual_2 == expected_2



def test_tree_pre_order(tree):
    #Arrange
    expected = [1, 2, 3 ,4, 5, 6]


    #Act
    actual = tree.pre_order()

    #Assert
    assert actual == expected


def test_tree_in_order(tree):
    #Arrange
    expected = [2, 1, 4, 3, 6, 5]


    #Act
    actual = tree.in_order()

    #Assert
    assert actual == expected


def test_tree_post_order(tree):
    #Arrange
    expected = [2, 4, 6, 5, 3, 1]


    #Act
    actual = tree.post_order()

    #Assert
    assert actual == expected


def test_tree_exceptions(tree):
    #Arrange
    tree = BinaryTree()

    #Assert
    with pytest.raises(Exception):
        assert tree.post_order()


# Binary Search Trees Tests
# -------------------------------------------------------------------

def test_bs_tree_add(bs_tree):
    #Arrange

    expected = 1

    #Act
    node = bs_tree.add(1)
    actual = node.value

    #Assert
    assert actual == expected


def test_bs_contain_add(bs_tree):
    #Arrange

    expected = True

    #Act
    bs_tree.add(1)
    actual = bs_tree.contain(1)

    #Assert
    assert actual == expected

def test_bs_not_contain(bs_tree):
    #Arrange

    expected = False

    #Act
    actual = bs_tree.contain(1)

    #Assert
    assert actual == expected

def test_bs_contain_right(bs_tree):
    #Arrange

    expected = True

    #Act
    actual = bs_tree.contain(80)

    #Assert
    assert actual == expected

def test_bs_add_correct_location(bs_tree):
    #Arrange

    expected = 100

    #Act
    bs_tree.add(100)
    actual = bs_tree.root.right.right.right.right.value

    #Assert
    assert actual == expected

def test_bs_add_empty():
    #Arrange
    bs_tree = BinarySearchTree()
    expected = 1

    #Act
    bs_tree.add(1)
    actual = bs_tree.root.value

    #Assert
    assert actual == expected



# Find Maximum Value Tests
# -------------------------------------------------------------------

def test_find_maximum_value_empty():
    #Arrange
    tree = BinaryTree()

    #Assert
    with pytest.raises(Exception):
        assert tree.post_order()

def test_find_maximum_value_none_numbers(tree):
    #Arrange
    expected = 6

    #Act
    actual = tree.find_maximum_value()

    #Assert
    assert actual == expected


def test_find_maximum_value_none_numbers(mixed_tree):
    #Arrange
    expected = 10

    #Act
    actual = mixed_tree.find_maximum_value()

    #Assert
    assert actual == expected

def test_find_maximum_value_bst(bs_tree):
    #Arrange
    expected = 80

    #Act
    actual = bs_tree.find_maximum_value()

    #Assert
    assert actual == expected

def test_find_maximum_value_bst_added_value(bs_tree):
    #Arrange
    expected = 100
    bs_tree.add(100)

    #Act
    actual = bs_tree.find_maximum_value()

    #Assert
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
def bs_tree():

    node50 = Node(50)

    node45 = Node(45)
    node40 = Node(40)
    node35 = Node(35)
    node30 = Node(30)
    node20 = Node(20)

    node80 = Node(80)
    node70 = Node(70)
    node65 = Node(65)
    node60 = Node(60)
    node55 = Node(55)


    node50.left = node40
    node50.right = node60

    node40.left = node30
    node40.right = node45

    node30.left = node20
    node30.right = node35

    node60.left = node55
    node60.right = node70

    node70.left = node65
    node70.right = node80

    bs_tree = BinarySearchTree()
    bs_tree.root = node50

    return bs_tree
