import sys
import io
import pytest
from src.color_logger import ColorLogger

def test_log_default_color():
    """Test default logging with white background"""
    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()
    
    try:
        ColorLogger.log("Test Message")
    finally:
        sys.stdout = old_stdout
    
    output = captured_output.getvalue()
    assert "\x1b[47m" in output
    assert "Test Message" in output
    assert "\x1b[0m" in output

def test_log_custom_background():
    """Test logging with custom background color"""
    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()
    
    try:
        ColorLogger.log("Test Message", bg_color='blue')
    finally:
        sys.stdout = old_stdout
    
    output = captured_output.getvalue()
    assert "\x1b[44m" in output
    assert "Test Message" in output
    assert "\x1b[0m" in output

def test_log_with_text_color():
    """Test logging with text color"""
    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()
    
    try:
        ColorLogger.log("Test Message", bg_color='green', text_color='red')
    finally:
        sys.stdout = old_stdout
    
    output = captured_output.getvalue()
    assert "\x1b[42m" in output
    assert "\x1b[31m" in output
    assert "Test Message" in output
    assert "\x1b[0m" in output

def test_debug_method():
    """Test debug method with default color"""
    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()
    
    try:
        ColorLogger.debug("Debug Message")
    finally:
        sys.stdout = old_stdout
    
    output = captured_output.getvalue()
    assert "\x1b[46m" in output
    assert "Debug Message" in output

def test_error_method():
    """Test error method with stderr"""
    # Capture stderr
    old_stderr = sys.stderr
    sys.stderr = captured_output = io.StringIO()
    
    try:
        ColorLogger.error("Error Message")
    finally:
        sys.stderr = old_stderr
    
    output = captured_output.getvalue()
    assert "\x1b[41m" in output
    assert "Error Message" in output

def test_invalid_background_color():
    """Test that invalid background color raises ValueError"""
    with pytest.raises(ValueError, match="Invalid background color"):
        ColorLogger.log("Test Message", bg_color='invalid_color')

def test_invalid_text_color():
    """Test that invalid text color raises ValueError"""
    with pytest.raises(ValueError, match="Invalid text color"):
        ColorLogger.log("Test Message", text_color='invalid_color')