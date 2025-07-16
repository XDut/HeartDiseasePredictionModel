import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open("model.sav", "rb"))


@app.route("/", methods=["GET"])
def greet():
    return "Send a POST request to this endpoint to use the ML model API."


@app.route("/", methods=["POST"])
def predict():
    data = request.get_json(force=True)

    """
    Received data is of type:
    {
        "age": number,
        "sex": number,
        "cp": number,
        "trestbps": number,
        "chol": number,
        "fbs": number,
        "restecg": number,
        "thalach": number,
        "exang": number,
        "oldpeak": number,
        "slope": number,
        "ca": number,
        "thal": number
    }

    Now we need to convert this data into a format suitable for the model,
    that is a numpy array with numbers in the same order as the JSON keys
    """

    # Convert the JSON data to a numpy array
    data = np.array(
        [
            data["age"],
            data["sex"],
            data["cp"],
            data["trestbps"],
            data["chol"],
            data["fbs"],
            data["restecg"],
            data["thalach"],
            data["exang"],
            data["oldpeak"],
            data["slope"],
            data["ca"],
            data["thal"],
        ],
        dtype=float,
    )

    # Make prediction
    prediction = model.predict([data])
    output = prediction[0]

    return jsonify(True if output == 1 else False)
