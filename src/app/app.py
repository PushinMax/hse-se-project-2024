from service import *
from entities import *
from flask import Flask, request, render_template, redirect, url_for, flash, session
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.secret_key = 'your_secret_key'

class CommentForm(FlaskForm):
    file_name = StringField('Номер посылки', validators=[DataRequired()])
    comment = TextAreaField('Комментарий', validators=[DataRequired()])
    submit = SubmitField('Отправить комментарий')

class TaskForm(FlaskForm):
    task_name = StringField('Название задания', validators=[DataRequired()])
    task_description = TextAreaField('Описание задания', validators=[DataRequired()])
    submit = SubmitField('Добавить задачу')

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    login = request.form['login']
    password = request.form['password']
    user = User_service.login(login, password)
    if (user is not None):
        session['id'] = user.id
        if (user.role == "student"):
            return redirect(url_for('student_main_menu'))
        else:
            return redirect(url_for('teacher_main_menu'))
    else:
        flash('Неправильное имя пользователя или пароль!')
        return redirect(url_for('home'))

@app.route("/register")
async def register(user: User):
    User_service.register(user.login, user.password, user.role)


@app.route("/leaderboard")
async def leaderboard():
    return Task_service.leaderboard()

@app.post("/main_menu")
def student_main_menu():
    tasks_list = Task_service.get_tasks()
    task_id = request.form['taskid']
    filename = request.form['filename']
    Task_service.submit(session['id'], task_id, filename)



@app.post("/main_menu")
def teacher_main_menu():
    tasks_list = Task_service.get_tasks()
    teacher_tasks = set([task for task in tasks_list if task.teacher_id == session['id']])
    subs = [s for s in Task_service.get_submissions() if s.task_id in teacher_tasks]


    table = [[sub.submission_id, sub.user_id, sub.task_id] for sub in subs]
    # Task_service.get_submissions()[sub_id].feedback
    # Task_service.get_submissions()[sub_id].fixes

@app.route("/", methods=["GET", "POST"])
def teacher_main_menu():
    tasks_list = Task_service.get_tasks()
    teacher_tasks = set([task for task in tasks_list if task.teacher_id == session['id']])
    subs = [s for s in Task_service.get_submissions() if s.task_id in teacher_tasks]

    table = [[sub.submission_id, sub.user_id, sub.task_id] for sub in subs]


    comment_form = CommentForm()
    task_form = TaskForm()

    if comment_form.validate_on_submit():
        file_name = comment_form.file_name.data
        comment = comment_form.comment.data

        print(f"Файл: {file_name}, Комментарий: {comment}")
        return redirect(url_for('teacher_main_menu'))

    if task_form.validate_on_submit():

        task_name = task_form.task_name.data
        task_description = task_form.task_description.data

        print(f"Задание: {task_name}, Описание: {task_description}")
        return redirect(url_for('teacher_main_menu'))

    return render_template('teacher_main_menu.html',
                           submissions=table,
                           comment_form=comment_form, task_form=task_form,
                           history=subs.feedback())

