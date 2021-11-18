"""This module tests Hash Table Module"""

from hashtable.hashtable import HashTable
import pytest


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

@pytest.fixture
def hashtable():
    return HashTable()
