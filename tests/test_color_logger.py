import io
import sys
import pytest
from src.color_logger import ColorLogger

def test_log_default_color():
    """Test default logging with white background"""
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    ColorLogger.log("Test Message")
    sys.stdout = sys.__stdout__
    
    assert "\033[47m" in captured_output.getvalue()
    assert "Test Message" in captured_output.getvalue()
    assert "\033[0m" in captured_output.getvalue()

def test_log_custom_background():
    """Test logging with custom background color"""
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    ColorLogger.log("Test Message", bg_color='blue')
    sys.stdout = sys.__stdout__
    
    assert "\033[44m" in captured_output.getvalue()
    assert "Test Message" in captured_output.getvalue()
    assert "\033[0m" in captured_output.getvalue()

def test_log_with_text_color():
    """Test logging with text color"""
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    ColorLogger.log("Test Message", bg_color='green', text_color='red')
    sys.stdout = sys.__stdout__
    
    assert "\033[42m" in captured_output.getvalue()
    assert "\033[31m" in captured_output.getvalue()
    assert "Test Message" in captured_output.getvalue()
    assert "\033[0m" in captured_output.getvalue()

def test_debug_method():
    """Test debug method with default color"""
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    ColorLogger.debug("Debug Message")
    sys.stdout = sys.__stdout__
    
    assert "\033[46m" in captured_output.getvalue()
    assert "Debug Message" in captured_output.getvalue()

def test_error_method():
    """Test error method with stderr"""
    captured_output = io.StringIO()
    sys.stderr = captured_output
    
    ColorLogger.error("Error Message")
    sys.stderr = sys.__stderr__
    
    assert "\033[41m" in captured_output.getvalue()
    assert "Error Message" in captured_output.getvalue()

def test_invalid_background_color():
    """Test that invalid background color raises ValueError"""
    with pytest.raises(ValueError, match="Invalid background color"):
        ColorLogger.log("Test Message", bg_color='invalid_color')

def test_invalid_text_color():
    """Test that invalid text color raises ValueError"""
    with pytest.raises(ValueError, match="Invalid text color"):
        ColorLogger.log("Test Message", text_color='invalid_color')