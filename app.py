from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Home route (to check server)
@app.route('/')
def home():
    return "ESP32 Render Server Running ✅"

# 🔥 Test route (ESP32 will send data here)
@app.route('/test', methods=['POST'])
def test():
    data = request.get_json()

    print("📥 Data received from ESP32:")
    print(data)

    return jsonify({
        "status": "success",
        "message": "Data received successfully on Render",
        "received_data": data
    })

# Run server (IMPORTANT for Render)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
