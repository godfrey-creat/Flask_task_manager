from flask import render_template, url_for, flash, redirect, request
from app import app, db
from app.forms import RegistrationForm, LoginForm, TaskForm
from app.models import User, Task, Department
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'Success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirecf(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@login_required
@app.route("/dashboard")
def dashboard():
    if current_user.is_manager:
        return redirect(url_for('manager_dashboard'))
    tasks = Task.query.filter_by(user_id=current_user.id)
    return render_template('employee_dashboard.html', tasks=tasks)

@login_required
@app.route("/manager_dashboard")
def manager_dashboard():
    if not current_user.is_manager:
        return redirect(url_for('dashboard'))
    departments = Department.query.all()
    return render_template('manager_dashboard.html', departments=departments)

@login_required
@app.route("tasks/new", methods=['GET', 'POST'])
def new_task():
    if not current_user.is_manager:
        return redirect(url_for('dashboard'))
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, description=form.description.data, due_date=form.due_date.data, status=form.status.data, user_id=current_user.id)
        db.session.add(task)
        db.session.commit()
        flash('Task has been created!', 'success')
        return redirect(url_for('manager_dashboard'))
    return render_template('task_form.html', title='New task', form=form)