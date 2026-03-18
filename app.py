from flask import Flask, request, jsonify

app = Flask(__name__)

# 🔹 Store latest data globally
latest_data = {}

# 🔹 Home page (Website UI)
@app.route('/')
def home():
    return f"""
    <h2>ESP32 Render Server Running ✅</h2>
    <h3>Latest Sensor Data:</h3>
    <p><b>Voltage:</b> {latest_data.get('voltage', 'No data')}</p>
    <p><b>Current:</b> {latest_data.get('current', 'No data')}</p>
    <p><b>Temperature:</b> {latest_data.get('temperature', 'No data')}</p>
    """

# 🔹 API endpoint (ESP32 sends data here)
@app.route('/test', methods=['POST'])
def test():
    global latest_data

    data = request.get_json()
    latest_data = data  # store data

    print("📥 Data received:", data)

    return jsonify({
        "status": "success",
        "message": "Data received successfully",
        "received_data": data
    })

# 🔹 Run app
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
