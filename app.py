#!flask/bin/python3

from flask import Flask

app = Flask(__name__)

from apis.todo import *
from apis.auth import *
    
if __name__ == "__main__":
    app.run(debug=True, port=8001)
