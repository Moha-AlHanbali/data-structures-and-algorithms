"""This module contains Insertion Sort algorithm"""

def insertion_sort(arr):
    """
    insertion_sort function sorts an array of integers in ascending order.

    Arguments: Array of Integers

    Return: Modified Array
    """
    for i in range(1, len(arr)):
        j = i-1
        temp = arr[i]

        while j >=0 and temp <arr[j]:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = temp

    return arr
