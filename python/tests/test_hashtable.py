"""This module tests Hash Table Module"""

from hashtable.hashtable import HashTable
from hashtable.hashmap_repeated_word import hashmap_repeated_word
import pytest

# Test HashTable
# --------------------------------------------------------------------------------
def test_hash_table(hashtable):
    # Arrange
    excepted = 1024

    #Act
    actual = hashtable._HashTable__size

    #Assert
    assert actual == excepted



def test_hash_table_hash(hashtable):
    # Arrange
    excepted = 759

    #Act
    actual = hashtable._HashTable__hash('a')

    #Assert
    assert actual == excepted


def test_hash_table_hash(hashtable):
    # Arrange
    excepted = 759

    #Act
    actual = hashtable._HashTable__hash('a')

    #Assert
    assert actual == excepted


def test_hash_table_hash_range(hashtable):
    # Arrange
    excepted = 993

    #Act
    actual = hashtable._HashTable__hash('zzzzzzZZDdasdsaSAAzzz')

    #Assert
    assert actual == excepted


def test_hash_table_add_T(hashtable):
    # Arrange
    excepted = True

    #Act
    hashtable.add('a', 1)
    actual = hashtable.contains('a')

    #Assert
    assert actual == excepted


def test_hash_table_add_F(hashtable):
    # Arrange
    excepted = False

    #Act
    hashtable.add('a', 1)
    actual = hashtable.contains('b')

    #Assert
    assert actual == excepted


def test_hash_table_get(hashtable):
    # Arrange
    excepted = 2
    hashtable.add('b', 2)

    #Act
    actual = hashtable.get('b')

    #Assert
    assert actual == excepted


def test_hash_table_get_None(hashtable):
    # Arrange
    excepted = None
    hashtable.add('b', 2)

    #Act
    actual = hashtable.get('c')

    #Assert
    assert actual == excepted

def test_hash_table_hash_collision(hashtable):
    # Arrange
    excepted_1 = 491
    excepted_2 = 491

    #Act
    actual_1 = hashtable._HashTable__hash('FG')
    actual_2 = hashtable._HashTable__hash('EH')


    #Assert
    assert actual_1 == excepted_1
    assert actual_2 == excepted_2

def test_hash_table_add_collision(hashtable):
    # Arrange
    excepted_1 = True
    excepted_2 = True
    hashtable.add('FG', 1)
    hashtable.add('EH', 2)

    #Act
    actual_1 = hashtable.contains('FG')
    actual_2 = hashtable.contains('EH')


    #Assert
    assert actual_1 == excepted_1
    assert actual_2 == excepted_2


def test_hash_table_get_collision(hashtable):
    # Arrange
    excepted_1 = 1
    excepted_2 = 2

    hashtable.add('FG', 1)
    hashtable.add('EH', 2)

    #Act
    actual_1 = hashtable.get('FG')
    actual_2 = hashtable.get('EH')


    #Assert
    assert actual_1 == excepted_1
    assert actual_2 == excepted_2


# Test hashmap_repeated_word
# --------------------------------------------------------------------------------
def test_hashmap_repeated_word_case_1():
    # Arrange
    str = "Once upon a time, there was a brave princess who..."
    expected = 'a'

    #Act
    actual = hashmap_repeated_word(str)

    #Assert
    assert actual == expected


def test_hashmap_repeated_word_case_2():
    # Arrange
    str = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    expected = 'it'

    #Act
    actual = hashmap_repeated_word(str)

    #Assert
    assert actual == expected


def test_hashmap_repeated_word_case_3():
    # Arrange
    str = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    expected = 'summer'

    #Act
    actual = hashmap_repeated_word(str)

    #Assert
    assert actual == expected



def test_hashmap_repeated_word_case_4():
    # Arrange
    str = "aaaa, aa,aa aaa,a aaa, aabbb, accaaaaa aaaa, aaaa, aaaa"
    expected = 'aaaa'

    #Act
    actual = hashmap_repeated_word(str)

    #Assert
    assert actual == expected


def test_hashmap_repeated_word_case_5():
    # Arrange
    str = "aaaa"
    expected = ''

    #Act
    actual = hashmap_repeated_word(str)

    #Assert
    assert actual == expected


def test_hashmap_repeated_word_exception():
    #Assert
    with pytest.raises(Exception):
        hashmap_repeated_word(str)


@pytest.fixture
def hashtable():
    return HashTable()
