# first import the sys library

import sys
import logging
from src.logger import logging
# creating my own error_message_detail that except two parametes 1. error 2. error_detail:sys in the sys.

def error_message_detail(error, error_detail:sys) :
    # so the exc_info will give you the three detail of the message so i'll need only third one so i'll write code like that
    
    _, _, exc_tb = error_detail.exc_info()
    
    # after receiving what is error, where occure, what is the line number i'll write the error_message code
    
    # First getting the File Name
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # Now getting the Line Number
    line_number = exc_tb.tb_lineno
    
    # Now geeting the Error Message.
    err_mess = str(error)
    
    error_message = "Error Occurs in Python Script name : [{0}], Line Number : [{1}], Error Message : [{2}]".format(
        
        file_name, line_number, err_mess
        
    )
    
    return error_message
    
# Now my erros raised i'll call my error_message_detail function. so creating a class CustomeException

# When ever i raise my customException first it will Inherits the Parent Exception what ever error message come into the error_message_detail and it wil be intialized into the self.error_message.
class CustomException(Exception) :
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    # if i want to print any error message
    def __str__(self):
        return self.error_message
    