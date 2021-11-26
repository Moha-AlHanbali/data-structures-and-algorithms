"""This module tests Hash Table Module"""

import pytest

from hashtable.hashtable import HashTable
from hashtable.hashmap_repeated_word import hashmap_repeated_word
from hashtable.hashmap_left_join import hashmap_left_join


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

def test_hash_table_get_keys(synonym_hashmap):
    # Arrange
    excepted = ['correct', 'happy', 'thin', 'positive', 'tidy', 'fitting', 'denied']

    #Act
    actual = synonym_hashmap.keys()

    #Assert
    assert actual == excepted


def test_hash_table_get_keys_empty():
    # Arrange
    hashmap = HashTable()
    excepted = []

    #Act
    actual = hashmap.keys()

    #Assert
    assert actual == excepted


def test_hash_table_get_values(synonym_hashmap):
    # Arrange
    excepted = ['right', 'pleased', 'slim',  'good', 'clean', 'adequate', 'prohibited']

    #Act
    actual = synonym_hashmap.values()


    #Assert
    assert actual == excepted

def test_hash_table_get_values_empty():
    # Arrange
    hashmap = HashTable()
    excepted = []

    #Act
    actual = hashmap.values()


    #Assert
    assert actual == excepted


def test_hash_table_get_pairs(synonym_hashmap):
    # Arrange
    excepted = [['correct', 'right'], ['happy','pleased'], ['thin','slim'],  ['positive','good'], ['tidy','clean'], ['fitting','adequate'], ['denied','prohibited']]

    #Act
    actual = synonym_hashmap.pairs()


    #Assert
    assert actual == excepted

def test_hash_table_get_pairs_empty():
    # Arrange
    hashmap = HashTable()
    excepted = []

    #Act
    actual = hashmap.pairs()


    #Assert
    assert actual == excepted

# Test hashmap_repeated_word
# --------------------------------------------------------------------------------
def test_hashmap_repeated_word_case_1():
    # Arrange
    string = "Once upon a time, there was a brave princess who..."
    expected = 'a'

    #Act
    actual = hashmap_repeated_word(string)

    #Assert
    assert actual == expected


def test_hashmap_repeated_word_case_2():
    # Arrange
    string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    expected = 'it'

    #Act
    actual = hashmap_repeated_word(string)

    #Assert
    assert actual == expected


def test_hashmap_repeated_word_case_3():
    # Arrange
    string = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    expected = 'summer'

    #Act
    actual = hashmap_repeated_word(string)

    #Assert
    assert actual == expected



def test_hashmap_repeated_word_case_4():
    # Arrange
    string = "aaaa, aa,aa aaa,a aaa, aabbb, accaaaaa aaaa, aaaa, aaaa"
    expected = 'aaaa'

    #Act
    actual = hashmap_repeated_word(string)

    #Assert
    assert actual == expected


def test_hashmap_repeated_word_case_5():
    # Arrange
    string = "aaaa"
    expected = ''

    #Act
    actual = hashmap_repeated_word(string)

    #Assert
    assert actual == expected


def test_hashmap_repeated_word_exception():
    #Assert
    with pytest.raises(Exception):
        hashmap_repeated_word(a)




# Test hashmap_left_join
# --------------------------------------------------------------------------------
def test_hashmap_left_join(synonym_hashmap, antonym_hashmap):
    # Arrange
    expected = [['correct', 'right', None], ['happy', 'pleased', 'sad'], ['thin', 'slim', 'fat'], ['positive', 'good', 'negative'], ['tidy', 'clean', None], ['fitting', 'adequate', None], ['denied', 'prohibited', 'allowed']]

    #Act
    actual = hashmap_left_join(synonym_hashmap, antonym_hashmap)

    #Assert
    assert actual == expected

def test_hashmap_left_join_reverse(synonym_hashmap, antonym_hashmap):
    # Arrange
    expected = [['happy', 'sad', 'pleased'], ['thin', 'fat', 'slim'], ['positive', 'negative', 'good'], ['denied', 'allowed', 'prohibited']]

    #Act
    actual = hashmap_left_join(antonym_hashmap, synonym_hashmap)

    #Assert
    assert actual == expected


def test_hashmap_left_join_case_2(synonym_hashmap_2, antonym_hashmap_2):
    # Arrange
    expected = [['diligent', 'employed', 'idle'], ['outfit', 'garb', None], ['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['wrath', 'anger', 'delight']]

    #Act
    actual = hashmap_left_join(synonym_hashmap_2, antonym_hashmap_2)

    #Assert
    assert actual == expected

def test_hashmap_left_join_case_2_reverse(synonym_hashmap_2, antonym_hashmap_2):
    # Arrange
    expected = [['diligent', 'idle', 'employed'], ['flow', 'jam', None], ['fond', 'averse', 'enamored'], ['guide', 'follow', 'usher'], ['wrath', 'delight', 'anger']]

    #Act
    actual = hashmap_left_join(antonym_hashmap_2, synonym_hashmap_2)

    #Assert
    assert actual == expected

def test_hashmap_left_join_exception():
    #Assert
    with pytest.raises(Exception):
        hashmap_left_join('a', 'b')

# Fixtures
# --------------------------------------------------------------------------------
@pytest.fixture
def hashtable():
    return HashTable()


@pytest.fixture
def synonym_hashmap():

    synonym_hashmap = HashTable()

    synonym_hashmap.add('thin','slim')
    synonym_hashmap.add('correct','right')
    synonym_hashmap.add('denied','prohibited')
    synonym_hashmap.add('tidy','clean')
    synonym_hashmap.add('positive','good')
    synonym_hashmap.add('fitting','adequate')
    synonym_hashmap.add('happy','pleased')

    return synonym_hashmap

@pytest.fixture
def synonym_hashmap_2():

    synonym_hashmap_2 = HashTable()
    synonym_hashmap_2.add('fond','enamored')
    synonym_hashmap_2.add('wrath','anger')
    synonym_hashmap_2.add('diligent','employed')
    synonym_hashmap_2.add('outfit','garb')
    synonym_hashmap_2.add('guide','usher')

    return synonym_hashmap_2

@pytest.fixture
def antonym_hashmap():

    antonym_hashmap = HashTable()

    antonym_hashmap.add('thin','fat')
    antonym_hashmap.add('denied','allowed')
    antonym_hashmap.add('positive','negative')
    antonym_hashmap.add('happy','sad')

    return antonym_hashmap

@pytest.fixture
def antonym_hashmap_2():

    antonym_hashmap_2 = HashTable()

    antonym_hashmap_2.add('fond','averse')
    antonym_hashmap_2.add('wrath','delight')
    antonym_hashmap_2.add('diligent','idle')
    antonym_hashmap_2.add('guide','follow')
    antonym_hashmap_2.add('flow','jam')

    return antonym_hashmap_2

