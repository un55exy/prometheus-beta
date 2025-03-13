def two_sum(numbers, target_sum):
    """
    Determine if there exist two numbers in the given array that sum to the target.

    Args:
        numbers (list): A list of integers to search through
        target_sum (int): The target sum to find

    Returns:
        bool: True if two numbers in the array sum to the target, False otherwise

    Time Complexity: O(n)
    Space Complexity: O(n)

    Examples:
        >>> two_sum([10, 15, 3, 7], 17)
        True
        >>> two_sum([10, 15, 3, 7], 19)
        False
        >>> two_sum([], 10)
        False
    """
    # Handle edge cases
    if len(numbers) < 2:
        return False

    # Use a set to track numbers we've seen
    seen = set()

    # Iterate through the numbers
    for num in numbers:
        # Calculate the complement needed to reach target_sum
        complement = target_sum - num

        # If complement is already in seen, we found a pair
        if complement in seen:
            return True

        # Add current number to seen set
        seen.add(num)

    # No pair found that sums to target
    return False