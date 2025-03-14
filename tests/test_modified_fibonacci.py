import pytest
from src.modified_fibonacci import generate_modified_fibonacci

def test_generate_modified_fibonacci_basic():
    """Test basic functionality of the modified Fibonacci sequence."""
    result = generate_modified_fibonacci(5)
    assert len(result) == 5
    
    # Only check divisibility for sequences with at least 3 elements
    if len(result) >= 3:
        # Verify that from the 3rd element onward, pair sums are divisible by 3
        for i in range(2, len(result)):
            assert (result[i-2] + result[i-1]) % 3 == 0, \
                f"Failed at index {i}: {result[i-2]} + {result[i-1]} not divisible by 3"

def test_divisibility_condition():
    """Verify that the sum of consecutive numbers is divisible by 3."""
    sequence = generate_modified_fibonacci(10)
    
    # Verify divisibility for sequences with at least 3 elements
    if len(sequence) >= 3:
        # Check divisibility from the 3rd element onward
        for i in range(2, len(sequence)):
            assert (sequence[i-2] + sequence[i-1]) % 3 == 0, \
                f"Failed at index {i}: {sequence[i-2]} + {sequence[i-1]} not divisible by 3"

def test_single_element():
    """Test generating sequence with single element."""
    result = generate_modified_fibonacci(1)
    assert result == [1]

def test_two_elements():
    """Test generating sequence with two elements."""
    result = generate_modified_fibonacci(2)
    assert result == [1, 1]

def test_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        generate_modified_fibonacci(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        generate_modified_fibonacci(-1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        generate_modified_fibonacci(1.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        generate_modified_fibonacci("not a number")