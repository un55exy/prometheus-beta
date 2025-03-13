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
        6
    """
    # Count occurrences of each even number
    even_counts = {}
    for num in numbers:
        if num % 2 == 0:
            even_counts[num] = even_counts.get(num, 0) + 1
    
    # Sum unique even numbers (those appearing exactly once)
    unique_even_sum = sum(
        num for num, count in even_counts.items() 
        if count == 1
    )
    
    return unique_even_sum