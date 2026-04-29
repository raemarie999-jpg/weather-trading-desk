from flask import Flask, jsonify, render_template
import json
import os

app = Flask(__name__)

@app.route("/")
def home():

    if os.path.exists("signals.json"):
        with open("signals.json") as f:
            data = json.load(f)
    else:
        data = {"message": "No signals yet"}

    return render_template("index.html", data=data)

@app.route("/api")
def api():

    if os.path.exists("signals.json"):
        with open("signals.json") as f:
            return jsonify(json.load(f))

    return jsonify({"message": "No data"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
