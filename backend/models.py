# backend/models.py
from backend.database import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    owner_name = db.Column(db.String(120), nullable=False)
    co_owner_name = db.Column(db.String(120))
    tower = db.Column(db.String(50), nullable=False)
    floor = db.Column(db.String(50), nullable=False)
    flat = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    user_image = db.Column(db.String(100), nullable=True)
