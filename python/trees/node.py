class Node():
    """
    Node class creates.

    Arguments:
    value: any
    left: Node
    right: Node
    """
    def __init__(self, value, next_ = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        self.next = next_
