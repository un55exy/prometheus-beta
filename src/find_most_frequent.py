from typing import List, Optional
from collections import Counter

def find_most_frequent_index(nums: List[int]) -> Optional[int]:
    """
    Find the index of the integer with the highest frequency in the list.
    
    Args:
        nums (List[int]): Input list of integers
    
    Returns:
        Optional[int]: Index of the first occurrence of the most frequent integer.
                       Returns None if the input list is empty.
    
    Examples:
        >>> find_most_frequent_index([1, 2, 2, 3, 3, 3])
        2
        >>> find_most_frequent_index([1, 1, 2, 2, 3])
        0
        >>> find_most_frequent_index([])
        None
    """
    # Handle empty list case
    if not nums:
        return None
    
    # Count frequencies of each number
    freq_counter = Counter(nums)
    
    # Find the maximum frequency
    max_freq = max(freq_counter.values())
    
    # Iterate through original list to get first occurrence of most frequent
    for i, num in enumerate(nums):
        if freq_counter[num] == max_freq:
            return i