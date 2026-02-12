# Here We will create an front end for the application from which tghe inputs will be given and then it will be tracked by the backend and then the backend woll connect this pickle files and all to give the prediction
# The Prediction Part is done here

import sys
import pandas as pd
import os

from src.exception import CustomException
from src.utlis import load_object


class PredictPipeline:
    # def __init__(self):
    #     pass                                                     # The default constructor
    
    
    # def predict(self,features):
    #     try:
    #         base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    #         model_path = r'C:\Users\Admin\Desktop\Data Science\MLOPS\Artifacts\model.pkl'                    # Getting the Preprocessor and the model using there path
    #         preprocessor_path = r'C:\Users\Admin\Desktop\Data Science\MLOPS\Artifacts\preprocessor.pkl'
            
    #         model = load_object(file_path = model_path)                                                     # This function will load the pickle file 
    #         preprocessor = load_object(file_path = preprocessor_path)
            
            
    #         data_scaled = preprocessor.transform(features)                                                  # Transforming the data.
    #         preds = model.predict(data_scaled)                                                              # For Predicting on the scaled data

    #         return preds
        
    #     except Exception as e:
    #         raise CustomException(e,sys)
    def __init__(self):
        try:
            # Dynamically get project root directory (works on AWS + local)
            base_dir = os.path.dirname(
                os.path.dirname(
                    os.path.dirname(os.path.abspath(__file__))
                )
            )

            # Construct proper paths
            model_path = os.path.join(base_dir, "artifacts", "model.pkl")
            preprocessor_path = os.path.join(base_dir, "artifacts", "preprocessor.pkl")

            # Load model and preprocessor
            self.model = load_object(model_path)
            self.preprocessor = load_object(preprocessor_path)

        except Exception as e:
            raise CustomException(e, sys)

    def predict(self, features):
        try:
            # Transform input data
            data_scaled = self.preprocessor.transform(features)

            # Predict
            preds = self.model.predict(data_scaled)

            return preds

        except Exception as e:
            raise CustomException(e, sys)
        
        
        
class CustomData:                                            # This class will be usefull for mapping all the inputs which are given in the front end to the back end
        
    def __init__(self , 
            gender: str, 
            race_ethnicity: str, 
            parental_level_of_education ,
            lunch: str,
            test_preparation_course: str,
            reading_score: int,
            writing_score: int):
#                                                               # All this values are coming from the Webpage and getting initialized in the function variable
            self.gender = gender 
            self.race_ethnicity = race_ethnicity
            self.parental_level_of_education = parental_level_of_education
            self.lunch = lunch
            self.test_preparation_course = test_preparation_course
            self.reading_score = reading_score
            self.writing_score = writing_score
        
        
    def get_data_as_data_frame(self):                      # This function is used to return the Dataframe because our model takes input in from of data frame
#                                                              # Creating Dictionary with the input values coming from the front end
            try:
                custom_data_input_dict = {
                    "gender":[self.gender],
                    "race_ethnicity":[self.race_ethnicity],
                    "parental_level_of_education":[self.parental_level_of_education],
                    "lunch":[self.lunch],
                    "test_preparation_course":[self.test_preparation_course],
                    "reading_score" : [self.reading_score],
                    "writing_score": [self.writing_score]
                }
                
                return pd.DataFrame(custom_data_input_dict)
            
            except Exception as e:
                raise CustomException(e,sys)
        
        
        