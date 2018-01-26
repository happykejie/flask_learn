from datetime import datetime

from flask import render_template, request,jsonify

from app.models import Todo, TodoForm
from app import app


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

@app.route('/app/tasks/', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/')
def index():
    form = TodoForm()
    todos = Todo.objects.order_by('-time')
    return render_template("index.html",todos=todos,form=form)


@app.route('/api/todolist/')
def api_todolist():
    form = TodoForm()
    todos = Todo.objects.order_by('-time')
    #return render_template("index.html",todos=todos,form=form)
    return  jsonify(todos)


@app.route('/add', methods=['POST',])
def add():
    form = TodoForm(request.form)
    if form.validate():
        content = form.content.data
        todo = Todo(content=content,time=datetime.now())
        todo.save()
    todos = Todo.objects.order_by('-time')
    return render_template("index.html",todos=todos,form=form)

@app.route('/done/<string:todo_id>')
def done(todo_id):
    form = TodoForm()
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.status = 1
    todo.save()
    todos = Todo.objects.order_by('-time')
    return render_template("index.html",todos=todos,form=form)


@app.route('/undone/<string:todo_id>')
def undone(todo_id):
    form = TodoForm()
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.status = 0
    todo.save()
    todos = Todo.objects.order_by('-time')
    return render_template("index.html",todos=todos,form=form)

@app.route('/delete/<string:todo_id>')
def delete(todo_id):
    form = TodoForm()
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.delete()
    todos = Todo.objects.order_by('-time')
    return render_template("index.html",todos=todos,form=form)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')