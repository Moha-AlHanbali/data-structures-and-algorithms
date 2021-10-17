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
    actual = str(ll)

    #Assert
    assert actual == expected

def test_link_append():
    #Arrange
    ll = LinkedList()
    ll.insert("THIRD VALUE")
    ll.insert("SECOND VALUE")
    ll.insert("FIRST VALUE")
    ll.append("FOURTH VALUE")
    expected = "{'FIRST VALUE'} -> {'SECOND VALUE'} -> {'THIRD VALUE'} -> {'FOURTH VALUE'} -> NULL"

    #Act
    actual = str(ll)

    #Assert
    assert actual == expected


def test_link_append_multiple():
    #Arrange
    ll = LinkedList()
    ll.insert("THIRD VALUE")
    ll.insert("SECOND VALUE")
    ll.insert("FIRST VALUE")
    ll.append("FOURTH VALUE")
    ll.append("FIFTH VALUE")
    ll.append("SIXTH VALUE")
    expected = "{'FIRST VALUE'} -> {'SECOND VALUE'} -> {'THIRD VALUE'} -> {'FOURTH VALUE'} -> {'FIFTH VALUE'} -> {'SIXTH VALUE'} -> NULL"
    #Act
    actual = str(ll)

    #Assert
    assert actual == expected


def test_link_insert_before_middle():
    #Arrange
    ll = LinkedList()
    ll.insert("THIRD VALUE")
    ll.insert("SECOND VALUE")
    ll.insert("FIRST VALUE")
    ll.insert_before("SECOND VALUE", "NEW VALUE")
    expected = "{'FIRST VALUE'} -> {'NEW VALUE'} -> {'SECOND VALUE'} -> {'THIRD VALUE'} -> NULL"

    #Act
    actual = str(ll)

    #Assert
    assert actual == expected


def test_link_insert_before_first():
    #Arrange
    ll = LinkedList()
    ll.insert("THIRD VALUE")
    ll.insert("SECOND VALUE")
    ll.insert("FIRST VALUE")
    ll.insert_before("FIRST VALUE", "NEW VALUE")
    expected = "{'NEW VALUE'} -> {'FIRST VALUE'} -> {'SECOND VALUE'} -> {'THIRD VALUE'} -> NULL"

    #Act
    actual = str(ll)

    #Assert
    assert actual == expected


def test_link_insert_after_middle():
    #Arrange
    ll = LinkedList()
    ll.insert("THIRD VALUE")
    ll.insert("SECOND VALUE")
    ll.insert("FIRST VALUE")
    ll.insert_after("SECOND VALUE", "NEW VALUE")
    expected = "{'FIRST VALUE'} -> {'SECOND VALUE'} -> {'NEW VALUE'} -> {'THIRD VALUE'} -> NULL"

    #Act
    actual = str(ll)

    #Assert
    assert actual == expected


def test_link_insert_after_last():
    #Arrange
    ll = LinkedList()
    ll.insert("THIRD VALUE")
    ll.insert("SECOND VALUE")
    ll.insert("FIRST VALUE")
    ll.insert_after("THIRD VALUE", "NEW VALUE")
    expected = "{'FIRST VALUE'} -> {'SECOND VALUE'} -> {'THIRD VALUE'} -> {'NEW VALUE'} -> NULL"

    #Act
    actual = str(ll)

    #Assert
    assert actual == expected
