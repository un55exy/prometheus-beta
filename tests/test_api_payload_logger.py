import pytest
import logging
import json
from unittest.mock import Mock, patch
from src.api_payload_logger import log_api_response_payload_size

class MockResponse:
    def __init__(self, text=None, content=None, json_data=None):
        self._text = text
        self._content = content
        self._json_data = json_data

    @property
    def text(self):
        return self._text

    @property
    def content(self):
        return self._content

    def json(self):
        return self._json_data

def test_log_api_response_payload_size_string():
    # Test with string response
    mock_logger = Mock(spec=logging.Logger)
    result = log_api_response_payload_size("Hello, World!", logger=mock_logger)
    
    assert result == len("Hello, World!".encode('utf-8'))
    mock_logger.info.assert_called_once()

def test_log_api_response_payload_size_dict():
    # Test with dictionary response
    test_dict = {"key": "value", "number": 42}
    mock_logger = Mock(spec=logging.Logger)
    
    result = log_api_response_payload_size(test_dict, logger=mock_logger)
    
    assert result == len(json.dumps(test_dict).encode('utf-8'))
    mock_logger.info.assert_called_once()

def test_log_api_response_payload_size_requests_response():
    # Test with requests-like response
    test_text = "API Response Content"
    mock_response = MockResponse(text=test_text)
    mock_logger = Mock(spec=logging.Logger)
    
    result = log_api_response_payload_size(mock_response, logger=mock_logger)
    
    assert result == len(test_text.encode('utf-8'))
    mock_logger.info.assert_called_once()

def test_log_api_response_payload_size_requests_json_response():
    # Test with requests response with json method
    test_json = {"data": "example"}
    mock_response = MockResponse(json_data=test_json)
    mock_logger = Mock(spec=logging.Logger)
    
    result = log_api_response_payload_size(mock_response, logger=mock_logger)
    
    assert result == len(json.dumps(test_json).encode('utf-8'))
    mock_logger.info.assert_called_once()

def test_log_api_response_payload_size_unsupported_type():
    # Test with unsupported response type
    mock_logger = Mock(spec=logging.Logger)
    
    with pytest.raises(TypeError):
        log_api_response_payload_size(42, logger=mock_logger)

def test_log_api_response_payload_size_default_logger():
    # Test with default logger
    with patch('logging.getLogger') as mock_get_logger:
        mock_logger = Mock(spec=logging.Logger)
        mock_get_logger.return_value = mock_logger
        
        log_api_response_payload_size("Test")
        
        mock_get_logger.assert_called_once_with(__name__)
        mock_logger.info.assert_called_once()