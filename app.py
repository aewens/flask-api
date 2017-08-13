#!flask/bin/python3

from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": u"Flask API",
        "description": u"Make an API out of Flask using JSON",
        "done": False
    },
    {
        "id": 2,
        "title": u"Database",
        "description": u"Add database to API to make it useful",
        "done": False
    }
]

@app.route("/api/v1.0/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": tasks})
    
if __name__ == "__main__":
    app.run(debug=True, port=8001)
