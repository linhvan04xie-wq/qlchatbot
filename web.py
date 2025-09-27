from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    user_message = request.json.get("message", "")
    # gọi gateway (port 5000)
    res = requests.post("http://localhost:5000/chat",
                        json={"userId": 1, "message": user_message})
    return jsonify(res.json())

if __name__ == "__main__":
    app.run(port=5005, debug=True)
