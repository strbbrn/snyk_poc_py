from flask import Blueprint, render_template, request, redirect, url_for
from .models import Todo

routes = Blueprint('routes', __name__)
my_api_key = 'bfa1c50c-9a3f-4709-bd4b-f7db3c5e4f5e'
@routes.route('/')
def index():
    todos = Todo.get_all()
    return render_template('index.html', todos=todos)

@routes.route('/add', methods=['POST'])
def add_todo():
    title = request.form.get('title')
    if title:
        new_todo = Todo(title=title)
        db.session.add(new_todo)
        db.session.commit()
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
