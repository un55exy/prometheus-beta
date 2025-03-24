def find_first_last_occurrence(arr, target):
    """
    Find the first and last occurrence of a target element in a sorted array.
    
    Args:
        arr (list): A sorted list of elements (ascending order)
        target: The element to find in the array
    
    Returns:
        tuple: A tuple containing (first_index, last_index)
               If element is not found, returns (-1, -1)
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    # Handle edge cases
    if not arr:
        return (-1, -1)
    
    # Find first occurrence
    first_occurrence = find_boundary(arr, target, True)
    
    # If first occurrence is not found, return (-1, -1)
    if first_occurrence == -1:
        return (-1, -1)
    
    # Find last occurrence
    last_occurrence = find_boundary(arr, target, False)
    
    return (first_occurrence, last_occurrence)

def find_boundary(arr, target, find_first):
    """
    Binary search to find the first or last occurrence of a target.
    
    Args:
        arr (list): A sorted list of elements (ascending order)
        target: The element to find
        find_first (bool): If True, find first occurrence; 
                           if False, find last occurrence
    
    Returns:
        int: Index of the boundary occurrence, or -1 if not found
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            
            # Adjust search direction based on find_first flag
            if find_first:
                right = mid - 1  # Continue searching left for first occurrence
            else:
                left = mid + 1   # Continue searching right for last occurrence
        
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result