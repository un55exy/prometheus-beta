import os
import pytest
import tempfile

from src.file_reader import read_file_contents

def test_read_existing_file():
    """Test reading contents of an existing file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello, world!")
        temp_file.close()
        
        try:
            content = read_file_contents(temp_file.name)
            assert content == "Hello, world!"
        finally:
            os.unlink(temp_file.name)

def test_read_empty_file():
    """Test reading an empty file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.close()
        
        try:
            content = read_file_contents(temp_file.name)
            assert content == ""
        finally:
            os.unlink(temp_file.name)

def test_read_nonexistent_file():
    """Test attempting to read a nonexistent file."""
    with pytest.raises(FileNotFoundError):
        read_file_contents("nonexistent_file_123456.txt")

def test_read_file_with_unicode():
    """Test reading a file with unicode characters."""
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as temp_file:
        temp_file.write("Héllo, wörld! 🌍")
        temp_file.close()
        
        try:
            content = read_file_contents(temp_file.name)
            assert content == "Héllo, wörld! 🌍"
        finally:
            os.unlink(temp_file.name)

def test_read_file_large_content():
    """Test reading a large file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        large_content = "Test content\n" * 1000
        temp_file.write(large_content)
        temp_file.close()
        
        try:
            content = read_file_contents(temp_file.name)
            assert content == large_content
        finally:
            os.unlink(temp_file.name)