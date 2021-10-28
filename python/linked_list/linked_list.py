class Node:
    """
    Node class creates Node instances.

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

        while self.current:
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

        while self.current:
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

        while self.current:
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

        while self.current.next:
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

        while self.current:
            if self.current.value == value:
                self.current.next = Node(new_value, self.current.next)
                break
            self.current = self.current.next


    def kth_from_end(self, k:int):
        """
        Return the node’s value that is k places from the tail of the linked list.

        Arguments:
        k: int

        Return: Node Value
        """

        self.current = self.head
        length = -1
        counter = 0

        while self.current:
            length += 1
            self.current = self.current.next

        if k > length or k < 0:
            raise Exception("An error occurred. Try using a positive value that doesn't exceed the list length for the argument (k).")

        self.current = self.head
        while self.current:
            if k == (length - counter):
                return self.current.value
            self.current = self.current.next
            counter += 1


def linked_list_zip(list1:LinkedList, list2:LinkedList):
    """
    Returns the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.

    Arguments:
    list1: LinkedList
    list2: LinkedList

    Return: LinkedList
    """
    new_list = LinkedList()
    list1.current = list1.head
    list2.current = list2.head

    while list1.current or list2.current:
        if list1.current == list1.head:
            new_list.insert(list1.current.value)
            list1.current = list1.current.next
            new_list.append(list2.current.value)
            list2.current = list2.current.next

        if list1.current:
            new_list.append(list1.current.value)
            list1.current = list1.current.next

        if list2.current:
            new_list.append(list2.current.value)
            list2.current = list2.current.next

    return new_list


def reverse_list(list:LinkedList):
    temp = list.head
    current = temp.next
    list.head.next = None
    while current.next:
        current.next = list.head
        list.head = current
        list.head.next = None
        current = temp.next
        # temp = temp.next
    print (list)
    return (list)


def linked_list_palindrome(list:LinkedList):
    """
    Checks if the linked list is a palindrome(a word, phrase, number, or sequence of nodes which reads the same backward as forward).

    Arguments:
    list: LinkedList

    Return: Boolean
    """
    regular_list = []
    is_palindrome = False

    while list.current:
        regular_list += [list.current.value]
        list.current = list.current.next

    median = (len(regular_list)) // 2

    for i in range(median + 1):

        print(regular_list[i], regular_list[-1-i])

        if regular_list[i] == regular_list[-1 - i]:
            is_palindrome = True
        else:
            is_palindrome = False
            break

    print(regular_list)
    print(is_palindrome)
    return is_palindrome




if __name__ == '__main__':
    # ll = LinkedList()
    # ll.insert(1)
    # ll.insert(2)
    # ll.insert(3)
    # ll.insert(4)
    # ll.insert(5)
    # ll.insert(4)
    # ll.insert(3)
    # ll.insert(2)
    # ll.insert(1)
    # linked_list_palindrome(ll)

    # ll2 = LinkedList()
    # ll2.insert(1)
    # ll2.insert(2)
    # ll2.insert(3)
    # ll2.insert(4)
    # ll2.insert(5)
    # ll2.insert(4)
    # ll2.insert(3)
    # ll2.insert(5)
    # ll2.insert(1)
    # linked_list_palindrome(ll2)

    ll3 = LinkedList()
    ll3.insert(5)
    ll3.insert(4)
    ll3.insert(3)
    ll3.insert(2)
    ll3.insert(1)
    print(ll3)
    reverse_list(ll3)

