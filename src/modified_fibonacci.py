def generate_modified_fibonacci(n):
    """
    Generate a modified Fibonacci sequence where the sum of any two consecutive 
    numbers (starting from the third number) is always divisible by 3.

    Args:
        n (int): The maximum number of elements in the sequence to generate.

    Returns:
        list: A modified Fibonacci sequence satisfying the divisibility condition.

    Raises:
        ValueError: If n is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")

    # Special handling for small sequences
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]

    # Start with initial sequence
    sequence = [1, 1]

    # Generate sequence while modifying to meet divisibility condition
    while len(sequence) < n:
        # Compute next number to ensure divisibility from 3rd element
        if len(sequence) == 2:
            # First modification will make the third number 3
            next_num = 3
        else:
            # Ensure divisibility by adding a correction factor
            next_num = 3 - (sequence[-1] + sequence[-2]) % 3 + sequence[-1] + sequence[-2]
        
        sequence.append(next_num)

    # Ensure exact sequence length
    return sequence[:n]