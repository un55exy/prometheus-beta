import pytest
from src.unique_even_sum import sum_unique_even_numbers

def test_sum_unique_even_numbers_basic():
    """Test basic functionality of summing unique even numbers."""
    assert sum_unique_even_numbers([1, 2, 3, 4, 2, 6]) == 10
    assert sum_unique_even_numbers([2, 4, 6, 2, 4]) == 0
    assert sum_unique_even_numbers([1, 3, 5]) == 0

def test_sum_unique_even_numbers_edge_cases():
    """Test edge cases for the function."""
    # Empty list
    assert sum_unique_even_numbers([]) == 0
    
    # List with only repeated even numbers
    assert sum_unique_even_numbers([2, 2, 4, 4, 6, 6]) == 0
    
    # List with unique negative even numbers
    assert sum_unique_even_numbers([-2, 1, -4, 3]) == -6

def test_sum_unique_even_numbers_types():
    """Test function behavior with different input types."""
    # Mixed positive and negative even numbers
    assert sum_unique_even_numbers([-2, 2, 3, -4, 4]) == -6
    
    # Large numbers
    assert sum_unique_even_numbers([10000, 20000, 10000, 30000]) == 50000