from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_migrate import Migrate
from models import db, bcrypt, User, Department, Task
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = User(username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify(message="User registered"), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    return jsonify(message="Invalid credentials"), 401

@app.route('/assign_manager', methods=['POST'])
@jwt_required()
def assign_manager():
    current_user = get_jwt_identity()
    user = User.query.get(current_user)
    if not user.is_manager:
        return jsonify(message="Only managers can assign roles"), 403

    data = request.get_json()
    user_to_promote = User.query.get(data['user_id'])
    if user_to_promote:
        user_to_promote.is_manager = True
        db.session.commit()
        return jsonify(message="User promoted to manager"), 200
    return jsonify(message="User not found"), 404

@app.route('/departments', methods=['POST'])
@jwt_required()
def create_department():
    current_user = get_jwt_identity()
    user = User.query.get(current_user)
    if not user.is_manager:
        return jsonify(message="Only managers can create departments"), 403

    data = request.get_json()
    department = Department(name=data['name'], manager_id=user.id)
    db.session.add(department)
    db.session.commit()
    return jsonify(message="Department created"), 201

@app.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    current_user = get_jwt_identity()
    user = User.query.get(current_user)
    if not user.is_manager:
        return jsonify(message="Only managers can create tasks"), 403

    data = request.get_json()
    task = Task(
        title=data['title'],
        description=data['description'],
        due_date=data['due_date'],
        assigned_to_id=data['assigned_to_id'],
        department_id=data['department_id'],
        created_by_id=user.id
    )
    db.session.add(task)
    db.session.commit()
    return jsonify(message="Task created"), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
@jwt_required()
def update_task(task_id):
    current_user = get_jwt_identity()
    user = User.query.get(current_user)
    if not user.is_manager:
        return jsonify(message="Only managers can update tasks"), 403

    task = Task.query.get(task_id)
    if not task:
        return jsonify(message="Task not found"), 404

    data = request.get_json()
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.due_date = data.get('due_date', task.due_date)
    task.is_completed = data.get('is_completed', task.is_completed)
    db.session.commit()
    return jsonify(message="Task updated"), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
    current_user = get_jwt_identity()
    user = User.query.get(current_user)
    if not user.is_manager:
        return jsonify(message="Only managers can delete tasks"), 403

    task = Task.query.get(task_id)
    if not task:
        return jsonify(message="Task not found"), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify(message="Task deleted"), 200

@app.route('/tasks/<int:task_id>/status', methods=['PATCH'])
@jwt_required()
def update_task_status(task_id):
    current_user = get_jwt_identity()
    user = User.query.get(current_user)
    task = Task.query.get(task_id)
    if not task:
        return jsonify(message="Task not found"), 404
    if task.assigned_to_id != user.id:
        return jsonify(message="You can only update your own tasks"), 403

    data = request.get_json()
    task.is_completed = data.get('is_completed', task.is_completed)
    db.session.commit()
    return jsonify(message="Task status updated"), 200

@app.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    current_user = get_jwt_identity()
    user = User.query.get(current_user)
    if user.is_manager:
        tasks = Task.query.all()
    else:
        tasks = Task.query.filter_by(assigned_to_id=user.id).all()
    return jsonify([task.as_dict() for task in tasks]), 200

if __name__ == '__main__':
    app.run(debug=True)

