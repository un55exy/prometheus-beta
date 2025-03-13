def binary_search(arr, target):
    """
    Perform an efficient binary search to find the index of a target element in a sorted array.
    
    Args:
        arr (list): A sorted list of comparable elements (ascending order)
        target: The element to search for
    
    Returns:
        int: Index of the target element if found, otherwise -1
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Raises:
        TypeError: If input is not a list
    """
    # Check for invalid input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty array case
    if not arr:
        return -1
    
    # Initialize left and right pointers
    left, right = 0, len(arr) - 1
    
    # Perform binary search
    while left <= right:
        # Calculate midpoint to avoid potential integer overflow
        mid = left + (right - left) // 2
        
        # Check if target is found
        if arr[mid] == target:
            return mid
        
        # If target is less than mid element, search left half
        if arr[mid] > target:
            right = mid - 1
        
        # If target is greater than mid element, search right half
        else:
            left = mid + 1
    
    # Target not found
    return -1