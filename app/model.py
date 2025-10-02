from zoneinfo import ZoneInfo
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from . import db

class Tasks(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    plan = db.Column(db.String(255), nullable=False)
    # 0 未完成，1 已完成
    state = db.Column(db.SmallInteger, nullable=False, default=0)
    create_time = db.Column(db.DateTime, default=lambda: datetime.now(ZoneInfo("Asia/Tokyo")), nullable=False)
    update_time = db.Column(db.DateTime, default=lambda: datetime.now(ZoneInfo("Asia/Tokyo")), onupdate=lambda: datetime.now(ZoneInfo("Asia/Tokyo")), nullable=False)
    delete_time = db.Column(db.DateTime, nullable=True)
    
    def __repr__(self):
        return f'<Tasks {self.id}>'