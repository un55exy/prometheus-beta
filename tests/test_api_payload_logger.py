import pytest
import logging
import json
from unittest.mock import Mock, patch
from src.api_payload_logger import log_api_response_payload_size

def test_log_api_response_payload_size_string():
    # Test with string response
    mock_logger = Mock(spec=logging.Logger)
    test_str = "Hello, World!"
    result = log_api_response_payload_size(test_str, logger=mock_logger)
    
    expected_size = len(test_str.encode('utf-8'))
    assert result == expected_size
    mock_logger.info.assert_called_once_with(f"API Response Payload Size: {expected_size} bytes")

def test_log_api_response_payload_size_dict():
    # Test with dictionary response
    test_dict = {"key": "value", "number": 42}
    mock_logger = Mock(spec=logging.Logger)
    
    result = log_api_response_payload_size(test_dict, logger=mock_logger)
    
    expected_size = len(json.dumps(test_dict).encode('utf-8'))
    assert result == expected_size
    mock_logger.info.assert_called_once_with(f"API Response Payload Size: {expected_size} bytes")

def test_log_api_response_payload_size_requests_response():
    # Test with requests-like response
    test_text = "API Response Content"
    class MockResponse:
        def __init__(self):
            self.text = test_text
            self.json = lambda: None
    
    mock_response = MockResponse()
    mock_logger = Mock(spec=logging.Logger)
    
    result = log_api_response_payload_size(mock_response, logger=mock_logger)
    
    expected_size = len(test_text.encode('utf-8'))
    assert result == expected_size
    mock_logger.info.assert_called_once_with(f"API Response Payload Size: {expected_size} bytes")

def test_log_api_response_payload_size_requests_json_response():
    # Test with requests response with json method
    test_json = {"data": "example"}
    class MockResponse:
        def __init__(self):
            self.text = None
            self.json = lambda: test_json
    
    mock_response = MockResponse()
    mock_logger = Mock(spec=logging.Logger)
    
    result = log_api_response_payload_size(mock_response, logger=mock_logger)
    
    expected_size = len(json.dumps(test_json).encode('utf-8'))
    assert result == expected_size
    mock_logger.info.assert_called_once_with(f"API Response Payload Size: {expected_size} bytes")

def test_log_api_response_payload_size_unsupported_type():
    # Test with unsupported response type
    mock_logger = Mock(spec=logging.Logger)
    
    with pytest.raises(TypeError, match="Unsupported response type: <class 'int'>"):
        log_api_response_payload_size(42, logger=mock_logger)

def test_log_api_response_payload_size_default_logger():
    # Test with default logger
    with patch('logging.getLogger') as mock_get_logger:
        mock_logger = Mock(spec=logging.Logger)
        mock_get_logger.return_value = mock_logger
        
        log_api_response_payload_size("Test")
        
        mock_get_logger.assert_called_once_with('test_api_payload_logger')