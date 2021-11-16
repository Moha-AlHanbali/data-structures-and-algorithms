"""This module contains Quick Sort algorithm"""

def quick_sort(arr, left, right):
    """
    Sorts a list of integers in ascending order.

    :param arr: arg1
    :type arr: list

    :param left: arg2
    :type left: int

    :param right: arg3
    :type right: int

    :return: sorted list
    """
    if left < right:
        position = partition(arr, left, right)
        quick_sort(arr, left, position-1)
        quick_sort(arr, position+1, right)
    return arr


def partition(arr, left, right):
    """
    Sets a pivot index and triggers swaps based on their value.

    :param arr: arg1
    :type arr: list

    :param left: arg2
    :type left: int

    :param right: arg3
    :type right: int

    :return: pivot index
    """
    pivot = arr[right]
    low = left -1

    for i in range(left, right):
        if arr[i] <= pivot:
            low += 1
            swap(arr, i, low)

    swap(arr, right, low+1)
    return low +1


def swap(arr, i, low):
    """
    Swaps the location of two indexes.

    :param arr: arg1
    :type arr: list

    :param i: arg2
    :type i: int

    :param low: arg3
    :type low: int

    :return: none
    """
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp
