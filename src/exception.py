import sys
# sys module provides various function and variables that are used to manipulate different parts of the Python runtime envirnoment
from src.logger import logging 

# The function is having the 2 parameters which is the error itself and the error_detail which will be present inside the sys
def error_message_details(error,error_detail:sys):
    _ , _ , exc_tb = error_detail.exc_info()
    # It give (type , value , traceback) in return
    # the exc_info() will give three values in which first 2 are not useful to use
    # this var exc_tb will give that in which file the error has occured, in which line the error has occured and all this information will be stored inside this variable
    
    file_name = exc_tb.tb_frame.f_code.co_filename                    # This is the name of file in which the error has occured , All this code we can find from the exception handling documentation
    
    error_message = "Error occured in Python Script name [{0} line number [{1}] error message [{2}]".format(file_name , exc_tb.tb_lineno , str(error))
    return error_message


# You used a class because:
# You wanted to extend built-in Exception
# You wanted custom behavior
# You wanted reusable structured error handling
# That cannot be done cleanly without a class.
# Creating an Class which is inherited from the Exception Class which is inbuilt in Python
class CustomException(Exception):
    def __init__(self , error_message , error_detail:sys):
        super().__init__(error_message)                                # The Super method is used to inherit the Exception Class over here
        self.error_message = error_message_details(error_message , error_detail = error_detail)
    
    # Without this function the python doesn't know what to print , if we not write this it will print the location of the error message in the device , but with this function written it knows what to print
    def __str__(self):
        return self.error_message
    # when we will print from the this custom_exception class the error_message will get printed
    
    
    
    # This is only for the one time , because it will be common for the rest of the projects
    
    
    


# For testing the Exception
# if __name__ == '__main__':
        
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.error("Unexpected Error Occured",exc_info = True)
#         raise CustomException(e,sys)