import sys
import logging

def error_messaage_detail(error, error_detail: sys):
    """
    This function takes an error and its details and returns a string with the error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in file: {file_name} at line: {line_number} - {str(error)}"
    return error_message

class CustomException(Exception):
    """
    Custom exception class that logs the error message and raises the exception.
    """
    def __init__(self, error_message: str, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_messaage_detail(error_message, error_detail)
    
    def __str__(self):
        return self.error_message