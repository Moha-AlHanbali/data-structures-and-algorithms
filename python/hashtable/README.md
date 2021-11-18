# Hash Table

- This Module provides means to create Hash Table Data Structure and modify them to some extent.

<br>

## Challenge

- To implement new data-structure and manipulate it.

<br>


## Whiteboard Process

-

## Approach & Efficiency

- O complexity (Time and Space) for (HashTable.__hash) method is O(1).

- O complexity (Time and Space) for (HashTable.add) method is O(1).

- O complexity (Time) for (HashTable.contains) method is O(n).
- O complexity (Space) for (HashTable.contains) method is O(1).

- O complexity (Time) for (HashTable.get) method is O(n).
- O complexity (Space) for (HashTable.get) method is O(1).


<br>

## API

- HashTree()

        HashTable is a data structue that stores key/value data pairs.

        Arguments:

        size: int, number of buckets in the hash table

- HashTable.__hash()

            A method to convert a string into an index number.

            Arguments:

            key: str

            Return: int, an index number


- HashTable.add()

            add:

            A method to add data pairs to Hash Table.

            Arguments:

            key: str
            value: str

            Return: None

- HashTable.get()

            A method to retrieve data from Hash Table.

            Arguments:

            key: str

            Return: str, the value of the given key.

- HashTable.contains()

            A method to check if the key exists in the hash table.

            Arguments:

            key: str

            Return: Boolean.

<br>

## Testing Goals

- HashTree

- [x] Adding a key/value to your hashtable results in the value being in the data structure
- [x] Retrieving based on a key returns the value stored
- [x] Successfully returns null for a key that does not exist in the hashtable
- [X] Successfully handle a collision within the hashtable
- [X] Successfully retrieve a value from a bucket within the hashtable that has a collision
- [x] Successfully hash a key to an in-range value

---------------------------------------------------------------------------
