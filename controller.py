from datetime import datetime
from zoneinfo import ZoneInfo
from flask import request
from model import Tasks, User, db

def get_all_users():
    users = User.query.all()
    return [{'id': u.id, 'username': u.username, 'email': u.email} for u in users]

def create_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return {'id': user.id, 'username': user.username, 'email': user.email}

def get_tasks():
    page = request.args.get("page", 1, type=int)
    tasks = Tasks.query.paginate(page=page, per_page=5)
    return [{'id': t.id, 'plan': t.plan, 'state': t.state} for t in tasks]

def create_tasks(plan):
    tasks = Tasks(plan=plan)
    db.session.add(tasks)
    db.session.commit()
    return {'id': tasks.id, 'plan': tasks.plan}

def delete_tasks(id):
    tasks = Tasks.query.get(id)
    if tasks:
        tasks.delete_time = datetime.now(ZoneInfo("Asia/Tokyo"))
        db.session.commit()
        return {'code': 200, 'msg': 'success'}
    return {'code': 404, 'msg': 'error'}