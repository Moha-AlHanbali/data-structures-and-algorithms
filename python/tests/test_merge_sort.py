"""This module tests Merge Sort Module"""

from merge_sort.merge_sort import merge_sort

def test_merge_sort_sorted():
    #Arrange
    expected = [1, 2, 3, 4, 5, 6]

    #Act
    actual = merge_sort([1, 2, 3, 4, 5, 6])

    #Assert
    assert actual == expected

def test_merge_sort_reversed():
    #Arrange
    expected = [1, 2, 3, 4, 5, 6]

    #Act
    actual = merge_sort([6, 5 ,4 ,3, 2, 1])

    #Assert
    assert actual == expected

def test_merge_sort():
    #Arrange
    expected = [1, 2, 3, 4, 5, 6]

    #Act
    actual = merge_sort([4, 5 ,6 ,3, 2, 1])

    #Assert
    assert actual == expected

def test_merge_sort_empty():
    #Arrange
    expected = []

    #Act
    actual = merge_sort([])

    #Assert
    assert actual == expected
