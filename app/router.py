from flask import Blueprint, jsonify, render_template
from app.controller import delete_tasks, get_tasks, create_tasks, update_tasks

main_bp = Blueprint("main", __name__)
@main_bp.route('/')
def index():
    return render_template("index.html")

@main_bp.route('/tasks', methods=['GET'])
def tasks():
    return jsonify(get_tasks())

@main_bp.route('/tasks', methods=['POST'])
def add_tasks():
    return jsonify(create_tasks())

@main_bp.route('/tasks', methods=['PUT'])
def up_tasks():
    return jsonify(update_tasks())

@main_bp.route('/tasks', methods=['DELETE'])
def del_tasks():
    return jsonify(delete_tasks())