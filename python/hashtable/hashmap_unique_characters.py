"""This module contains hashmap_unique_characters function"""

from hashtable.hashtable import HashTable

def hashmap_unique_characters(string: str):
    """

    """
    hashmap = HashTable(len(string))
    char_list = list(string.replace(",", "").replace(".", "").replace(" ", "").replace("!", "").replace("?", "").replace(":", "").replace(";", "").lower())

    for character in char_list :
        if hashmap.contains(character):
            return False

        else:
            hashmap .add(character , character)

    return True
