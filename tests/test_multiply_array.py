import pytest
from src.multiply_array import multiply

def test_multiply_two_arrays():
    """Test multiplication of two arrays with positive integers."""
    result = multiply([[1, 2, 3], [4, 5, 6]])
    assert result == [4, 10, 18]

def test_multiply_float_arrays():
    """Test multiplication of arrays with float values."""
    result = multiply([[1.5, 2.0], [2.0, 3.0]])
    assert result == [3.0, 6.0]

def test_multiply_multiple_arrays():
    """Test multiplication of more than two arrays."""
    result = multiply([[1, 2], [3, 4], [5, 6]])
    assert result == [15, 48]

def test_empty_input_raises_error():
    """Test that an empty input raises a ValueError."""
    with pytest.raises(ValueError, match="Input list of arrays cannot be empty"):
        multiply([])

def test_different_length_arrays_raises_error():
    """Test that arrays of different lengths raise a ValueError."""
    with pytest.raises(ValueError, match="All input arrays must have the same length"):
        multiply([[1, 2], [3, 4, 5]])

def test_single_array():
    """Test multiplication with a single array."""
    result = multiply([[2, 3, 4]])
    assert result == [2, 3, 4]

def test_zero_values():
    """Test multiplication with zero values."""
    result = multiply([[1, 0, 3], [2, 5, 0]])
    assert result == [2, 0, 0]

def test_negative_values():
    """Test multiplication with negative values."""
    result = multiply([[-1, 2], [3, -4]])
    assert result == [-3, -8]