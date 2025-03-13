import pytest
from src.binary_search import binary_search

def test_binary_search_normal_cases():
    """Test binary search with typical scenarios"""
    # Basic sorted array cases
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 1) == 0
    assert binary_search([1, 2, 3, 4, 5], 5) == 4

def test_binary_search_not_found():
    """Test cases where target is not in the array"""
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([1, 2, 3, 4, 5], 0) == -1

def test_binary_search_edge_cases():
    """Test edge cases"""
    # Empty array
    assert binary_search([], 5) == -1
    
    # Single element array
    assert binary_search([1], 1) == 0
    assert binary_search([1], 2) == -1

def test_binary_search_duplicate_elements():
    """Test array with duplicate elements"""
    # Return the first occurrence
    assert binary_search([1, 2, 2, 3, 3, 3, 4], 3) in [3, 4, 5]

def test_binary_search_large_array():
    """Test with a larger sorted array"""
    large_arr = list(range(1000))
    assert binary_search(large_arr, 500) == 500
    assert binary_search(large_arr, 999) == 999
    assert binary_search(large_arr, 1000) == -1

def test_binary_search_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        binary_search(None, 5)
    with pytest.raises(TypeError):
        binary_search("not a list", 5)
    with pytest.raises(TypeError):
        binary_search(5, 5)