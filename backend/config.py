# backend/config.py
import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(24)
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///durgapuja.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
