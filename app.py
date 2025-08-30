import os
from flask import Flask, jsonify, request
import google.generativeai as genai

app = Flask(__name__)

# Read API key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set!")

# Configure Gemini API
genai.configure(api_key=API_KEY)

@app.route("/generate", methods=["GET", "POST"])
def generate():
    # Example prompt from query param or POST JSON
    prompt = request.args.get("prompt") or request.json.get("prompt") if request.is_json else "Hello, World!"

    try:
        # Call Gemini API
        response = genai.generate_text(model="gemini-text-1.5", prompt=prompt)
        text_output = response.result if hasattr(response, "result") else str(response)
    except Exception as e:
        return jsonify({
            "message": "Error calling Gemini API",
            "error": str(e),
            "api_key_used": bool(API_KEY)
        }), 500

    return jsonify({
        "message": "Flask generate endpoint working!",
        "prompt": prompt,
        "api_key_used": bool(API_KEY),
        "gemini_output": text_output
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
