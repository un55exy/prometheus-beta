def xor_array_elements(arr):
    """
    Calculate the XOR of all elements in the given array.

    Args:
        arr (list): A list of integers to perform XOR operation on.

    Returns:
        int: The result of XORing all elements in the array.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
        ValueError: If the input list is empty.

    Examples:
        >>> xor_array_elements([1, 2, 3])
        0
        >>> xor_array_elements([5, 7, 2])
        4
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Check all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Perform XOR of all elements
    result = arr[0]
    for x in arr[1:]:
        result ^= x
    
    return result