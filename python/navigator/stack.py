from navigator.node import Node

class Stack():
    """
    Stack class creates Stack instances.

    Arguments:
    top: Node
    """

    def __init__(self, top = None):
        self.top = top

    def push(self, value):
        """
        This method adds a Node to the top of a Stack.

        Arguments:
        value: any
        """
        if self.is_empty():
            self.top = Node(value)
        else:
            node = Node(value, self.top)
            self.top = node


    def pop(self):
        """
        This method removes the top Node of a Stack.

        Arguments: None

        Return: Popped Node Value
        """
        if self.is_empty():
            raise Exception("Stack is empty.")
        else:
            dispose = self.top
            self.top = self.top.next
            dispose.next = None
            return dispose.value


    def peek(self):
        """
        This method returns the value of top Node of a Stack.

        Arguments: None

        Return : Top Node Value
        """
        if self.is_empty():
            raise Exception("Stack is empty.")
        else:
            return self.top.value


    def is_empty(self):
        """
        This method checks if a Stack has any Nodes within.

        Arguments: None

        Return : Boolean
        """
        if not self.top:
            return True
        else:
            return False
