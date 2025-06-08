import os
from flask import Flask, render_template
from config import Config
from db.db_setup import db
from routes.todo_routes import todo_bp
from routes.auth_routes import auth_bp
from flask_cors import CORS

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "Frontend", "templates"),
    static_folder=os.path.join(BASE_DIR, "Frontend", "static")
)

CORS(app)
app.config.from_object(Config)
db.init_app(app)

# Routes for rendering frontend pages
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard_page():
    return render_template("dashboard.html")

# Register API route blueprints
app.register_blueprint(todo_bp)
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)
