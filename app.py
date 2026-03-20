from flask import Flask, request, jsonify
import os

app = Flask(__name__)

latest_data = {}

@app.route('/')
def home():
    if not latest_data:
        return "<h2>No data received yet</h2>"

    return f"""
    <h2>SMART EV BMS CLOUD DASHBOARD 🚀</h2>

    <p><b>Voltage:</b> {latest_data['voltage']} V</p>
    <p><b>Current:</b> {latest_data['current']} A</p>
    <p><b>Temperature:</b> {latest_data['temperature']} °C</p>
    <p><b>Status:</b> {latest_data['status']}</p>
    """

@app.route('/test', methods=['POST'])
def test():
    global latest_data

    data = request.get_json()
    latest_data = data

    print("📥 Data received:")
    print(data)

    return jsonify({
        "status": "success",
        "data": data
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
