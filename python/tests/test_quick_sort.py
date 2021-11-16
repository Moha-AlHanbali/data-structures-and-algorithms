"""This module tests Quick Sort Module"""

from quick_sort.quick_sort import quick_sort

def test_quick_sort_sorted():
    #Arrange
    expected = [1, 2, 3, 4, 5, 6]

    #Act
    actual = quick_sort([1, 2, 3, 4, 5, 6], 0, len([1, 2, 3, 4, 5, 6])-1)

    #Assert
    assert actual == expected

def test_quick_sort_reversed():
    #Arrange
    expected = [1, 2, 3, 4, 5, 6]

    #Act
    actual = quick_sort([6, 5 ,4 ,3, 2, 1], 0, len([1, 2, 3, 4, 5, 6])-1)

    #Assert
    assert actual == expected

def test_quick_sort():
    #Arrange
    expected = [1, 2, 3, 4, 5, 6]

    #Act
    actual = quick_sort([4, 5 ,6 ,3, 2, 1], 0, len([1, 2, 3, 4, 5, 6])-1)

    #Assert
    assert actual == expected

def test_quick_sort_empty():
    #Arrange
    expected = []

    #Act
    actual = quick_sort([], 0, len([])-1)

    #Assert
    assert actual == expected
