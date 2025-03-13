import pytest
from src.replace_hyphens import replace_hyphens_with_spaces

def test_replace_hyphens_basic():
    """Test basic hyphen replacement."""
    assert replace_hyphens_with_spaces('hello-world') == 'hello world'

def test_replace_multiple_hyphens():
    """Test replacing multiple hyphens in a string."""
    assert replace_hyphens_with_spaces('python-is-awesome') == 'python is awesome'

def test_no_hyphens():
    """Test string with no hyphens remains unchanged."""
    assert replace_hyphens_with_spaces('pythonisawesome') == 'pythonisawesome'

def test_empty_string():
    """Test empty string handling."""
    assert replace_hyphens_with_spaces('') == ''

def test_only_hyphens():
    """Test string with only hyphens."""
    assert replace_hyphens_with_spaces('----') == '    '

def test_invalid_input_type():
    """Test raising TypeError for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_hyphens_with_spaces(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_hyphens_with_spaces(None)