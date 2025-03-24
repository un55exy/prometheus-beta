import pytest
from src.capitalize_words import capitalize_words

def test_basic_capitalization():
    """Test basic word capitalization."""
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python programming") == "Python Programming"

def test_already_capitalized():
    """Test strings that are already capitalized."""
    assert capitalize_words("Hello World") == "Hello World"

def test_multiple_spaces():
    """Test strings with multiple spaces between words."""
    assert capitalize_words("  hello   world  ") == "Hello World"

def test_empty_string():
    """Test empty string input."""
    assert capitalize_words("") == ""

def test_single_word():
    """Test single word input."""
    assert capitalize_words("hello") == "Hello"

def test_mixed_case():
    """Test string with mixed case."""
    assert capitalize_words("hElLo wOrLd") == "Hello World"

def test_invalid_input_type():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        capitalize_words(123)
    with pytest.raises(TypeError):
        capitalize_words(None)
    with pytest.raises(TypeError):
        capitalize_words(["hello", "world"])

def test_special_characters():
    """Test strings with special characters and numbers."""
    assert capitalize_words("hello world! 123") == "Hello World! 123"