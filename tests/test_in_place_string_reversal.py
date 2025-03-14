import pytest
from src.in_place_string_reversal import reverse_string_in_place

def test_standard_string_reversal():
    """Test reversing a standard string"""
    chars = list('hello')
    reverse_string_in_place(chars)
    assert chars == ['o', 'l', 'l', 'e', 'h']

def test_single_character():
    """Test reversing a single character list"""
    chars = list('a')
    reverse_string_in_place(chars)
    assert chars == ['a']

def test_empty_list():
    """Test reversing an empty list"""
    chars = []
    reverse_string_in_place(chars)
    assert chars == []

def test_even_length_string():
    """Test reversing a string with even number of characters"""
    chars = list('python')
    reverse_string_in_place(chars)
    assert chars == ['n', 'o', 'h', 't', 'y', 'p']

def test_palindrome():
    """Test reversing a palindrome"""
    chars = list('racecar')
    reverse_string_in_place(chars)
    assert chars == ['r', 'a', 'c', 'e', 'c', 'a', 'r']

def test_invalid_input_type():
    """Test that an error is raised for invalid input types"""
    with pytest.raises(TypeError):
        reverse_string_in_place('not a list')

def test_input_modification():
    """Verify that the input list is actually modified in-place"""
    chars = list('world')
    original_id = id(chars)
    reverse_string_in_place(chars)
    
    # Check that the list is modified in-place (same memory address)
    assert id(chars) == original_id
    assert chars == ['d', 'l', 'r', 'o', 'w']