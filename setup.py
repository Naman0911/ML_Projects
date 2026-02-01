from setuptools import find_packages,setup
# the find_packages is the module that will automatically find out all the packages that are available in the directory which we have given
from typing import List

HYPEN_E_DOT = '-e .'

# It shows that the function get_requirements will take the path as a string and it will return an list which will also be string because this requirements.txt will be containing the list of libraries
def get_requirements(path: str) -> List[str]:
    requirements = []
    
    with open(path) as file_obj:
        requirements = file_obj.readlines()                                # When we do the readlines function it will read the content line by line but when the line is changed to the next line the \n is also gets added which we don't want 
        requirements = [req.strip()for req in requirements]       # This will all the values from the requirements and then it will replace the \n with the blank space
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements
            
# Now we can directly install the setup.py or when we are trying to install requirements.txt at that point of time this setup.py should also run to build the packages and for enabling that we will write this in teh requirments.txt
        
setup(
    name = 'ML_Project',
    version = '0.0.1',
    author = 'Naman Vijay Upadhyay',
    author_email = 'naman.unpadhyay@mitwpu.edu.in',
    packages = find_packages(),
    install_requires=get_requirements('requirements.txt')
    # install_requires = ['pandas','numpy','matplotlib','seaborn']
    # Now there can be a projects in which we requires 100 numbers of libraries and then it is not feasible to write them one by one so we will create an function to get the requirments which are needed
)
# When we are creating the setup function we need to give the name of projects and all
# It is basically a function which have all the meta details of the project

# ---- find_packages() ----
# . Now how the find_packages will find the package
# . First of all we need to create an src named folder
# . Then inside that folder we will create an file named __init__.py
# . Now whenever the find_packages will be running this will go and check in how many folder this __init__.py file is there and then the folder which have this file will be directly src (source) folder as package it self
# . And It will try to build it , and once the build is done we can import this anywhere , wherever we want , Just like how we import seaborn , pandas 

# Now the entire project development will be done inside this src folder and when any new folder we will make we'll also use there the __init__.py file , so that the internal folder also behave likes an package



# use pip install -e . --> For Building it as an package




# --------------- Src (Source) Folder ---------------- 

# Components folder
# 1. Firstly we will create an components folder and inside it we will create an __.init__.py for exporting it as package later on
#    . Components are all the modules which we are going to create such as data ingestion and etc.
# 2. We will start with the data_ingestion.py file which will be having the code for reading the data.
#    . Now after reading the data we will go for the validation and for the transformation of the data.
# 3. data_tranformation.py, It is the file which will be having the code for transforming the data , like catgeorical features into numerical features , ohe etc.
# 4. model_train.py ,It is the file which will be having the code for training the model and also for the evaluation of the model.


#  Pipeline folder
#    . Basically there will be 2 pipelines in our project (1) training pipeline and (2) Predicting Pipeline
# 1. train_pipeline.py , It will be having all the code for the training process and from this file we'll try to trigger the components folder's files
# 2. predict_pipeline.py , It will be having the code for the prediction of the test data or new data


# logger.py file
#    . This is the file which we keep the track of logging.


# exception.py 
#     . This is the file which we use to do exception handling


# utlis.py 
#     . This is the file in which any functiionailty which we are writing in a common way will be stored .
#     . for ecxampke reading the code from the dastabse we need a mongo client, whose code will be written here.
#     . Similarly the code for pushing the file to the code will be done here