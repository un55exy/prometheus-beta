def remove_duplicate_words(text):
    """
    Remove duplicate words from a string while maintaining the original order.

    Args:
        text (str): The input string to process.

    Returns:
        str: A new string with duplicate words removed, preserving original order.

    Examples:
        >>> remove_duplicate_words("the quick brown fox jumps the quick brown fox")
        'the quick brown fox jumps'
        >>> remove_duplicate_words("hello hello world world")
        'hello world'
        >>> remove_duplicate_words("")
        ''
    """
    # Validate input is a string
    if not isinstance(text, str):
        raise AttributeError("Input must be a string")
    
    # Handle empty string case
    if not text:
        return ""
    
    # Split the input string into words
    words = text.split()
    
    # Use a set to track seen words while preserving order
    seen_words = set()
    unique_words = []
    
    for word in words:
        # Only add word if it hasn't been seen before (case-insensitive)
        word_lower = word.lower()
        if word_lower not in seen_words:
            unique_words.append(word)
            seen_words.add(word_lower)
    
    # Join the unique words back into a string
    return " ".join(unique_words)