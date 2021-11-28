"""This module contains Stack class"""

from collections import deque

class Stack:
    """
        Stack class creates Stack instances.

        Arguments: None

        Methods:

            push

                This method adds a Node to the top of stack.

                Arguments: value: any

                Return: None

            pop

                This method removes a Node to the top of stack.

                Arguments: None

                Return: None

            peek

                This method returns the Node on top of stack.

                Arguments: None

                Return: Node
    """
    def __init__(self):
        self.dq = deque()

    def __len__(self):
        return len(self.dq)

    def push(self, value):
        self.dq.append(value)

    def pop(self):
        return self.dq.pop()

    def peek(self):
        return self.dq[-1]
