import io
import sys
import pytest
from src.color_logger import ColorLogger

class MockStdout:
    def __init__(self):
        self.captured = []
    
    def write(self, message):
        self.captured.append(message)
    
    def flush(self):
        pass

def test_log_default_color():
    """Test default logging with white background"""
    mock_stdout = MockStdout()
    sys.stdout = mock_stdout
    
    ColorLogger.log("Test Message")
    sys.stdout = sys.__stdout__
    
    assert any("\x1b[47m" in msg for msg in mock_stdout.captured)
    assert any("Test Message" in msg for msg in mock_stdout.captured)
    assert any("\x1b[0m" in msg for msg in mock_stdout.captured)

def test_log_custom_background():
    """Test logging with custom background color"""
    mock_stdout = MockStdout()
    sys.stdout = mock_stdout
    
    ColorLogger.log("Test Message", bg_color='blue')
    sys.stdout = sys.__stdout__
    
    assert any("\x1b[44m" in msg for msg in mock_stdout.captured)
    assert any("Test Message" in msg for msg in mock_stdout.captured)
    assert any("\x1b[0m" in msg for msg in mock_stdout.captured)

def test_log_with_text_color():
    """Test logging with text color"""
    mock_stdout = MockStdout()
    sys.stdout = mock_stdout
    
    ColorLogger.log("Test Message", bg_color='green', text_color='red')
    sys.stdout = sys.__stdout__
    
    assert any("\x1b[42m" in msg for msg in mock_stdout.captured)
    assert any("\x1b[31m" in msg for msg in mock_stdout.captured)
    assert any("Test Message" in msg for msg in mock_stdout.captured)
    assert any("\x1b[0m" in msg for msg in mock_stdout.captured)

def test_debug_method():
    """Test debug method with default color"""
    mock_stdout = MockStdout()
    sys.stdout = mock_stdout
    
    ColorLogger.debug("Debug Message")
    sys.stdout = sys.__stdout__
    
    assert any("\x1b[46m" in msg for msg in mock_stdout.captured)
    assert any("Debug Message" in msg for msg in mock_stdout.captured)

def test_error_method():
    """Test error method with stderr"""
    mock_stderr = MockStdout()
    sys.stderr = mock_stderr
    
    ColorLogger.error("Error Message")
    sys.stderr = sys.__stderr__
    
    assert any("\x1b[41m" in msg for msg in mock_stderr.captured)
    assert any("Error Message" in msg for msg in mock_stderr.captured)

def test_invalid_background_color():
    """Test that invalid background color raises ValueError"""
    with pytest.raises(ValueError, match="Invalid background color"):
        ColorLogger.log("Test Message", bg_color='invalid_color')

def test_invalid_text_color():
    """Test that invalid text color raises ValueError"""
    with pytest.raises(ValueError, match="Invalid text color"):
        ColorLogger.log("Test Message", text_color='invalid_color')