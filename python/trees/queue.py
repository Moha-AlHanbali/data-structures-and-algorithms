# from trees.node  import Node
from node import Node



class Queue():
     """
     Queue class creates Queue instances.

     Arguments:
     front: Node
     back: Node
     """
     def __init__(self, front = None, back = None):
        self.front = front
        self.back = back

     def enqueue(self, value):
        """
        This method adds a Node to the back of a Queue.

        Arguments:
        value: any
        """
        if self.is_empty():
            self.front = Node(value)
            self.back = self.front
        else:
            self.back.next = Node(value)
            self.back = self.back.next


     def dequeue(self):
        """
        This method removes a Node to the front of a Queue.

        Arguments: None

        Return: Value of Dequeued Node
        """
        if self.is_empty():
            raise Exception("Queue is empty.")
        else:
            dispose = self.front
            self.front = self.front.next
            dispose.next = None
            if dispose == self.back:
                self.back == None
            return dispose.value


     def peek(self):
        """
        This method returns the value of front Node of a Queue.

        Arguments: None

        Return : Front Node Value
        """
        if self.is_empty():
            raise Exception("Queue is empty.")
        else:
            return self.front.value


     def is_empty(self):
        """
        This method checks if a Queue has any Nodes within.

        Arguments: None

        Return : Boolean
        """
        if not self.front:
            return True
        else:
            return False
