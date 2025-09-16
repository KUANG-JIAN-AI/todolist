from model import User, db

def get_all_users():
    users = User.query.all()
    return [{'id': u.id, 'username': u.username, 'email': u.email} for u in users]

def create_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return {'id': user.id, 'username': user.username, 'email': user.email}
