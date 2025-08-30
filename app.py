import os
from flask import Flask, jsonify

app = Flask(__name__)

# Read API key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY", "not-set")

@app.route("/generate", methods=["GET", "POST"])
def generate():
    return jsonify({
        "message": "Flask generate endpoint working!",
        "prompt": "Hello, World!",
        "api_key": API_KEY
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
