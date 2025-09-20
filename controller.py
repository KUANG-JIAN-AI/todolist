from datetime import datetime
from zoneinfo import ZoneInfo
from flask import request
from model import Tasks, db

def get_tasks():
    page = request.args.get("page", 1, type=int)
    plan = request.args.get("plan")
    query  = Tasks.query.order_by(Tasks.id.desc()).filter(Tasks.delete_time.is_(None))
    if plan:
        query = query.filter(Tasks.plan.like(f"%{plan}%"))

    tasks = query.paginate(page=page, per_page=5, error_out=False)

    return {
        'total': tasks.total,
        'pages': tasks.pages,
        'page': page,
        'has_prev': tasks.has_prev,
        'has_next': tasks.has_next,
        'data': [
            {'id': t.id, 'plan': t.plan, 'state': t.state}
            for t in tasks.items
        ]
    }


def create_tasks():
    data = request.get_json()  # 从请求体里解析 JSON
    plan = data.get("plan")
    tasks = Tasks(plan=plan)
    db.session.add(tasks)
    db.session.commit()
    return {'code': 200, 'msg': 'success'}

def update_tasks():
    data = request.get_json()  # 从请求体里解析 JSON
    task_id = data.get("task_id")
    tasks = Tasks.query.get(task_id)
    if tasks:
        tasks.state = 1 - tasks.state
        db.session.commit()
        return {'code': 200, 'msg': 'success'}
    return {'code': 404, 'msg': 'error'}

def delete_tasks():
    data = request.get_json()  # 从请求体里解析 JSON
    task_id = data.get("task_id")
    tasks = Tasks.query.get(task_id)
    if tasks:
        tasks.delete_time = datetime.now(ZoneInfo("Asia/Tokyo"))
        db.session.commit()
        return {'code': 200, 'msg': 'success'}
    return {'code': 404, 'msg': 'error'}