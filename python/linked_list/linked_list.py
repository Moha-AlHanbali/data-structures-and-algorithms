class Node:
    """
    Node class creates Linked Lists instances.

    Arguments:
    value: any
    next_: Node
    """
    try:
        def __init__(self, value:any, next_ = None):
            self.value = value
            self.next = next_
    except TypeError as err:
        raise

class LinkedList:
    """
    LinkedList class creates Linked Lists instances.

    Arguments:
    None
    """

    def __init__(self):
        self.head = None
        self.current = self.head

    def insert(self, value):
        """
        Adds a new node with that value to the head of the list.

        Arguments:
        value: any

        Return: None
        """
        self.head = Node(value, self.head)
        self.current = self.head


    def includes(self, value):
        """
        Indicates whether that value exists as a Node’s value somewhere within the list.

        Arguments:
        value: any

        Return: Boolean
        """
        self.current = self.head

        while self.current != None:
            print("FLAG", self.current.value)
            if self.current.value == value:
                return True
            self.current = self.current.next
        return False


    def to_string(self):
        """
        Returns a formatted string representing all the values in the Linked List.

        Arguments:
        None

        Return: String Output
        """
        self.current = self.head

        output = ""

        while self.current != None:
            print("PRINT", self.current.value)
            output = output + (f"{ {self.current.value} } -> ")
            self.current = self.current.next
        output = output + "NULL"
        return(output)


# if __name__ == "__main__":
#     ll = LinkedList()
#     print(ll.insert("ABC"))
#     print(ll.head.value)
#     print(ll.insert("EFG"))
#     print(ll.head.value)
#     print(ll.insert("HIJ"))
#     print(ll.head.value)
#     print(ll.insert(123))
#     print(ll.head.value)
#     print(ll.includes("ABE"))
#     print(ll.to_string())
