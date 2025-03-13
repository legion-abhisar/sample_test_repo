# test_sample.py
import pytest

def test_addition():
    assert 2 + 3 == 5

def test_subtraction():
    assert 5 - 3 == 2

def test_multiplication():
    assert 4 * 2 == 8

def test_division():
    assert 8 / 2 == 4

def test_string_concatenation():
    assert "Hello " + "World" == "Hello World"

def test_list_length():
    assert len([1, 2, 3]) == 3

def test_dict_value():
    assert {"key": "value"}["key"] == "value"

def test_set_membership():
    assert 3 in {1, 2, 3}

def test_tuple_indexing():
    assert (1, 2, 3)[1] == 2

def test_boolean_logic():
    assert True and True