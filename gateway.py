from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_id = data.get("userId")
    message = data.get("message")

    try:
        # gọi NLP service
        nlp_res = requests.post("http://localhost:5001/parse", json={"message": message})
        intent = nlp_res.json()["intent"]

        # gọi Chatbot Core
        bot_res = requests.post("http://localhost:5002/response", json={"userId": user_id, "intent": intent})
        return jsonify(bot_res.json())
    except Exception as e:
        return jsonify({"error": "Service error", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000)
