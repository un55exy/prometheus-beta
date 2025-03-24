import io
import sys
import pytest
from src.color_logger import ColorLogger

def test_log_default_color(capsys):
    """Test default logging with white background"""
    ColorLogger.log("Test Message")
    captured = capsys.readouterr()
    
    assert "\x1b[47m" in captured.out
    assert "Test Message" in captured.out
    assert "\x1b[0m" in captured.out

def test_log_custom_background(capsys):
    """Test logging with custom background color"""
    ColorLogger.log("Test Message", bg_color='blue')
    captured = capsys.readouterr()
    
    assert "\x1b[44m" in captured.out
    assert "Test Message" in captured.out
    assert "\x1b[0m" in captured.out

def test_log_with_text_color(capsys):
    """Test logging with text color"""
    ColorLogger.log("Test Message", bg_color='green', text_color='red')
    captured = capsys.readouterr()
    
    assert "\x1b[42m" in captured.out
    assert "\x1b[31m" in captured.out
    assert "Test Message" in captured.out
    assert "\x1b[0m" in captured.out

def test_debug_method(capsys):
    """Test debug method with default color"""
    ColorLogger.debug("Debug Message")
    captured = capsys.readouterr()
    
    assert "\x1b[46m" in captured.out
    assert "Debug Message" in captured.out

def test_error_method(capsys):
    """Test error method with stderr"""
    ColorLogger.error("Error Message")
    captured = capsys.readouterr()
    
    assert "\x1b[41m" in captured.err
    assert "Error Message" in captured.err

def test_invalid_background_color():
    """Test that invalid background color raises ValueError"""
    with pytest.raises(ValueError, match="Invalid background color"):
        ColorLogger.log("Test Message", bg_color='invalid_color')

def test_invalid_text_color():
    """Test that invalid text color raises ValueError"""
    with pytest.raises(ValueError, match="Invalid text color"):
        ColorLogger.log("Test Message", text_color='invalid_color')