from flask import Flask, jsonify, abort, make_response, request, url_for
import jwt
import datetime
from app import app

# TODO: Change in production, move to environment variable
app.config["SECRET_KEY"] = "supersecret"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)

@app.route("/auth", methods=["GET"])
def index():
    return jsonify({
        "message": "Welcome to the Auth API"
    })
    
@app.route("/auth/unsecure")
def unsecure():
    return jsonify({})
    
@app.route("/auth/secure")
def secure():
    return jsonify({})
    
@app.route("/auth/login")
def login():
    auth = request.authorization
    
    if auth and auth.password == "guest":
        expires = datetime.timedelta(minutes=60 * 24 * 7 * 2) # two weeks
        token = jwt.encode({
            "user": auth.username,
            "exp": datetime.datetime.utcnow() + expires
        }, app.config["SECRET_KEY"])
        return jsonify({"token": token.decode("utf-8")})
        
    return make_response(jsonify({"error": "Incorrect credentials"}), 401, {
        "WWW-Authenticate": "Basic realm=\"Login Required\""
    })
