from stack_and_queue.node import Node
from stack_and_queue.stack import Stack
from stack_and_queue.queue import Queue
from stack_and_queue.pseudo_queue import PseudoQueue
from stack_and_queue.animal_shelter import AnimalShelter, Animal, Cat, Dog, Mouse, Horse
from stack_and_queue.stack_queue_brackets import validate_brackets
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






# Animal Shelter Tests
# -------------------------------------------------------------------


def test_shelter_enqueue_value(animal_queue):
     # Arrange
    expected = "bog"

    # Act
    actual = animal_queue.front.value.name

    # Assert
    assert actual == expected

def test_shelter_enqueue_wrong_value(mouse, animal_queue):
     # Arrange
    expected = False

    # Act
    actual = animal_queue.enqueue(mouse)

    # Assert
    assert actual == expected


def test_shelter_enqueue_multiple(animal_queue):
     # Arrange
    expected_1 = "bog"
    expected_2 = "sog"

    # Act
    actual_1 = animal_queue.front.value.name
    actual_2 = animal_queue.front.next.value.name

    # Assert
    assert actual_1 == expected_1
    assert expected_2 == actual_2

def test_shelter_dequeue_invalid(horse, animal_queue):
     # Arrange
    expected = None

    # Act
    actual = animal_queue.dequeue(horse)

    # Assert
    assert actual == expected


def test_shelter_dequeue_first_value(animal_queue):
     # Arrange
    expected = "bog"

    # Act
    actual = animal_queue.dequeue("dog")

    # Assert
    assert actual == expected

def test_shelter_dequeue_two_values(animal_queue):
     # Arrange
    expected_1 = "bog"
    expected_2 = "sog"

    # Act
    actual_1 = animal_queue.dequeue("dog")
    actual_2 = animal_queue.dequeue("dog")

    # Assert
    assert actual_1 == expected_1
    assert actual_2 == expected_2

def test_shelter_dequeue_different_value(animal_queue):
     # Arrange
    expected_1 = "mat"
    expected_2 = "bog"

    # Act
    actual_1 = animal_queue.dequeue("cat")
    actual_2 = animal_queue.front.value.name

    # Assert
    assert actual_1 == expected_1
    assert actual_2 == expected_2


def test_shelter_dequeue_alternating_values(animal_queue):
     # Arrange
    expected_1 = "mat"
    expected_2 = "bog"
    expected_3 = "pat"
    expected_4 = "sog"
    expected_5 = "log"

    # Act
    actual_1 = animal_queue.dequeue("cat")
    actual_2 = animal_queue.dequeue("dog")
    actual_3 = animal_queue.dequeue("cat")
    actual_4 = animal_queue.dequeue("dog")
    actual_5 = animal_queue.front.value.name


    # Assert
    assert actual_1 == expected_1
    assert actual_2 == expected_2
    assert actual_3 == expected_3
    assert actual_4 == expected_4
    assert actual_5 == expected_5


def test_shelter_dequeue_empties_shelter(animal_queue):
    # Act
    animal_queue.dequeue("dog")
    animal_queue.dequeue("dog")
    animal_queue.dequeue("dog")
    animal_queue.dequeue("dog")
    animal_queue.dequeue("cat")
    animal_queue.dequeue("cat")
    animal_queue.dequeue("cat")
    animal_queue.dequeue("cat")

    # Assert
    with pytest.raises(Exception):
        assert new_pseudo_queue_5.dequeue()







# Validate Brackets Tests
# -------------------------------------------------------------------

def test_validate_brackets_case_1():
    #Arrange
    expected = True

    #Act
    actual = validate_brackets("{}")

    #Assert
    assert actual == expected


def test_validate_brackets_case_2():
    #Arrange
    expected = True

    #Act
    actual = validate_brackets("{}(){}")

    #Assert
    assert actual == expected


def test_validate_brackets_case_3():
    #Arrange
    expected = True

    #Act
    actual = validate_brackets("()[[Extra Characters]]")

    #Assert
    assert actual == expected


def test_validate_brackets_case_4():
    #Arrange
    expected = True

    #Act
    actual = validate_brackets("(){}[[]]")

    #Assert
    assert actual == expected



def test_validate_brackets_case_5():
    #Arrange
    expected = True

    #Act
    actual = validate_brackets("{}{Code}[Fellows](())")

    #Assert
    assert actual == expected


def test_validate_brackets_case_6():
    #Arrange
    expected = True

    #Act
    actual = validate_brackets("WILL([])()({)(})BE(())TRUE")

    #Assert
    assert actual == expected



def test_validate_brackets_case_7():
    #Arrange
    expected = False

    #Act
    actual = validate_brackets("[({}]")

    #Assert
    assert actual == expected


def test_validate_brackets_case_8():
    #Arrange
    expected = False

    #Act
    actual = validate_brackets("(](")

    #Assert
    assert actual == expected


def test_validate_brackets_case_9():
    #Arrange
    expected = False

    #Act
    actual = validate_brackets("{(})")

    #Assert
    assert actual == expected

def test_validate_brackets_case_10():
    #Arrange
    expected = True

    #Act
    actual = validate_brackets("(([{[()]}]))")

    #Assert
    assert actual == expected

def test_validate_brackets_case_11():
    #Arrange
    expected = True

    #Act
    actual = validate_brackets("(([{[)(]}]))")

    #Assert
    assert actual == expected

def test_validate_brackets_case_12():
    #Arrange
    expected = False

    #Act
    actual = validate_brackets("(([{)[(]}]))")

    #Assert
    assert actual == expected

def test_validate_brackets_case_13():
    #Arrange
    expected = False

    #Act
    actual = validate_brackets("(([{)[(]}]})")

    #Assert
    assert actual == expected

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


@pytest.fixture
def dog():
    dog = Dog("dog")
    return dog

@pytest.fixture
def cat():
    cat = Cat("cat")
    return cat

@pytest.fixture
def mouse():
    mouse = Mouse("mouse")
    return mouse

@pytest.fixture
def horse():
    horse = Horse("horse")
    return horse

@pytest.fixture
def animal_queue():
    shelter = AnimalShelter()

    bog = Dog("bog")
    sog = Dog("sog")
    log = Dog("log")
    hog = Dog("hog")

    mat = Cat("mat")
    pat = Cat("pat")
    fat = Cat("fat")
    nat = Cat("nat")

    shelter.enqueue(bog)
    shelter.enqueue(sog)
    shelter.enqueue(log)
    shelter.enqueue(hog)

    shelter.enqueue(mat)
    shelter.enqueue(pat)
    shelter.enqueue(fat)
    shelter.enqueue(nat)

    return shelter
