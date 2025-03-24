import re

def validate_email_format(email: str) -> bool:
    """
    Validate the format of an email address.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email format is valid, False otherwise.
    
    Validates the email address based on the following criteria:
    - Must have a username part before the '@' symbol
    - Must have a domain name after the '@' symbol
    - Username can contain letters, numbers, dots, underscores, and hyphens
    - Domain must have at least one dot, no consecutive dots
    - Total length constraints
    """
    # Check if email is a string and not empty
    if not isinstance(email, str) or not email:
        return False
    
    # Regular expression for email validation with stricter domain checks
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z]{2,})+$'
    
    # Check overall email format
    if not re.match(email_regex, email):
        return False
    
    # Check total email length
    if len(email) > 254:  # Maximum total email length
        return False
    
    # Split email into username and domain
    username, domain = email.rsplit('@', 1)
    
    # Check username length
    if len(username) > 64:
        return False
    
    # Check domain length
    if len(domain) > 255:
        return False
    
    return True