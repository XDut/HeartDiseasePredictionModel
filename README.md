# Introduction

This git repo contains the implementation of my ML project on Heart Disease Prediction. This is a real-world machine learning model/project that predicts whether a patient can be diagnosed with heart disease or not.

# Procedure

Performed data wrangling, filtering, and tested six different ML algorithms to find which one offers the optimal results for our dataset.

Since Random Forest gave the best results, the accompanying flask app only contains that specific model.

# Components

The main components of the project include the following:

1. Objective of the Project
2. Features
3. Data Wrangling
4. Conducting EDA
5. Using Machine Learning Algorithms
6. Finding Feature Score
7. Conclusion

# Usage

Run the flask server and send a POST request to / to use the ML model API.

For Bash, the POST request should be a JSON object with the following schema :

\> curl -X POST https://heart-disease-prediction-l9fj.onrender.com/ -H "Content-Type: application/json" -d  @- <<EOF

\> {  ..... }  

\> EOF

Example 1:

{
    "age": 63,
    "sex": 1,
    "cp": 3,
    "trestbps": 145,
    "chol": 233,
    "fbs": 1,
    "restecg": 0,
    "thalach": 150,
    "exang": 0,
    "oldpeak": "2.3",
    "slope": 0,
    "ca": 0,
    "thal": 1
  }

OUTPUT : True

Example 2 : 

{
    "age": 43,
    "sex": 0,
    "cp": 0,
    "trestbps": 132,
    "chol": 341,
    "fbs": 1,
    "restecg": 0,
    "thalach": 136,
    "exang": 1,
    "oldpeak": "3",
    "slope": 1,
    "ca": 0,
    "thal": 3
}

OUTPUT : False
