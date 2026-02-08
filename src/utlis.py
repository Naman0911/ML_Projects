# This file will have all the common things that we are going to probably import or use 
# The Common functionailty which we will be used by all over the code

import os
import sys

import dill
# pip install -r requirement.txt

import numpy as np
import pandas as pd

from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV , RandomizedSearchCV

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
    
    

def evaluate_models(X_train,Y_train,X_test,Y_test,models,param):
    try:
        report = {}
        
        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]
            
            gs = GridSearchCV(model,para,cv = 3)
            gs.fit(X_train , Y_train)
            
            model.set_params(**gs.best_params_)
            model.fit(X_train , Y_train)
            
            Y_train_pred = model.predict(X_train)
            
            Y_test_pred = model.predict(X_test)
            
            train_model_score = r2_score(Y_train , Y_train_pred)
            
            test_model_score = r2_score(Y_test , Y_test_pred)
            
            report[list(models.keys())[i]] = test_model_score
            
        return report
    
    except Exception as e:
        raise CustomException(e,sys)
            
            
            
def load_object(file_path):                                     # This is the function used for loading the Model and activating it.
    try:
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)
        
    except Exception as e:
        raise CustomException(e,sys)
            