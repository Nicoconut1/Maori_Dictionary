from flask import Flask, render_template, request, redirect, session
import sqlite3
from sqlite3 import Error
from flask_bcrypt import Bcrypt
from datetime import datetime

app = Flask(__name__)
bcrypt = Bcrypt(app)
# app.secret_key = "hfdsj vfdhsk eunca kaeomca"
DATABASE = "C:/Users/18488/OneDrive - Wellington College/13DTS/Maori_Dictionary/maori_dictionary.db"


def create_connection(db_file):
    """
    Create a connection with the database
    parameter: name of the database file
    returns: a connection to the file
    """
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
        return None


def is_logged_in():
    """
    A function to return whether the user is logged in or not
    """
    if session.get("email") is None:
        print("Not logged in")
        return False
    else:
        print("Logged in")
        return True


@app.route('/')
def render_homepage():
    return render_template('home.html', logged_in=is_logged_in())


@app.route('/login')
def render_login_page():
    return render_template('login.html', logged_in=is_logged_in())


@app.route('/signup')
def render_signup_page():
    return render_template('signup.html', logged_in=is_logged_in())


app.run(host='0.0.0.0', debug=True)
