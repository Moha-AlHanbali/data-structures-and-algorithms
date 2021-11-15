"""This module contains Merge Sort algorithm"""

def merge(left, right, arr):
    """
    merge function merges three lists into one in ascending order, based on their values.

    Arguments:
        left: list of integers
        right: list of integers
        arr: list of integers

    Return:
        None
    """
    i = 0
    j = 0
    k = 0

    while i <len(left) and j< len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1



def merge_sort(arr):
    """
    merge_sort function sorts list items in an ascending order, based on their values.

    Arguments:
        arr: list of integers

    Return:
        Modified list
    """
    n = len(arr)

    if n >1:
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)

        merge_sort(right)

        merge(left, right, arr)

    return arr
