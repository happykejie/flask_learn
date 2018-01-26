from datetime import datetime

from flask import render_template, request, jsonify

from api.models import Todo, TodoForm
from api import api


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@api.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@api.route('/')
def index():
    form = TodoForm()
    todos = Todo.objects.order_by('-time')
    return render_template("index.html",todos=todos,form=form)


@api.route('/add', methods=['POST',])
def add():
    form = TodoForm(request.form)
    if form.validate():
        content = form.content.data
        todo = Todo(content=content,time=datetime.now())
        todo.save()
    todos = Todo.objects.order_by('-time')
    return render_template("index.html",todos=todos,form=form)

@api.route('/done/<string:todo_id>')
def done(todo_id):
    form = TodoForm()
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.status = 1
    todo.save()
    todos = Todo.objects.order_by('-time')
    return render_template("index.html",todos=todos,form=form)


@api.route('/undone/<string:todo_id>')
def undone(todo_id):
    form = TodoForm()
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.status = 0
    todo.save()
    todos = Todo.objects.order_by('-time')
    return render_template("index.html",todos=todos,form=form)

@api.route('/delete/<string:todo_id>')
def delete(todo_id):
    form = TodoForm()
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.delete()
    todos = Todo.objects.order_by('-time')
    return render_template("index.html",todos=todos,form=form)


@api.errorhandler(404)
def not_found(error):
    return render_template('404.html')