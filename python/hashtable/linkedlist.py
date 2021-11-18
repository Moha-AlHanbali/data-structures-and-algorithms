"""This module contains Linked List data structure Class"""

from hashtable.node import Node


class LinkedList:
    """
    LinkedList class creates Linked Lists instances.

    Arguments:
    None
    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        """
        Adds a new node with that value to the head of the list.

        Arguments:
        value: any

        Return: None
        """
        self.head = Node(value, self.head)
