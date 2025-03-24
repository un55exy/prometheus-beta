import sys

class ColorLogger:
    """
    A logger class that supports colored background output to console.
    
    Supports different background colors and various logging methods.
    Uses ANSI escape codes for terminal color formatting.
    """
    
    # ANSI background color codes
    BG_COLORS = {
        'red': '\033[41m',
        'green': '\033[42m',
        'yellow': '\033[43m',
        'blue': '\033[44m',
        'magenta': '\033[45m',
        'cyan': '\033[46m',
        'white': '\033[47m',
        'reset': '\033[0m'
    }
    
    @classmethod
    def log(cls, message, bg_color='white', text_color=None, file=sys.stdout):
        """
        Log a message with specified background color.
        
        Args:
            message (str): The message to log
            bg_color (str, optional): Background color. Defaults to 'white'.
            text_color (str, optional): Text color. Defaults to None.
            file (file, optional): Output stream. Defaults to sys.stdout.
        
        Raises:
            ValueError: If an invalid background color is specified
        """
        # Validate background color
        if bg_color not in cls.BG_COLORS:
            raise ValueError(f"Invalid background color. Choose from {list(cls.BG_COLORS.keys())}")
        
        # Construct color formatting
        bg_code = cls.BG_COLORS.get(bg_color, '')
        reset_code = cls.BG_COLORS['reset']
        
        # Optional text color formatting (basic implementation)
        text_prefix = ''
        if text_color:
            text_color_codes = {
                'red': '\033[31m',
                'green': '\033[32m',
                'yellow': '\033[33m',
                'blue': '\033[34m',
                'magenta': '\033[35m',
                'cyan': '\033[36m',
                'white': '\033[37m'
            }
            if text_color not in text_color_codes:
                raise ValueError(f"Invalid text color. Choose from {list(text_color_codes.keys())}")
            text_prefix = text_color_codes[text_color]
        
        # Combine formatting and message
        formatted_message = f"{bg_code}{text_prefix}{message}{reset_code}"
        
        # Print to specified file/stream
        print(formatted_message, file=file)
    
    @classmethod
    def debug(cls, message, bg_color='cyan'):
        """
        Log a debug message with optional background color.
        
        Args:
            message (str): Debug message
            bg_color (str, optional): Background color. Defaults to 'cyan'.
        """
        cls.log(message, bg_color=bg_color)
    
    @classmethod
    def error(cls, message, bg_color='red'):
        """
        Log an error message with optional background color.
        
        Args:
            message (str): Error message
            bg_color (str, optional): Background color. Defaults to 'red'.
        """
        cls.log(message, bg_color=bg_color, text_color='white', file=sys.stderr)