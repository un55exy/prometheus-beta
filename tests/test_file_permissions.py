import os
import stat
import pytest
import tempfile

from src.file_permissions import get_file_permissions

def create_temp_file(mode):
    """Create a temporary file with specified permissions."""
    # Create a temporary file
    temp_file = tempfile.mkstemp()[1]
    
    # Set the specified permissions
    os.chmod(temp_file, mode)
    
    return temp_file

def test_get_file_permissions_basic():
    """Test basic file permissions retrieval."""
    # Create a temp file with known permissions
    temp_file = create_temp_file(0o644)
    
    try:
        # Get file permissions
        perms = get_file_permissions(temp_file)
        
        # Check numeric permissions
        assert perms['numeric'] == 644
        
        # Check boolean permissions
        assert perms['owner_read'] is True
        assert perms['owner_write'] is True
        assert perms['owner_execute'] is False
        assert perms['group_read'] is True
        assert perms['group_write'] is False
        assert perms['group_execute'] is False
        assert perms['others_read'] is True
        assert perms['others_write'] is False
        assert perms['others_execute'] is False
    finally:
        # Clean up the temporary file
        os.unlink(temp_file)

def test_get_file_permissions_full_access():
    """Test file permissions with full access."""
    # Create a temp file with full read/write/execute permissions
    temp_file = create_temp_file(0o777)
    
    try:
        # Get file permissions
        perms = get_file_permissions(temp_file)
        
        # Check all permissions are True
        assert perms['owner_read'] is True
        assert perms['owner_write'] is True
        assert perms['owner_execute'] is True
        assert perms['group_read'] is True
        assert perms['group_write'] is True
        assert perms['group_execute'] is True
        assert perms['others_read'] is True
        assert perms['others_write'] is True
        assert perms['others_execute'] is True
    finally:
        # Clean up the temporary file
        os.unlink(temp_file)

def test_get_file_permissions_no_access():
    """Test file permissions with no access."""
    # Create a temp file with no permissions
    temp_file = create_temp_file(0o000)
    
    try:
        # Get file permissions
        perms = get_file_permissions(temp_file)
        
        # Check all permissions are False
        assert perms['owner_read'] is False
        assert perms['owner_write'] is False
        assert perms['owner_execute'] is False
        assert perms['group_read'] is False
        assert perms['group_write'] is False
        assert perms['group_execute'] is False
        assert perms['others_read'] is False
        assert perms['others_write'] is False
        assert perms['others_execute'] is False
    finally:
        # Clean up the temporary file
        os.unlink(temp_file)

def test_get_file_permissions_nonexistent_file():
    """Test that FileNotFoundError is raised for nonexistent file."""
    with pytest.raises(FileNotFoundError):
        get_file_permissions('/path/to/nonexistent/file')

def test_get_file_permissions_readable_format():
    """Test the readable permissions format."""
    # Create a temp file with known permissions
    temp_file = create_temp_file(0o644)
    
    try:
        # Get file permissions
        perms = get_file_permissions(temp_file)
        
        # Check readable format 
        # For 0o644, it should be 'rw-r--r--'
        assert perms['readable'] == 'rw-r--r--'
    finally:
        # Clean up the temporary file
        os.unlink(temp_file)