from zoneinfo import ZoneInfo
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

class Tasks(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    plan = db.Column(db.String(255), nullable=False)
    state = db.Column(db.SmallInteger, nullable=False, default=1)
    create_time = db.Column(db.DateTime, default=lambda: datetime.now(ZoneInfo("Asia/Tokyo")), nullable=False)
    update_time = db.Column(db.DateTime, default=lambda: datetime.now(ZoneInfo("Asia/Tokyo")), onupdate=lambda: datetime.now(ZoneInfo("Asia/Tokyo")), nullable=False)
    delete_time = db.Column(db.DateTime, nullable=True)
    
    def __repr__(self):
        return f'<Tasks {self.id}>'