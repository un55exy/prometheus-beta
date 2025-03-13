def sum_unique_even_numbers(numbers):
    """
    Calculate the sum of even numbers that appear only once in the input array.
    
    Args:
        numbers (list): A list of integers to process.
    
    Returns:
        int: Sum of even numbers that appear exactly once in the input list.
    
    Examples:
        >>> sum_unique_even_numbers([1, 2, 3, 4, 2, 6])
        10
        >>> sum_unique_even_numbers([1, 3, 5])
        0
        >>> sum_unique_even_numbers([2, 4, 6, 2, 4])
        0
    """
    # Group even and odd numbers
    unique_even_map = {}
    for num in numbers:
        if num % 2 == 0:
            unique_even_map[num] = unique_even_map.get(num, 0) + 1
    
    # Sum only unique even numbers
    unique_even_sum = sum(
        num for num, count in unique_even_map.items() 
        if count == 1
    )
    
    return unique_even_sum