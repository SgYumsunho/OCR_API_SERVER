from urllib import request
from flask import Flask, request
#from flask_restx import Resource, Api
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "test"

@app.route("/two")
def hello_world2():
    return "test2"

@app.route("/three")
def hello_world3():
    return "test3"