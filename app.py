import os
import pickle
from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# Correct model path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "diabetes_model.pkl")

# Load model
model = pickle.load(open(model_path, 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    # Get values from form
    pregnancies = float(request.form['pregnancies'])
    glucose = float(request.form['glucose'])
    blood_pressure = float(request.form['blood_pressure'])
    skin_thickness = float(request.form['skin_thickness'])
    insulin = float(request.form['insulin'])
    bmi = float(request.form['bmi'])
    diabetes_pedigree = float(request.form['diabetes_pedigree'])
    age = float(request.form['age'])

    # Arrange features in correct order
    features = np.array([[
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        diabetes_pedigree,
        age
    ]])

    # Prediction
    prediction = model.predict(features)

    # Result
    if prediction[0] == 1:
        result = "The person is Diabetic"
    else:
        result = "The person is Not Diabetic"

    return render_template('index.html', prediction_text=result)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=False)