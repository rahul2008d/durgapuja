# backend/config.py
import os

# from redis import Redis


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(24)

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///durgapuja.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    # SESSION_TYPE = "redis"
    # SESSION_PERMANENT = False
    # SESSION_USE_SIGNER = True
    # SESSION_REDIS = Redis.from_url("redis://127.0.0.1:6379")
