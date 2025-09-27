from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/today", methods=["GET"])
def today():
    return jsonify({"weather": "sunny with 30°C"})

if __name__ == "__main__":
    app.run(port=5003)
