# Here we are going to train differnet models and then evaluate the perfromance matrixs and then select the best model for the certain data

import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import AdaBoostRegressor , GradientBoostingRegressor , RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score

from src.exception import CustomException
from src.logger import logging
from src.utlis import save_object , evaluate_models


# For every component the first thing is we need to create a config file 

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl")
    
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()                       # Inside this particular variable we will get the path of the Model fil 

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Splitting training and testing data")
            
            X_train ,Y_train , X_test , Y_test = train_array[:,:-1],train_array[:,-1],test_array[:,:-1],test_array[:,-1]                               # In the Train_arr the last column was added which was of target so now we are spltting them into x_train , Y_train , X_test , Y_test
            
            models = {
                "Linear Regression" : LinearRegression(),
                "Knn Regressor" : KNeighborsRegressor(),
                "Decision Tree Regressor" : DecisionTreeRegressor(),
                "Random Forest Regressor" : RandomForestRegressor(),
                "Adaboost Regressor" : AdaBoostRegressor(),
                "Gradient Boost Regressor" : GradientBoostingRegressor(),
                "Catboost Regressor" : CatBoostRegressor(),
                "Xgboost" : XGBRegressor()
            }
            
            model_report:dict= evaluate_models(X_train = X_train , Y_train = Y_train , X_test= X_test , Y_test=Y_test ,models = models)
            
            # To get the best model score from the dictionary
            best_model_score = max(sorted(model_report.values()))
            
            # To get best model name from dictionary
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]
            
            # If there is not an single model which has accuracy more than 0.6 then there is no best model found 
            if(best_model_score < 0.6):
                raise CustomException("No best Model Found")
            logging.info(f"Best found Model on both training and testing dataset")
            
            save_object(file_path=self.model_trainer_config.trained_model_file_path , obj = best_model)
            
            predicted = best_model.predict(X_test)
            
            r2_square = r2_score(Y_test , predicted)
            return r2_square
        
        
        except Exception as e:
            raise CustomException(e,sys)