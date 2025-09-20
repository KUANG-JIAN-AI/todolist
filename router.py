from flask import Flask, jsonify, render_template
from controller import delete_tasks, get_tasks, create_tasks, update_tasks

def register_routes(app: Flask):
    @app.route('/')
    def index():
        return render_template("index.html")

    @app.route('/tasks', methods=['GET'])
    def tasks():
        return jsonify(get_tasks())

    @app.route('/tasks', methods=['POST'])
    def add_tasks():
        return jsonify(create_tasks())
    
    @app.route('/tasks', methods=['PUT'])
    def up_tasks():
        return jsonify(update_tasks())

    @app.route('/tasks', methods=['DELETE'])
    def del_tasks():
        return jsonify(delete_tasks())