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
    id = db.Column(db.Integer, primary_key=True)
    plan = db.Column(db.String(255), nullable=False)
    state = db.Column(db.SmallInteger, nullable=False, default=1)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    update_time = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    delete_time = db.Column(db.DateTime, nullable=True)
    
    def __repr__(self):
        return f'<Tasks {self.id}>'