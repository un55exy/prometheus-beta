import pytest
from src.find_duplicates import find_duplicates

def test_find_duplicates_basic():
    """Test basic duplicate finding"""
    assert find_duplicates([1, 2, 3, 4, 2, 5, 6, 3]) == [2, 3]

def test_find_duplicates_multiple_duplicates():
    """Test with multiple duplicates of the same number"""
    assert find_duplicates([1, 1, 1, 1]) == [1]

def test_find_duplicates_no_duplicates():
    """Test with no duplicates"""
    assert find_duplicates([1, 2, 3, 4, 5]) == []

def test_find_duplicates_empty_list():
    """Test with an empty list"""
    assert find_duplicates([]) == []

def test_find_duplicates_sorted_output():
    """Ensure output is sorted"""
    assert find_duplicates([5, 4, 3, 3, 2, 2, 1, 1]) == [1, 2, 3]

def test_find_duplicates_large_list():
    """Test with a larger list of numbers"""
    large_list = [1, 2, 3] * 10 + [4, 5, 6]
    assert find_duplicates(large_list) == [1, 2, 3]