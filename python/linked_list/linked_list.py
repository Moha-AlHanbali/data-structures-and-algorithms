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


    def __str__(self):
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


    def append(self, value):
        """
        Adds a new node with the given value to the end of the list

        Arguments:
        value: any

        Return: None
        """
        self.current = self.head

        while self.current != None:
            if self.current.next == None:
                self.current.next = Node(value)
                break
            self.current = self.current.next


    def insert_before(self,value, new_value):
        """
        Adds a new node with the given new value immediately before the first node that has the value specified.

        Arguments:
        value: any
        new_value: any

        Return: None
        """

        self.current = self.head

        while self.current.next != None:
            if self.current.value == value:
                self.insert(new_value)
                break

            if self.current.next.value == value:
                self.current.next = Node(new_value, self.current.next)
                break
            self.current = self.current.next


    def insert_after(self,value, new_value):
        """
        Adds a new node with the given new value immediately after the first node that has the value specified.

        Arguments:
        value: any
        new_value: any

        Return: None
        """

        self.current = self.head

        while self.current != None:
            if self.current.value == value:
                self.current.next = Node(new_value, self.current.next)
                break
            self.current = self.current.next


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
#     print(str(ll))
#     print(ll.append("last_item"))
#     print(str(ll))
#     print(ll.insert_before("EFG", "insert_before"))
#     print(str(ll))
#     print(ll.insert_after("EFG", "insert_after"))
#     print(str(ll))
