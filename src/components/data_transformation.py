# For Creating the classes and System Handling
import sys 
import os
from dataclasses import dataclass

# For Transforming the Features
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer

# For Imputations and Pipeline Operation
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

# Encoding and Scaling
from sklearn.preprocessing import OneHotEncoder,StandardScaler

# Exception Handling and Logging
from src.exception import CustomException
from src.logger import logging
from src.utlis import save_object

@dataclass
class DataTransformationConfig:                                                                        # It will be giving any inputs or the paths which are required for the Data transformation component
    preprocessor_ob_file_path: str = os.path.join('artifacts',"preprocessor.pkl")                           # It is the path of the model which are saving in a pickle file that is this File path.
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()                                   # This is varibale which is being the object of the DataTransformationConfig
        
        
    def get_data_transformer_object(self):                                                             # This function is responsible for the data transformation for the differnet types of columns using Different types of transfromers
        try:
           numerical_features = ['writing_score','reading_score']
           categorical_features = ["gender","race_ethnicity","parental_level_of_education","lunch","test_preparation_course"] 
           
           num_pipeline = Pipeline(steps = [('imputer',SimpleImputer(strategy='median')),
                                            ('scaler',StandardScaler(with_mean=False))])
           
           cat_pipeline = Pipeline(steps=[('imputer',SimpleImputer(strategy='most_frequent')) , 
                                          ('OHE',OneHotEncoder(handle_unknown='ignore'))])
           
           logging.info(f"Categorical Features: {categorical_features}")
           logging.info(f"Numerical Features: {numerical_features}")
           
           preprocessor = ColumnTransformer([('Numerical_pipeline',num_pipeline,numerical_features) , 
                                             ('Categorical_Pipeline',cat_pipeline,categorical_features)])
           
           return preprocessor
       
       
        except Exception as e:
            raise CustomException(e,sys)
        
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            # Reading the data from the path recieved from the data ingestion
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Reading of train and test data is complelted")
            
            
            # Creating the Preprocessor Object
            logging.info("Obtaining preprocessor object")
            preprocessing_obj = self.get_data_transformer_object()
            
            
            # Defining the columns
            target_column_name = "math_score"
            numerical_columns = ["writing_score","reading_score"]
            
            # X_train , X_test , Y_train , Y_test
            input_features_train_df = train_df.drop(columns=[target_column_name])
            target_features_train_df = train_df[target_column_name]
            
            input_features_test_df = test_df.drop(columns=[target_column_name])
            target_features_test_df = test_df[target_column_name]
            
            # Transformed Train and Test Data Using Preprocessor
            logging.info("Applying the preprocessing object on training dataframe and testing dataframe ")
            input_feature_train_arr = preprocessing_obj.fit_transform(input_features_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_features_test_df)
            
            # np.c_ is a NumPy convenience indexer used to concatenate arrays column-wise (i.e., along the second axis, axis=1).
            train_arr = np.c_[input_feature_train_arr , np.array(target_features_train_df)]
            test_arr = np.c_[input_feature_test_arr , np.array(target_features_test_df)]
            # Here basically we are taking the transformed Train ,Test data and array version of the target data for the both and we are combining them
            
            logging.info(f"Saved Preprocessing Objects")
            
            # Used for saving the pickle file
            save_object(file_path = self.data_transformation_config.preprocessor_ob_file_path , obj = preprocessing_obj)
            
            # Return the Final train and test data with the pickle file of the preprocessor object
            return (train_arr , test_arr , self.data_transformation_config.preprocessor_ob_file_path)
            
        except Exception as e:
            raise CustomException(e,sys)