from typing import List, Union

def multiply(arrays: List[List[Union[int, float]]]) -> List[Union[int, float]]:
    """
    Multiply corresponding elements from multiple input arrays.

    Args:
        arrays (List[List[Union[int, float]]]): A list of arrays to multiply element-wise.

    Returns:
        List[Union[int, float]]: A new array with elements multiplied.

    Raises:
        ValueError: If input arrays are empty or have different lengths.
    
    Examples:
        >>> multiply([[1, 2, 3], [4, 5, 6]])
        [4, 10, 18]
        >>> multiply([[2, 2], [3, 3]])
        [6, 6]
    """
    # Check if input is empty
    if not arrays:
        raise ValueError("Input list of arrays cannot be empty")
    
    # Check if all arrays have the same length
    if len(set(len(arr) for arr in arrays)) > 1:
        raise ValueError("All input arrays must have the same length")
    
    # Perform element-wise multiplication
    return [
        # Multiply corresponding elements across all input arrays
        # Use math.prod() if Python 3.8+, or use reduce for earlier versions
        # This works for any number of input arrays
        multiply_single_position(arrays, pos) 
        for pos in range(len(arrays[0]))
    ]

def multiply_single_position(arrays: List[List[Union[int, float]]], position: int) -> Union[int, float]:
    """
    Multiply elements at a specific position across all arrays.

    Args:
        arrays (List[List[Union[int, float]]]): Input arrays
        position (int): Position to multiply

    Returns:
        Union[int, float]: Product of elements at given position
    """
    result = 1
    for arr in arrays:
        result *= arr[position]
    return result