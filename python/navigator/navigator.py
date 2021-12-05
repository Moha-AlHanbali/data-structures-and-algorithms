"""This module contains Navigator class"""

from navigator.stack import Stack
from navigator.node import Node


class Naviagtor:
    """
    Navigator class keeps track of visited pages history

    Methods:

        back:
            back method takes no arguments and returns the previous location or NULL if there is none.

            Arguments: None

            Return: Node value or None

        forward:
            forward method takes no arguments and returns the next location or NULL if there is none.

            Arguments: None

            Return: Node value or None

        go:
            go method should take a string argument representing the desired location.

            Arguments: Str

            Return: Node value or None

    """

    def __init__(self):
        self.history = Stack()
        self.backtrack = Stack()

    def back(self):
        if self.history.is_empty():
            return None

        self.backtrack.push(self.history.pop())

        return self.history.peek().value

    def forward(self):
        if self.backtrack.is_empty():
            return None

        self.history.push(self.backtrack.pop())

        return self.history.peek().value

    def go(self, page:str):
        self.history.push(Node(page))

        while not self.backtrack.is_empty():
            self.backtrack = Stack()

        return self.history.peek().value
