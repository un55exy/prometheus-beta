import os
import typing


def create_directory(path: str, mode: int = 0o755) -> bool:
    """
    Create a new directory with the specified path and optional permissions.

    Args:
        path (str): The path of the directory to create.
        mode (int, optional): The file mode (permissions) to set for the directory. 
                               Defaults to 0o755 (rwxr-xr-x).

    Returns:
        bool: True if the directory was created successfully, False if it already exists.

    Raises:
        PermissionError: If the user lacks permission to create the directory.
        OSError: For other OS-related errors during directory creation.
    """
    try:
        # Expand and normalize the path
        full_path = os.path.abspath(os.path.expanduser(path))
        
        # Validate path
        if not os.path.dirname(full_path):
            raise OSError(f"Invalid path: {full_path}")
        
        # Check parent directories exist
        parent_dir = os.path.dirname(full_path)
        if not os.path.exists(parent_dir):
            raise OSError(f"Parent directory does not exist: {parent_dir}")
        
        # Check if directory already exists
        if os.path.exists(full_path):
            return False
        
        # Create directory with specified mode
        os.mkdir(full_path, mode=mode)
        return True
    
    except PermissionError:
        raise PermissionError(f"Permission denied: Unable to create directory {path}")
    except OSError as e:
        raise OSError(f"Error creating directory {path}: {str(e)}")