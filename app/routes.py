from flask import Blueprint, render_template, request, redirect, url_for
from .models import Todo

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    todos = Todo.get_all()
    return render_template('index.html', todos=todos)

@routes.route('/add', methods=['POST'])
def add_todo():
    title = request.form.get('title')
    if title:
        # Simulating SQL injection vulnerability
        query = f"INSERT INTO todos (title) VALUES ('{title}')"
        Todo.raw(query)  # Assuming Todo.raw can execute raw SQL queries
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
