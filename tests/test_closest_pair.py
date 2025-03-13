import pytest
from src.closest_pair import find_closest_pair

def test_basic_closest_pair():
    """Test finding the closest pair in a simple list."""
    assert find_closest_pair([1, 3, 5, 7, 9]) == (1, 3)

def test_negative_numbers():
    """Test finding closest pair with negative numbers."""
    assert find_closest_pair([-5, -2, 0, 3, 7]) == (-2, 0)

def test_duplicate_numbers():
    """Test finding closest pair with duplicate numbers."""
    assert find_closest_pair([1, 1, 5, 5, 10]) == (1, 1)

def test_floating_point_numbers():
    """Test finding closest pair with floating point numbers."""
    assert find_closest_pair([1.1, 1.5, 2.0, 3.7]) == (1.1, 1.5)

def test_tie_breaking():
    """Test that the function returns the pair with smaller numbers in case of a tie."""
    assert find_closest_pair([1, 3, 4, 6, 7]) == (3, 4)
    assert find_closest_pair([10, 12, 14, 16]) == (10, 12)

def test_unsorted_input():
    """Test that the function works with unsorted input."""
    assert find_closest_pair([7, 1, 5, 3, 9]) == (1, 3)

def test_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError):
        find_closest_pair([])
    
    with pytest.raises(ValueError):
        find_closest_pair([42])

def test_large_list():
    """Test performance and correctness with a larger list."""
    large_list = list(range(0, 1000, 2)) + [999]
    assert find_closest_pair(large_list) == (998, 999)

def test_all_identical_numbers():
    """Test a list with all identical numbers."""
    assert find_closest_pair([5, 5, 5, 5]) == (5, 5)