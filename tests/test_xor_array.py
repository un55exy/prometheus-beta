import pytest
from src.xor_array import xor_array_elements

def test_xor_array_basic():
    """Test basic XOR operation with simple array"""
    assert xor_array_elements([1, 2, 3]) == 0
    assert xor_array_elements([5, 7, 2]) == 4

def test_xor_array_single_element():
    """Test XOR with a single element"""
    assert xor_array_elements([42]) == 42

def test_xor_array_zero_elements():
    """Test XOR with zero elements"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        xor_array_elements([])

def test_xor_array_invalid_input():
    """Test invalid input types"""
    with pytest.raises(TypeError, match="Input must be a list"):
        xor_array_elements("not a list")
    
    with pytest.raises(TypeError, match="All elements must be integers"):
        xor_array_elements([1, 2, "3"])
    
    with pytest.raises(TypeError, match="All elements must be integers"):
        xor_array_elements([1, 2, 3.5])

def test_xor_array_large_numbers():
    """Test XOR with larger numbers"""
    assert xor_array_elements([100, 200, 300]) == 200

def test_xor_array_repeated_elements():
    """Test XOR with repeated elements"""
    assert xor_array_elements([10, 10, 10]) == 10