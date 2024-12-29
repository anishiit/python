from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

class Todo:
    def __init__(self, task):
        self.task = task
        self.done = False
        self.created_at = datetime.now()
        self.completed_at = None

    def toggle(self):
        self.done = not self.done
        self.completed_at = datetime.now() if self.done else None

    def get_status(self):
        return "Completed" if self.done else "Pending"

# Store todos in a list with more functionality
todos = []

@app.route('/')
def index():
    pending_count = sum(1 for todo in todos if not todo.done)
    completed_count = len(todos) - pending_count
    return render_template('index.html', 
                         todos=todos,
                         pending_count=pending_count,
                         completed_count=completed_count)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('todo')
    if task:
        new_todo = Todo(task)
        todos.append(new_todo)
    return redirect(url_for('index'))

@app.route('/toggle/<int:index>')
def toggle(index):
    if 0 <= index < len(todos):
        todos[index].toggle()
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(todos):
        todos.pop(index)
    return redirect(url_for('index'))

@app.route('/clear_completed')
def clear_completed():
    global todos
    todos = [todo for todo in todos if not todo.done]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)