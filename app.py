from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Global data storage
latest_data = {
    "voltage": 0,
    "current": 0,
    "temperature": 0,
    "soc": 0,
    "prediction": "Waiting..."
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(latest_data)

@app.route('/predict', methods=['POST'])
def predict():
    global latest_data

    data = request.get_json()

    voltage = data['voltage']
    current = data['current']
    temperature = data['temperature']

    # Dummy SOC calculation
    soc = (voltage / 12.6) * 100  

    # Dummy logic for prediction (for testing UI)
    if temperature > 45:
        result = "Overheating 🔥"
    elif voltage < 10:
        result = "Low Voltage ⚠️"
    else:
        result = "Healthy ✅"

    latest_data = {
        "voltage": voltage,
        "current": current,
        "temperature": temperature,
        "soc": round(soc, 2),
        "prediction": result
    }

    return jsonify(latest_data)

if __name__ == '__main__':
    app.run(debug=True)
