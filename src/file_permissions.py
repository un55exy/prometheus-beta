import os
import stat

def get_file_permissions(file_path):
    """
    Get the file permissions of a given file.

    Args:
        file_path (str): The path to the file.

    Returns:
        dict: A dictionary containing file permission details with keys:
            - 'numeric': Numeric representation of permissions (e.g., 644)
            - 'readable': Human-readable permission string (e.g., 'rw-r--r--')
            - 'owner_read': Boolean indicating if owner has read permission
            - 'owner_write': Boolean indicating if owner has write permission
            - 'owner_execute': Boolean indicating if owner has execute permission
            - 'group_read': Boolean indicating if group has read permission
            - 'group_write': Boolean indicating if group has write permission
            - 'group_execute': Boolean indicating if group has execute permission
            - 'others_read': Boolean indicating if others have read permission
            - 'others_write': Boolean indicating if others have write permission
            - 'others_execute': Boolean indicating if others have execute permission

    Raises:
        FileNotFoundError: If the file does not exist
        PermissionError: If there's no permission to access the file
    """
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        # Get file stats
        file_stat = os.stat(file_path)
        
        # Get numeric mode
        mode = file_stat.st_mode
        numeric_mode = stat.S_IMODE(mode)
        
        # Convert to numeric representation (e.g., 644)
        numeric_permissions = int(str(oct(numeric_mode))[2:].zfill(3))
        
        # Create readable permission string
        readable_permissions = ''
        permission_groups = [
            (stat.S_IRUSR, stat.S_IWUSR, stat.S_IXUSR),  # Owner
            (stat.S_IRGRP, stat.S_IWGRP, stat.S_IXGRP),  # Group
            (stat.S_IROTH, stat.S_IWOTH, stat.S_IXOTH)   # Others
        ]
        
        for read_perm, write_perm, exec_perm in permission_groups:
            readable_permissions += 'r' if mode & read_perm else '-'
            readable_permissions += 'w' if mode & write_perm else '-'
            readable_permissions += 'x' if mode & exec_perm else '-'
        
        return {
            'numeric': numeric_permissions,
            'readable': readable_permissions,
            'owner_read': bool(mode & stat.S_IRUSR),
            'owner_write': bool(mode & stat.S_IWUSR),
            'owner_execute': bool(mode & stat.S_IXUSR),
            'group_read': bool(mode & stat.S_IRGRP),
            'group_write': bool(mode & stat.S_IWGRP),
            'group_execute': bool(mode & stat.S_IXGRP),
            'others_read': bool(mode & stat.S_IROTH),
            'others_write': bool(mode & stat.S_IWOTH),
            'others_execute': bool(mode & stat.S_IXOTH)
        }
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing file: {file_path}")