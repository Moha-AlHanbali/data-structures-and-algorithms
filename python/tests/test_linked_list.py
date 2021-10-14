from linked_list.linked_list import LinkedList, Node
import pytest


def test_import():
    assert LinkedList
    assert Node


def test_empty_node():
    with pytest.raises(TypeError):
        node = Node()


def test_empty_link():
    #Arrange
    ll = LinkedList()
    expected = str(ll.__class__)

    #Act
    actual = "<class 'linked_list.linked_list.LinkedList'>"

    #Assert
    assert actual == expected


def test_link_insert():
    #Arrange
    ll = LinkedList()
    ll.insert("value")
    expected = "value"

    #Act
    actual = ll.head.value

    #Assert
    assert actual == expected


def test_link_insert_multiple():
    #Arrange
    ll = LinkedList()
    ll.insert("FIRST VALUE")
    ll.insert("SECOND VALUE")
    ll.insert("THIRD VALUE")
    expected_first = "THIRD VALUE"
    expected_second = "SECOND VALUE"
    expected_third = "FIRST VALUE"

    #Act
    actual_first = ll.head.value
    actual_second = ll.head.next.value
    actual_third = (ll.head.next).next.value

    #Assert
    assert actual_first == expected_first
    assert actual_second == expected_second
    assert actual_third == expected_third


def test_link_head_pointer():
    #Arrange
    ll = LinkedList()
    ll.insert("FIRST VALUE")
    ll.insert("SECOND VALUE")
    ll.insert("THIRD VALUE")
    expected = "THIRD VALUE"

    #Act
    actual = ll.head.value

    #Assert
    assert actual == expected

def test_link_includes_true():
    #Arrange
    ll = LinkedList()
    ll.insert("FIRST VALUE")
    ll.insert("SECOND VALUE")
    ll.insert("THIRD VALUE")
    expected = True

    #Act
    actual = ll.includes("FIRST VALUE")

    #Assert
    assert actual == expected

def test_link_includes_false():
    #Arrange
    ll = LinkedList()
    ll.insert("FIRST VALUE")
    ll.insert("SECOND VALUE")
    ll.insert("THIRD VALUE")
    expected = False

    #Act
    actual = ll.includes("MILLIONTH VALUE")

    #Assert
    assert actual == expected


def test_link_to_string():
    #Arrange
    ll = LinkedList()
    ll.insert(4)
    ll.insert("THIRD VALUE")
    ll.insert("SECOND VALUE")
    ll.insert("FIRST VALUE")
    expected = "{'FIRST VALUE'} -> {'SECOND VALUE'} -> {'THIRD VALUE'} -> {4} -> NULL"

    #Act
    actual = ll.to_string()

    #Assert
    assert actual == expected
