from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

@app.route("/response", methods=["POST"])
def response():
    data = request.get_json()
    user_id = data.get("userId")
    intent = data.get("intent")

    reply = "I don't understand."

    if intent == "greeting":
        reply = "Hello! How can I help you today?"
    elif intent == "get_weather":
        weather_res = requests.get("http://localhost:5003/today")
        reply = f"The weather today is {weather_res.json()['weather']}"
    elif intent == "thanks":
        reply = "You're welcome! Happy to help 😊"
    elif intent == "goodbye":
        reply = "Goodbye! Have a nice day 👋"
    elif intent == "ask_name":
        reply = "I'm ChatBot Demo, your virtual assistant 🤖"
    elif intent == "ask_time":
        now = datetime.now().strftime("%H:%M:%S")
        reply = f"The current time is {now}"
    elif intent == "ask_date":
        today = datetime.now().strftime("%Y-%m-%d")
        reply = f"Today's date is {today}"

    return jsonify({"userId": user_id, "reply": reply})

if __name__ == "__main__":
    app.run(port=5002)
