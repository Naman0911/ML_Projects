from flask import Flask , request , render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData , PredictPipeline


application = Flask(__name__)                                  # This will give us the entry point where we need to execute it
app = application


# Route for the Home  PAge
@app.route('/')
def index():
    return render_template('index.html')                       # When we use the render_template module it goes in the directory and finds the template folder and execute the file which is given as parameter




@app.route('/predictdata',methods = ['GET','POST'])            # This route will work in both GET and POST method 
def predict_datapoint():                                       # This function will be responsible for getting the data and doing the predictions
    if request.method == 'GET':                                # If the request method is just GET then it will return the Home.html page which will be the basic page for inputs
        return render_template("home.html")
    
    else:
        try:
            data = CustomData(
                gender = request.form.get('gender'),
                race_ethnicity = request.form.get('race_ethnicity'),
                parental_level_of_education = request.form.get('parental_level_of_education'),
                lunch = request.form.get('lunch'),
                test_preparation_course = request.form.get('test_preparation_course'),
                reading_score = float(request.form.get('reading_score')),
                writing_score = float(request.form.get('writing_score')),
            )
        
            predict_df = data.get_data_as_data_frame()
            print(predict_df)
            
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(predict_df)
            
            return render_template("home.html",results = results[0])
        
        except Exception as e:
            return str(e)
        


if  __name__ == "__main__":
    app.run(host = "0.0.0.0")
    # While deploying we don't use debug = True