"""This module contains Hash Tables"""

from hashtable.linkedlist import LinkedList


class HashTable():
    """
    HashTable is a data structue that stores key/value data pairs.

        Arguments:

        size: int, number of buckets in the hash table

    Methods:

        __hash:

            A method to convert a string into an index number.

            Arguments:

            key: str

            Return: int, an index number

    ------------------------------------------------------------

            add:

            A method to add data pairs to Hash Table.

            Arguments:

            key: str
            value: str

            Return: None

    ------------------------------------------------------------

            get:

            A method to retrieve data from Hash Table.

            Arguments:

            key: str

            Return: str, the value of the given key.

    ------------------------------------------------------------

            contains:

            A method to check if the key exists in the hash table.

            Arguments:

            key: str

            Return: Boolean.

    """

    def __init__(self, size = 1024):
        self.__size = size
        self.__buckets = [None] * self.__size


    def __hash(self, key):
        return (sum([ord(char) for char in key]) * 599 % self.__size)


    def contains(self, key):
        if self.__buckets[self.__hash(key)]:
            current = self.__buckets[self.__hash(key)].head
            while current:
                if current.value[0] == key:
                    return True

                current = current.next

        return False


    def add(self, key, value):
        index = self.__hash(key)

        if not self.__buckets[index]:
            self.__buckets[index] = LinkedList()

        self.__buckets[index].insert([key, value])


    def get(self, key):
        index = self.__hash(key)

        if self.__buckets[index]:
            current = self.__buckets[index].head
            while current:
                if current.value[0] == key:

                    return current.value[1]

                current = current.next

        return None
