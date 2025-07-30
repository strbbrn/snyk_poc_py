from flask import Blueprint, render_template, request, redirect, url_for
from .models import Todo

routes = Blueprint('routes', __name__)

import sqlite3
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
@routes.route('/addUser', methods=['POST'])
def user():
    username = request.form.get('username')
    password = request.form.get('password')
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    
@routes.route('/')
def index():
    todos = Todo.get_all()
    return render_template('index.html', todos=todos)

@routes.route('/add', methods=['POST'])
def add_todo():
    title = request.form.get('title')
    if title:
        Todo.create(title)
    return redirect(url_for('routes.index'))

@routes.route('/update/<int:todo_id>', methods=['POST'])
def update_todo(todo_id):
    todo = Todo.get(todo_id)
    if todo:
        todo.completed = not todo.completed
        todo.save()
    return redirect(url_for('routes.index'))

@routes.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    Todo.delete(todo_id)
    return redirect(url_for('routes.index'))
