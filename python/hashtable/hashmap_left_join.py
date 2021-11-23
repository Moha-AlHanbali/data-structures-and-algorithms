"""This module contains hashmap_left_join function"""

from hashtable.hashtable import HashTable

def hashmap_left_join(hashmap1: HashTable, hashmap2: HashTable):
    """
    hashmap_left_join returns all data from the first hashmap, even if there are no matches in the right table. If it has matches on the second hashmap, it'll return the values along with the corresponding data from the first hashmap, if not, they'll be replaced by None.

    Arguments:
        hashmap1: HashTable
        hashmap2: HashTable

    Return: List of lists containing the joined values.
    """
    try:
        output_list = []

        for bucket in range(len(hashmap1._HashTable__buckets)):

            if hashmap2._HashTable__buckets[bucket]:

                if hashmap1.contains(str(hashmap2._HashTable__buckets[bucket].head.value[0])):

                    output_list += [[hashmap1._HashTable__buckets[bucket].head.value[0], hashmap1._HashTable__buckets[bucket].head.value[1], hashmap2._HashTable__buckets[bucket].head.value[1]]]

            else:

                if hashmap1._HashTable__buckets[bucket]:

                    output_list += [[hashmap1._HashTable__buckets[bucket].head.value[0], hashmap1._HashTable__buckets[bucket].head.value[1], None]]

        return(output_list)

    except:

        raise Exception('Please check the hashmaps you entered and try again.')
