from trees.node import Node
from trees.binary_tree import BinaryTree, BinarySearchTree
from trees.tree_breadth_first import breadth_first
from trees.kary_tree import KaryNode, KaryTree
from trees.tree_fizz_buzz import fizz_buzz
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
        assert tree.test_find_maximum_value_empty()

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



# Breadth First Tests
# -------------------------------------------------------------------

def test_breadth_first(tree):
    #Arrange
    expected = [1, 2, 3, 4, 5, 6]


    #Act
    actual = breadth_first(tree)

    #Assert
    assert actual == expected

def test_breadth_first_mixed(mixed_tree):
    #Arrange
    expected = ["a", 1, "b", 2, 3, 10, 4 ,5 ,6]


    #Act
    actual = breadth_first(mixed_tree)

    #Assert
    assert actual == expected

def test_breadth_first_bs_tree(bs_tree):
    #Arrange
    expected = [50, 40, 60, 30, 45, 55, 70, 20, 35, 65, 80]


    #Act
    actual = breadth_first(bs_tree)

    #Assert
    assert actual == expected


def test_breadth_first_empty():
    #Arrange
    tree = BinaryTree()

    #Assert
    with pytest.raises(Exception):
        assert test_breadth_first_empty(tree)




# K-ary Tree
# -------------------------------------------------------------------
def test_k_tree_create_tree():
    #Arrange
    tree = KaryTree(1)
    expected = None

    #Act
    actual = tree.traverse_kary_tree()

    #Assert
    assert actual == expected



def test_k_tree_add_root():
    #Arrange
    k_tree = KaryTree(1)
    k_tree.root = KaryNode(1)
    expected = 1

    #Act
    actual = k_tree.root.value

    #Assert
    assert actual == expected



def test_k_tree(k_tree):
    #Arrange
    expected = [5, 10, 33, 20, 15, 85, 80, "NO" , 1, 222, 131]


    #Act
    actual = k_tree.traverse_kary_tree()

    #Assert
    assert actual == expected


def test_k_tree_exceptions():
    #Arrange
    k_tree = KaryTree(1)

    #Assert
    with pytest.raises(Exception):
        assert k_tree.traverse_kary_tree()



# K-ary Tree FizzBuzz
# -------------------------------------------------------------------


def test_k_tree_fizz_buzz_values(k_tree):
    #Arrange
    expected = ["Buzz", "Buzz", "Fizz", "Buzz", "FizzBuzz", "Buzz", "Buzz", "NO" , "1", "Fizz", "131"]

    #Act
    actual = fizz_buzz(k_tree)


    #Assert
    assert actual == expected


def test_k_tree_fizz_buzz():
    #Arrange
    k_tree = KaryTree(1)

    #Assert
    with pytest.raises(Exception):
        assert k_tree.traverse_kary_tree()


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


@pytest.fixture
def k_tree():

    node5 = KaryNode(5)

    node10 = KaryNode(10)
    node33 = KaryNode(33)
    node20 = KaryNode(20)

    node15 = KaryNode(15)
    node85 = KaryNode(85)
    node80 = KaryNode(80)

    node1 = KaryNode(1)
    node222 = KaryNode(222)
    node131 = KaryNode(131)

    nodeNO = KaryNode("NO")

    node5.children.append(node10)
    node5.children.append(node33)
    node5.children.append(node20)

    node10.children.append(node15)
    node10.children.append(node85)
    node10.children.append(node80)

    node80.children.append(node1)
    node80.children.append(node222)
    node80.children.append(node131)

    node20.children.append(nodeNO)

    k_tree = KaryTree(3)
    k_tree.root = node5

    return k_tree
