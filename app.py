import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
# from tempfile import mkdtemp

# import time

from helpers import price

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///airports.db")




@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/flights")
# def flights():
#     # response = price(originCode, 'LGA')
#     # print(response)
#     arr = dict()
#     arr["age"] = 2
#     return arr

@app.route("/origin")
def origin():
    args = request.args
    response = dict()
    origin = args['origin']
    # print(f'origin is {origin}')
    if origin == '':
        response['name'] = 'Please Enter A City'
        return response
    origin_code = db.execute("SELECT name, code FROM airports WHERE name LIKE ?", f'%{origin}%')
    response['name'] = origin_code[0]['name']
    return response

@app.route("/destination")
def destination():
    args = request.args
    response = dict()
    destination = args['destination']
    if destination == '':
        response['name'] = 'Please Enter A City'
        return response
    destination_code = db.execute("SELECT name, code FROM airports WHERE name LIKE ?", f'%{destination}%')
    response['name'] = destination_code[0]['name']
    return response

@app.route("/flights")
def flights():
    args = request.args
    response = dict()
    return '0'




    # originName = origin[0]['name']
    # originCode = origin[0]['code']
    # destination = db.execute("SELECT name, code FROM airports WHERE name LIKE '%New York%'")
    # print(destination)