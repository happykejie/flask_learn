from datetime import datetime

from flask import render_template, request,jsonify

from app.models import Todo, TodoForm
from app import app

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

#Home
@app.route('/main/')
def mainpage():
    return  render_template("main.html")

#category
@app.route('/category/')
def category():
    return  render_template("category.html")
#me
@app.route('/me/')
def me():
    return  render_template("me.html")


#detail
@app.route('/detail/')
def detail():
    return  render_template("detail.html")

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