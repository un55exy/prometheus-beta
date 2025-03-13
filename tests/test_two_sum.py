import pytest
from src.two_sum import two_sum

def test_two_sum_basic_positive():
    """Test basic case where two numbers sum to target"""
    assert two_sum([10, 15, 3, 7], 17) == True

def test_two_sum_basic_negative():
    """Test case where no two numbers sum to target"""
    assert two_sum([10, 15, 3, 7], 19) == False

def test_two_sum_empty_list():
    """Test behavior with empty list"""
    assert two_sum([], 10) == False

def test_two_sum_single_element():
    """Test behavior with single element list"""
    assert two_sum([5], 10) == False

def test_two_sum_same_number():
    """Test case where same number can't be used twice"""
    assert two_sum([3], 6) == False

def test_two_sum_negative_numbers():
    """Test with negative numbers"""
    assert two_sum([-1, -2, 3, 4], 2) == True

def test_two_sum_zero_target():
    """Test with zero as target sum"""
    assert two_sum([-1, 1, 2, -2], 0) == True

def test_two_sum_large_list():
    """Test with a large list"""
    large_list = list(range(1000))
    # Looking for 997 + 1001 = 1998
    assert two_sum(large_list, 1998) == True

def test_two_sum_no_solution():
    """Test case where no solution exists"""
    assert two_sum([1, 2, 3, 4], 10) == False