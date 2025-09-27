from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/parse", methods=["POST"])
def parse():
    data = request.get_json()
    message = data.get("message", "").lower()

    intent = "smalltalk"
    if "weather" in message:
        intent = "get_weather"
    elif "hello" in message or "hi" in message:
        intent = "greeting"
    elif "thank" in message:
        intent = "thanks"
    elif "bye" in message or "goodbye" in message:
        intent = "goodbye"
    elif "your name" in message or "who are you" in message:
        intent = "ask_name"
    elif "time" in message or "hour" in message or "giờ" in message:
        intent = "ask_time"
    elif "date" in message or "today" in message or "ngày" in message:
        intent = "ask_date"

    return jsonify({"intent": intent})

if __name__ == "__main__":
    app.run(port=5001)
