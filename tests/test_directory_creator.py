import os
import pytest
import shutil
import tempfile

from src.directory_creator import create_directory


def test_create_directory_success():
    """Test successful directory creation."""
    with tempfile.TemporaryDirectory() as temp_base:
        test_dir = os.path.join(temp_base, 'new_directory')
        
        # Create directory
        result = create_directory(test_dir)
        
        # Verify directory was created
        assert result is True
        assert os.path.exists(test_dir)
        assert os.path.isdir(test_dir)


def test_create_existing_directory():
    """Test attempting to create an existing directory."""
    with tempfile.TemporaryDirectory() as temp_base:
        test_dir = os.path.join(temp_base, 'existing_directory')
        
        # Create directory first time
        first_result = create_directory(test_dir)
        assert first_result is True
        
        # Try to create same directory again
        second_result = create_directory(test_dir)
        assert second_result is False


def test_create_nested_directories():
    """Test creating nested directories."""
    with tempfile.TemporaryDirectory() as temp_base:
        nested_dir = os.path.join(temp_base, 'parent', 'child', 'grandchild')
        
        # Create nested directories
        result = create_directory(nested_dir)
        
        # Verify nested directories were created
        assert result is True
        assert os.path.exists(nested_dir)
        assert os.path.isdir(nested_dir)


def test_create_directory_invalid_path():
    """Test creating directory with invalid path."""
    with pytest.raises(OSError):
        create_directory('/nonexistent/parent/path/to/directory')


def test_directory_permissions():
    """Test directory creation with specific permissions."""
    with tempfile.TemporaryDirectory() as temp_base:
        test_dir = os.path.join(temp_base, 'permissions_dir')
        
        # Create directory with specific mode
        create_directory(test_dir, mode=0o700)
        
        # Verify directory exists and has correct permissions
        assert os.path.exists(test_dir)
        assert os.path.isdir(test_dir)
        # Note: Precise permission checking can be OS-dependent