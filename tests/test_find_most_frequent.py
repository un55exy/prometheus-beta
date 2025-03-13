import pytest
from src.find_most_frequent import find_most_frequent_index

def test_basic_functionality():
    """Test basic cases with clear most frequent element"""
    assert find_most_frequent_index([1, 2, 2, 3, 3, 3]) == 2
    assert find_most_frequent_index([3, 3, 1, 1, 2]) == 0

def test_tie_breaker():
    """Test that the first occurrence is returned in case of a tie"""
    assert find_most_frequent_index([1, 2, 1, 2, 3]) == 0

def test_empty_list():
    """Test handling of empty list"""
    assert find_most_frequent_index([]) is None

def test_single_element():
    """Test list with a single element"""
    assert find_most_frequent_index([5]) == 0

def test_all_unique():
    """Test list where all elements appear once"""
    assert find_most_frequent_index([1, 2, 3, 4, 5]) == 0

def test_multiple_max_freq_elements():
    """Test when multiple elements have the same max frequency"""
    assert find_most_frequent_index([1, 2, 1, 2, 3]) == 0