"""This module contains hashmap_repeated_word funciton"""

from hashtable.hashtable import HashTable


def hashmap_repeated_word(str):
    """
    hashmap_repeated_word is a function that maps a string into a hash table and returns the first repeated word within it.

        Arguments:
            str: str

        Returns: str, the first repeated word
    """
    try:
        bare_str = str.replace(",", "").replace(".", "").replace("'", "").replace("!", "").replace("?", "").replace(":", "").replace(";", "").replace("'", "").replace('"', "").lower()
        str_list = bare_str.split(" ")

        hashtable = HashTable(len(str_list))

        for word in str_list:

            if not hashtable.contains(word):
                hashtable.add(word, word)
            else:
                return word

        return ''
    except:
        raise ValueError("Please check the string input and try again.")
