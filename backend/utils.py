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

def send_task_notification(task):
    subject = f"Task Due: {task.title}"
    message = f"The task '{task.title}' is due on {task.due_date}."
    recipient_list = [task.assigned_to.email, task.created_by.email]
    send_mail(subject, message, 'your-email@example.com', recipient_list)

