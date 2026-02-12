# Suppose we are working in a big company and as a data scientist the first thing which we need is the data itself.
# The Data will be stored into a databse or in mongodb or in Hadoop etc, and mostly we will be having a seprate big data anaylsis team which will work on it an provide us the data
# Like the team will be reading the data from the live stream and , many more things and then they will give us the data.

# Now we as a Data Scientist have to read the particular dataset from the data sources
# The Data sources can be many kinds of , so initially we will start from the Local Data Soucre and next on we will try it from the mongodb 

import os
import sys
from src.exception import CustomException                                # For the custom exception handling
from src.logger import logging                                           # For the Logging 
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass                                        # This is basically used to create an class variables

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_train import ModelTrainerConfig
from src.components.model_train import ModelTrainer

# When we are performing the data ingestion component , there should be some inputs that may be probably required by this data ingestion components
# The input can be like where i have to save my training path or the train data or test data or the raw data , so this kind of inputs will basically be creating in another class and this class we will mention as Data Ingestion class
# This class is created for any input which is required for the data ingestion will give through this particular data ingestion config
# Similary if we do data transformation we will go on and write the data transformation config cause here also we will be requiring some kind of inputs 

# Self parameter explaination
# s1.display()
# Student.display(s1) 

# self → receives s1
# self.name → means s1.name
# self.marks → means s1.marks

# Inside the class if we want to define a class variables we basically use __init__
# But if we use the decorator dataclass we can directly define our class variable
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts','train.csv')                                # The data ingestion component's output will be save the file in this path example the training data path  
    test_data_path: str = os.path.join('artifacts','test.csv')
    raw_data_path: str = os.path.join('artifacts','data.csv')
    # All this are the inputs which we are giving to the data ingestion config and now the data ingestion knows where to save the train path test part and data path
    
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        # As soon as Data Ingestion is called all the three part will get saved inside this particular class variable
        
        
    def initiate_data_ingestion(self):
        # This function will be used if the data is stored at some database to read the data from there we will write the code here
        # For example if we have to read the data from the mongodb client in the utlis.py
        logging.info("Entered the data ingestion method or component")
        try:
            
            # Now we only need to change the code of reading the data from api or from the mongodb or from somewhere else
            df = pd.read_csv(r'C:\Users\Admin\Desktop\Data Science\MLOPS\notebook\data\stud.csv')
            logging.info('Data is readed as the Dataframe')
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            # We have combine the directory path name so we will write 1 more brakcet and if it already exists then append in it 
            
            df.to_csv(self.ingestion_config.raw_data_path,index = False , header = True)
            
            logging.info("Train test Split Initiated")
            train_set , test_set = train_test_split(df,test_size=0.2,random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index = False , header = True)
            test_set.to_csv(self.ingestion_config.test_data_path,index = False , header = True)
            
            logging.info("Ingestion of the Data Completed")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            # This information is passed so that the next step which is the data transformation can just grab the data from here and start the process
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == '__main__':
    obj = DataIngestion()
    train_data , test_data = obj.initiate_data_ingestion()                               # Because when we are creating an instance we are getting 2 values in return
        
# Firstly we have read the data from suppose differnet sources we can say from clipboard or from APIs or anywhere
# Then we converted the raw data file into a CSV file 
# Then we did the train test split
# Then we are returing the training and test data path


# Donot run it while going inside the current working diretory means to the folder components then to the data_ingestion.py file it will create the folders inside the components folder because the cwd is that
# But we want it to form under the root folder so we will do it like python\src\components\data_ingestion.py and the execute it
    
    
    # Combined the data transformation
    data_transformation = DataTransformation()
    train_arr , test_arr , _= data_transformation.initiate_data_transformation(train_data , test_data)
    
    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr , test_arr))