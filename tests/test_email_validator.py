import pytest
from src.email_validator import validate_email_format

def test_valid_emails():
    """Test a variety of valid email formats."""
    valid_emails = [
        "user@example.com",
        "first.last@example.co.uk",
        "user+tag@example.org",
        "user123@example.net",
        "user-name@example.io",
        "user_name@example.com"
    ]
    for email in valid_emails:
        assert validate_email_format(email) is True, f"{email} should be valid"

def test_invalid_emails():
    """Test various invalid email formats."""
    invalid_emails = [
        "",  # Empty string
        None,  # None value
        "invalid.email",  # No @ symbol
        "@missing.username",  # Missing username
        "user@.com",  # Missing domain name
        "user@domain",  # Missing top-level domain
        "user@domain.",  # Incomplete top-level domain
        "user@domain..com",  # Double dot in domain
        "user@-domain.com",  # Invalid domain start
        "user@domain.-com",  # Invalid domain end
        "user name@example.com",  # Spaces in username
        f"{'a' * 65}@example.com",  # Username too long
        f"user@{'a' * 256}.com",  # Domain too long
        f"user@example.{'a' * 64}"  # Too long top-level domain
    ]
    for email in invalid_emails:
        assert validate_email_format(email) is False, f"{email} should be invalid"

def test_email_length_limits():
    """Test email address length limits."""
    # Maximum allowed total length is 254 characters
    long_username = "a" * 64
    valid_long_email = f"{long_username}@example.com"
    assert validate_email_format(valid_long_email) is True
    
    # Exceeding total length
    too_long_email = f"{long_username}x@example.com"
    assert validate_email_format(too_long_email) is False

def test_email_formatting():
    """Additional tests for specific formatting rules."""
    # Test various valid and invalid formatting scenarios
    assert validate_email_format("user.name+tag@example.co.uk") is True
    assert validate_email_format("user@subdomain.example.com") is True
    assert validate_email_format("user@domain") is False  # No top-level domain
    assert validate_email_format("user@.com") is False  # Incomplete domain