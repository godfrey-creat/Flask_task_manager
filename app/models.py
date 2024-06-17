from datetime import datetime
from app import db, login_manager
from flak_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_manager = db.Column(db.Boolean, default=False)
    tasks = db.relationship('Task', backref='assignee', lazy=True)
    department_id = db.Column(db.Integer, db.ForeignKey('department_id'))

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    users = db.relationship('User', backref='department', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable= False)
    due_date = db.Column(db.Datetime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False, default='In Progress')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
