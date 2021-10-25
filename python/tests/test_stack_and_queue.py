from stack_and_queue.node import Node
from stack_and_queue.stack import Stack
from stack_and_queue.queue import Queue
from stack_and_queue.pseudo_queue import PseudoQueue
import pytest




def test_node_created():
    # Arrange
    expected = "Test_Value"

    # Act
    actual = Node("Test_Value").value

    # Assert
    assert actual == expected


# Stack Tests
# -------------------------------------------------------------------

def test_stack_created():
    # Arrange
    expected = True
    stack = Stack()

    # Act
    actual = stack.is_empty()

    # Assert
    assert actual == expected


def test_stack_push_value(new_stack_1):
     # Arrange
    expected = "Test_Value_1"

    # Act
    actual = new_stack_1.top.value

    # Assert
    assert actual == expected


def test_stack_push_multiple(new_stack_5):
     # Arrange
    expected = "Test_Value_1"

    # Act
    actual = new_stack_5.top.value

    # Assert
    assert actual == expected


def test_stack_pop(new_stack_5):
     # Arrange
    expected_1 = "Test_Value_1"
    expected_2 = "Test_Value_2"

    # Act
    new_stack_5.pop()
    actual_1 = new_stack_5.top.value
    actual_2 = new_stack_5.top.next.value

    # Assert
    assert actual_1 == expected_1
    assert actual_2 == expected_2

def test_stack_pop(new_stack_5):
     # Arrange
    expected = True

    # Act
    new_stack_5.pop()
    new_stack_5.pop()
    new_stack_5.pop()
    new_stack_5.pop()
    new_stack_5.pop()
    actual = new_stack_5.is_empty()

    # Assert
    assert actual == expected


def test_stack_peek(new_stack_5):
     # Arrange
    expected = "Test_Value_1"

    # Act
    actual = new_stack_5.peek()

    # Assert
    assert actual == expected


def test_stack_peek_empty(new_stack_0):
    # Assert
     with pytest.raises(Exception):
        assert new_stack_0.peek()


def test_stack_pop_empty(new_stack_0):
    # Assert
     with pytest.raises(Exception):
        assert new_stack_0.pop()




# Queue Tests
# -------------------------------------------------------------------

def test_queue_created():
    # Arrange
    expected = True
    queue = Queue()

    # Act
    actual = queue.is_empty()

    # Assert
    assert actual == expected



def test_queue_enqueue_value(new_queue_1):
     # Arrange
    expected = "Test_Value_1"

    # Act
    actual = new_queue_1.front.value

    # Assert
    assert actual == expected


def test_queue_enqueue_multiple(new_queue_5):
     # Arrange
    expected_1 = "Test_Value_1"
    expected_2 = "Test_Value_2"

    # Act
    actual_1 = new_queue_5.front.value
    actual_2 = new_queue_5.front.next.value

    # Assert
    assert actual_1 == expected_1
    assert expected_2 == actual_2


def test_queue_dequeue_value(new_queue_5):
     # Arrange
    expected = "Test_Value_1"

    # Act
    actual = new_queue_5.dequeue()

    # Assert
    assert actual == expected

def test_queue_peek(new_queue_5):
     # Arrange
    expected = "Test_Value_1"

    # Act
    actual = new_queue_5.peek()

    # Assert
    assert actual == expected

def test_queue_dequeue_multiple(new_queue_5):
     # Arrange
    expected = True

    # Act
    new_queue_5.dequeue()
    new_queue_5.dequeue()
    new_queue_5.dequeue()
    new_queue_5.dequeue()
    new_queue_5.dequeue()

    actual = new_queue_5.is_empty()

    # Assert
    assert actual == expected


def test_queue_peek_empty(new_queue_0):
    # Assert
    with pytest.raises(Exception):
        assert new_queue_0.peek()


def test_queue_dequeue_empty(new_queue_0):
    # Assert
    with pytest.raises(Exception):
        assert new_queue_0.dequeue()






# Pseudo Queue Tests
# -------------------------------------------------------------------


def test_pseudo_queue_enqueue_value(new_pseudo_queue_1):
     # Arrange
    expected = "Test_Value_1"

    # Act
    actual = new_pseudo_queue_1.front.value

    # Assert
    assert actual == expected


def test_pseudo_queue_enqueue_multiple(new_pseudo_queue_5):
     # Arrange
    expected_1 = "Test_Value_1"
    expected_2 = "Test_Value_2"

    # Act
    actual_1 = new_pseudo_queue_5.front.value
    actual_2 = new_pseudo_queue_5.front.next.value

    # Assert
    assert actual_1 == expected_1
    assert expected_2 == actual_2


def test_pseudo_queue_dequeue_value(new_pseudo_queue_5):
     # Arrange
    expected = "Test_Value_1"

    # Act
    actual = new_pseudo_queue_5.dequeue()

    # Assert
    assert actual == expected


def test_pseudo_queue_dequeue_multiple(new_pseudo_queue_5):
     # Arrange
    expected = True

    # Act
    new_pseudo_queue_5.dequeue()
    new_pseudo_queue_5.dequeue()
    new_pseudo_queue_5.dequeue()
    new_pseudo_queue_5.dequeue()
    new_pseudo_queue_5.dequeue()

    # Assert
    with pytest.raises(Exception):
        assert new_pseudo_queue_5.dequeue()


def test_pseudo_queue_dequeue_empty(new_pseudo_queue_0):
    # Assert
    with pytest.raises(Exception):
        assert new_pseudo_queue_0.dequeue()




# Fixtures
# -------------------------------------------------------------------
@pytest.fixture
def new_stack_0():
    stack = Stack()
    return stack


@pytest.fixture
def new_stack_1():
    stack = Stack()
    stack.push("Test_Value_1")
    return stack

@pytest.fixture
def new_stack_5():
    stack = Stack()
    stack.push("Test_Value_5")
    stack.push("Test_Value_4")
    stack.push("Test_Value_3")
    stack.push("Test_Value_2")
    stack.push("Test_Value_1")
    return stack

@pytest.fixture
def new_queue_0():
    queue = Queue()
    return queue

@pytest.fixture
def new_queue_1():
    queue = Queue()
    queue.enqueue("Test_Value_1")
    return queue

@pytest.fixture
def new_queue_5():
    queue = Queue()
    queue.enqueue("Test_Value_1")
    queue.enqueue("Test_Value_2")
    queue.enqueue("Test_Value_3")
    queue.enqueue("Test_Value_4")
    queue.enqueue("Test_Value_5")
    return queue


@pytest.fixture
def new_pseudo_queue_0():
    pseudo = PseudoQueue()
    return pseudo

@pytest.fixture
def new_pseudo_queue_1():
    pseudo = PseudoQueue()
    pseudo.enqueue("Test_Value_1")
    return pseudo

@pytest.fixture
def new_pseudo_queue_5():
    pseudo = PseudoQueue()
    pseudo.enqueue("Test_Value_1")
    pseudo.enqueue("Test_Value_2")
    pseudo.enqueue("Test_Value_3")
    pseudo.enqueue("Test_Value_4")
    pseudo.enqueue("Test_Value_5")
    return pseudo
