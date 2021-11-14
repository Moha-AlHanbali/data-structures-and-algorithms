"""This module tests Insertion Sort Module"""

from insertion_sort.insertion_sort import insertion_sort

def test_insertion_sort_sorted():
    #Arrange
    expected = [1, 2, 3, 4, 5, 6]

    #Act
    actual = insertion_sort([1, 2, 3, 4, 5, 6])

    #Assert
    assert actual == expected

def test_insertion_sort_reversed():
    #Arrange
    expected = [1, 2, 3, 4, 5, 6]

    #Act
    actual = insertion_sort([6, 5 ,4 ,3, 2, 1])

    #Assert
    assert actual == expected

def test_insertion_sort():
    #Arrange
    expected = [1, 2, 3, 4, 5, 6]

    #Act
    actual = insertion_sort([4, 5 ,6 ,3, 2, 1])

    #Assert
    assert actual == expected

def test_insertion_sort_empty():
    #Arrange
    expected = []

    #Act
    actual = insertion_sort([])

    #Assert
    assert actual == expected
