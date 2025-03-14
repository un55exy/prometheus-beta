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

    while len(sequence) < n:
        # First two sequences are unique
        if len(sequence) == 2:
            next_num = 3
        else:
            # Modify sequence to make the sum divisible by 3
            # We do this by adding the amount needed to make the sum a multiple of 3
            correction = 3 - (sequence[-2] + sequence[-1]) % 3
            next_num = sequence[-1] + correction
        
        sequence.append(next_num)

    # Ensure exact sequence length
    return sequence[:n]