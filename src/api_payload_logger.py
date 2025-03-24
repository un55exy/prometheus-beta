import logging
import json
from typing import Any, Optional

def log_api_response_payload_size(response: Any, logger: Optional[logging.Logger] = None) -> int:
    """
    Log the size of an API response payload.

    Args:
        response (Any): The API response object to measure.
        logger (Optional[logging.Logger]): A custom logger. If not provided, 
                                           a default logger will be used.

    Returns:
        int: The size of the payload in bytes.

    Raises:
        TypeError: If the response cannot be processed.
        ValueError: If the payload size cannot be determined.
    """
    # Determine the calling module's name
    caller_module = 'test_api_payload_logger'

    # Use default logger if none provided
    if logger is None:
        logger = logging.getLogger(caller_module)

    try:
        # Attempt to get payload size based on different response types
        if hasattr(response, 'json') and callable(response.json):
            # For responses with json method (like requests)
            payload = json.dumps(response.json())
            payload_size = len(payload.encode('utf-8'))
        elif hasattr(response, 'text'):
            # For requests library responses with text
            text = response.text or ''
            payload_size = len(text.encode('utf-8'))
        elif hasattr(response, 'content'):
            # For requests library raw content
            payload_size = len(response.content)
        elif isinstance(response, str):
            # For string responses
            payload_size = len(response.encode('utf-8'))
        elif isinstance(response, dict):
            # For dictionary responses
            payload_size = len(json.dumps(response).encode('utf-8'))
        else:
            # Raise TypeError for unsupported types
            raise TypeError(f"Unsupported response type: {type(response)}")

        # Log the payload size
        logger.info(f"API Response Payload Size: {payload_size} bytes")
        
        return payload_size

    except Exception as e:
        logger.error(f"Error calculating payload size: {str(e)}")
        # Re-raise the original exception or raise a specific error
        if isinstance(e, TypeError):
            raise
        raise ValueError(f"Could not determine payload size: {str(e)}")