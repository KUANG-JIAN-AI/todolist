from flask import Flask, jsonify, render_template, request
from controller import get_all_users, create_user

def register_routes(app: Flask):
    @app.route('/')
    def index():
        return render_template("index.html")

    @app.route('/users', methods=['GET'])
    def users():
        return jsonify(get_all_users())

    @app.route('/users', methods=['POST'])
    def add_user():
        data = request.json
        username = data.get('username')
        email = data.get('email')
        if not username or not email:
            return jsonify({'error': 'Missing username or email'}), 400
        return jsonify(create_user(username, email))
