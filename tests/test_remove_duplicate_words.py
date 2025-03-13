import pytest
from src.remove_duplicate_words import remove_duplicate_words

def test_remove_duplicate_words_basic():
    """Test basic duplicate word removal."""
    assert remove_duplicate_words("the quick brown fox jumps the quick brown fox") == "the quick brown fox jumps"

def test_remove_duplicate_words_consecutive():
    """Test consecutive duplicate words."""
    assert remove_duplicate_words("hello hello world world") == "hello world"

def test_remove_duplicate_words_empty_string():
    """Test empty string input."""
    assert remove_duplicate_words("") == ""

def test_remove_duplicate_words_no_duplicates():
    """Test input with no duplicate words."""
    assert remove_duplicate_words("hello world python") == "hello world python"

def test_remove_duplicate_words_mixed_case():
    """Test case sensitivity of duplicate removal."""
    assert remove_duplicate_words("Hello hello World world") == "Hello World"

def test_remove_duplicate_words_multiple_duplicates():
    """Test multiple duplicate words in different positions."""
    assert remove_duplicate_words("a b c a b c a b c") == "a b c"

def test_remove_duplicate_words_type_error():
    """Test type error handling."""
    with pytest.raises(AttributeError):
        remove_duplicate_words(None)
    with pytest.raises(AttributeError):
        remove_duplicate_words(123)