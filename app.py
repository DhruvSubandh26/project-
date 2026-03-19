import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Load ML model
model = pickle.load(open("model.pkl", "rb"))

# Store latest values
latest_data = {}
latest_prediction = None


# Home route (UI)
@app.route('/')
def home():
    return render_template("index.html", data=latest_data, prediction=latest_prediction)


# Existing test route (optional)
@app.route('/test', methods=['POST'])
def test():
    global latest_data
    latest_data = request.get_json()
    return jsonify({"status": "received"})


# ML Prediction API
@app.route('/predict', methods=['POST'])
def predict():
    global latest_prediction, latest_data

    try:
        data = request.get_json()

        # Extract values
        voltage = data['voltage']
        current = data['current']
        temperature = data['temperature']

        # Convert to model input
        features = np.array([[voltage, current, temperature]])

        # Predict
        pred = model.predict(features)[0]

        # Convert output to readable result
        if pred == 0:
            result = "Healthy Battery"
        else:
            result = "Fault Detected"

        # Store latest values
        latest_prediction = result
        latest_data = data

        return jsonify({
            "status": "success",
            "prediction": result
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })


# Run locally
if __name__ == "__main__":
    app.run(debug=True)
