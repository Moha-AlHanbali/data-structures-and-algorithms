class Node():
    """
    Node class creates Node instances.

    Arguments:
    value: any
    next_: Node
    """
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_
