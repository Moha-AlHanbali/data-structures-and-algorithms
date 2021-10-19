from linked_list.linked_list import LinkedList, Node, linked_list_zip
import unittest
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


def test_link_kth_from_end():
    #Arrange
    ll = LinkedList()
    ll.insert("THIRD VALUE")
    ll.insert("SECOND VALUE")
    ll.insert("FIRST VALUE")

    expected = "SECOND VALUE"

    #Act
    actual = ll.kth_from_end(1)

    #Assert
    assert actual == expected


def test_link_kth_from_end_greater_than_length():
    #Arrange
    ll = LinkedList()
    ll.insert("THIRD VALUE")
    ll.insert("SECOND VALUE")
    ll.insert("FIRST VALUE")

    #Assert
    with pytest.raises(Exception):
        assert ll.kth_from_end(10)



def test_link_kth_from_end_same_length_exact():
    #Arrange
    ll = LinkedList()
    ll.insert("THIRD VALUE")
    ll.insert("SECOND VALUE")
    ll.insert("FIRST VALUE")

    #Assert
    with pytest.raises(Exception):
        assert ll.kth_from_end(3)



def test_link_kth_from_end_same_length_relative():
    #Arrange
    ll = LinkedList()
    ll.insert("THIRD VALUE")
    ll.insert("SECOND VALUE")
    ll.insert("FIRST VALUE")

    expected = "FIRST VALUE"

    #Act
    actual = ll.kth_from_end(2)

    #Assert
    assert actual == expected


def test_link_kth_from_end_same_length_of_1():
    #Arrange
    ll = LinkedList()
    ll.insert("FIRST VALUE")

    expected = "FIRST VALUE"

    #Act
    actual = ll.kth_from_end(0)

    #Assert
    assert actual == expected


def test_link_kth_from_end_negative():
    #Arrange
    ll = LinkedList()
    ll.insert("FIRST VALUE")
    ll.insert("SECOND VALUE")
    ll.insert("FIRST VALUE")

    #Assert
    with pytest.raises(Exception):
        assert ll.kth_from_end(-1)


def test_linked_list_zip():
    #Arrange
    list1 = LinkedList()
    list1.insert("123")
    list1.append("456")
    list1.append("789")
    list2 = LinkedList()
    list2.insert("ABC")
    list2.append("DEF")
    list2.append("GHI")

    expected = "{'123'} -> {'ABC'} -> {'456'} -> {'DEF'} -> {'789'} -> {'GHI'} -> NULL"

    #Act
    actual = str(linked_list_zip(list1, list2))

    #Assert
    assert actual == expected


def test_linked_list_zip_list1_longer():
    #Arrange
    list1 = LinkedList()
    list1.insert("123")
    list1.append("456")
    list1.append("789")
    list1.append("101112")
    list1.append("131415")
    list2 = LinkedList()
    list2.insert("ABC")
    list2.append("DEF")
    list2.append("GHI")

    expected = "{'123'} -> {'ABC'} -> {'456'} -> {'DEF'} -> {'789'} -> {'GHI'} -> {'101112'} -> {'131415'} -> NULL"

    #Act
    actual = str(linked_list_zip(list1, list2))

    #Assert
    assert actual == expected


def test_linked_list_zip_list2_longer():
    #Arrange
    list1 = LinkedList()
    list1.insert("123")
    list1.append("456")
    list1.append("789")

    list2 = LinkedList()
    list2.insert("ABC")
    list2.append("DEF")
    list2.append("GHI")
    list2.append("JKL")
    list2.append("MNO")

    expected = "{'123'} -> {'ABC'} -> {'456'} -> {'DEF'} -> {'789'} -> {'GHI'} -> {'JKL'} -> {'MNO'} -> NULL"

    #Act
    actual = str(linked_list_zip(list1, list2))

    #Assert
    assert actual == expected


def test_linked_list_zip_list1_1():
    #Arrange
    list1 = LinkedList()
    list1.insert("123")

    list2 = LinkedList()
    list2.insert("ABC")
    list2.append("DEF")
    list2.append("GHI")

    expected = "{'123'} -> {'ABC'} -> {'DEF'} -> {'GHI'} -> NULL"

    #Act
    actual = str(linked_list_zip(list1, list2))

    #Assert
    assert actual == expected


def test_linked_list_zip_list2_1():
    #Arrange
    list1 = LinkedList()
    list1.insert("123")
    list1.append("456")
    list1.append("789")

    list2 = LinkedList()
    list2.insert("ABC")

    expected = "{'123'} -> {'ABC'} -> {'456'} -> {'789'} -> NULL"

    #Act
    actual = str(linked_list_zip(list1, list2))

    #Assert
    assert actual == expected


def test_linked_list_zip_reverse_order():
    #Arrange
    list1 = LinkedList()
    list1.insert("123")
    list1.append("456")
    list1.append("789")
    list2 = LinkedList()
    list2.insert("ABC")
    list2.append("DEF")
    list2.append("GHI")

    expected = "{'ABC'} -> {'123'} -> {'DEF'} -> {'456'} -> {'GHI'} -> {'789'} -> NULL"

    #Act
    actual = str(linked_list_zip(list2, list1))

    #Assert
    assert actual == expected
