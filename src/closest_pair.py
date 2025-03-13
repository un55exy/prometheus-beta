def find_closest_pair(numbers):
    """
    Find the closest pair of numbers in the given array.
    
    Args:
        numbers (list): A list of numbers to find the closest pair from.
    
    Returns:
        tuple: A tuple containing two numbers that are closest to each other.
               In case of a tie, returns the pair with the smallest numbers.
    
    Raises:
        ValueError: If the input list has fewer than 2 numbers.
    """
    # Check for invalid input
    if not numbers or len(numbers) < 2:
        raise ValueError("Input list must contain at least two numbers")
    
    # Sort the list to help with finding the closest pair
    sorted_nums = sorted(numbers)
    
    # Initialize minimum difference with the first two sorted numbers
    min_diff = float('inf')
    closest_pair = (sorted_nums[0], sorted_nums[1])
    
    # Iterate through the sorted list to find the closest pair
    for i in range(1, len(sorted_nums)):
        current_diff = sorted_nums[i] - sorted_nums[i-1]
        
        # Update if current difference is smaller
        if current_diff < min_diff:
            min_diff = current_diff
            closest_pair = (sorted_nums[i-1], sorted_nums[i])
        
        # If differences are equal, choose the pair with smaller numbers
        elif current_diff == min_diff:
            # Compare the pairs lexicographically
            if (sorted_nums[i-1], sorted_nums[i]) < closest_pair:
                closest_pair = (sorted_nums[i-1], sorted_nums[i])
    
    return closest_pair