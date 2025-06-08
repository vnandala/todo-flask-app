from utils.auth_utils import token_required
from flask import Blueprint, request, jsonify
from models.todo import Todo
from db.db_setup import db

todo_bp = Blueprint('todo_routes', __name__)

@todo_bp.route("/todos", methods=["GET"])
@token_required
def get_todos(current_user):
    todos = Todo.query.filter_by(user_id=current_user.id).all()
    return jsonify([todo.to_dict() for todo in todos])

@todo_bp.route("/todos", methods=["POST"])
@token_required
def create_todo(current_user):
    data = request.get_json()
    new_todo = Todo(task=data["task"], user_id=current_user.id)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({"message": "To-do added!"}), 201

@todo_bp.route("/todos/<int:todo_id>", methods=["PUT"])
@token_required
def update_todo(current_user, todo_id):
    data = request.get_json()
    todo = Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()
    if not todo:
        return jsonify({"error": "To-do not found"}), 404
    todo.task = data["task"]
    db.session.commit()
    return jsonify({"message": "To-do updated!"})

@todo_bp.route("/todos/<int:todo_id>", methods=["DELETE"])
@token_required
def delete_todo(current_user, todo_id):
    todo = Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()
    if not todo:
        return jsonify({"error": "To-do not found"}), 404
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"message": "To-do deleted!"})

