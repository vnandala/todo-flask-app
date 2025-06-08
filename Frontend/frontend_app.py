# frontend/frontend_app.py

from flask import Flask, render_template, redirect, request, url_for
import requests

app = Flask(__name__, template_folder="templates", static_folder="static")
API_BASE = "http://127.0.0.1:5000"  # Backend running locally

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/todos")
def todos_page():
    return render_template("todos.html")

if __name__ == "__main__":
    app.run(port=3000, debug=True)
