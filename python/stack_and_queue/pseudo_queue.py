from stack_and_queue.node  import Node
# from node  import Node

from stack_and_queue.stack  import Stack
# from stack  import Stack


class PseudoQueue():
     """
     Queue class creates a Pseudo Queue instances.

     Arguments:
     front: Node
     back: Node
     """
     def __init__(self, front = None, back = None):
        self.front = front
        self.back = back
        self.straight_stack = Stack()
        self.reverse_stack = Stack()


     def enqueue(self, value):
        """
        This method Inserts value into the PseudoQueue, using a first-in, first-out approach..

        Arguments:
        value: any
        """
        if not self.front:
            self.reverse_stack.push(value)
            self.front = Node(self.reverse_stack.peek())
            self.back = self.front
            self.reverse_stack.pop()

        else:
            self.reverse_stack.push(value)

            current = self.reverse_stack.top
            while current:
                self.straight_stack.push(self.reverse_stack.peek())
                self.reverse_stack.pop()
                current = self.reverse_stack.top

            current = self.straight_stack.top
            while current:
                self.back.next = Node(self.straight_stack.peek())
                self.straight_stack.pop()
                self.back = self.back.next
                current = self.straight_stack.top


     def dequeue(self):
        """
        This method Extracts a value from the PseudoQueue, using a first-in, first-out approach.

        Arguments: None

        Return: Value of Dequeued Node
        """
        dispose = ''
        if not self.front:
            raise Exception("Queue is empty.")

        else:
            current = self.front
            while current:
                self.reverse_stack.push(current.value)
                current = current.next

            current = self.reverse_stack.top
            while current:
                self.straight_stack.push(self.reverse_stack.peek())
                self.reverse_stack.pop()
                current = self.reverse_stack.top

            dispose = self.straight_stack.peek()
            self.straight_stack.pop()
            if self.straight_stack.top:
                self.front = Node(self.straight_stack.peek())
            self.back = self.front
            if self.straight_stack.top:
                self.straight_stack.pop()
                current = self.straight_stack.top
                while current:
                    self.back.next = Node(self.straight_stack.peek())
                    self.straight_stack.pop()
                    self.back = self.back.next
                    current = self.straight_stack.top
            else:
                self.front = None
                self.back = self.front

            return dispose
