import sys
import logging

def error_message_detail(error):
    exc_type, exc_value, exc_tb = sys.exc_info()
    
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        error = str(error)
    else:
        file_name = "<unknown file>"
        line_number = "<unknown line>"
    
    error_message = (
        f"Error occurred in python script [{file_name}] "
        f"line number [{line_number}] "
        f"error message [{error}]"
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message)

    
    def __str__(self):
        return self.error_message
    
