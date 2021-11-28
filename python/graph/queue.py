"""This module contains Queue class"""

from collections import deque

class Queue:
    """
        Queue class creates Queue instances.

        Arguments: None

        Methods:

            enqueue

                This method adds a Node to the back of a Queue.

                Arguments: value: any

                Return: None

            dequeue

                This method removes a Node to the front of a Queue.

                Arguments: None

                Return: None
    """
    def __init__(self):
        self.dq = deque()

    def __len__(self):
        return len(self.dq)

    def enqueue(self, value):
        self.dq.append(value)

    def dequeue(self):
        return self.dq.popleft()

