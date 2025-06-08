import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "super-secret-dev-key"
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:Vamrich%40123@localhost/todoapp"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True  # Optional: enable debug mode
