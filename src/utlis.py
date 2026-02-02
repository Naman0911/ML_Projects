# This file will have all the common things that we are going to probably import or use 
# The Common functionailty which we will be used by all over the code

import os
import sys

import dill
# pip install -r requirement.txt

import numpy as np
import pandas as pd

from src.exception import CustomException


def save_object(file_path , obj):
    try:
        # This will take the directory path
        dir_path = os.path.dirname(file_path)
        
        # It will make directory if not there
        os.makedirs(dir_path , exist_ok=True)
        
        # It will open the file path as object and then dump the model at that path
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
            
    except Exception as e:
        raise CustomException(e,sys)