from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store todos in a list (we'll use this instead of a database for simplicity)
todos = []

@app.route('/')
def index():
    print("Accessing index route")  # Debug print
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    print("Accessing add route")  # Debug print
    todo = request.form.get('todo')
    if todo:
        todos.append({'task': todo, 'done': False})
        print(f"Added todo: {todo}")  # Debug print
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    print(f"Deleting todo at index: {index}")  # Debug print
    if 0 <= index < len(todos):
        removed_todo = todos.pop(index)
        print(f"Deleted todo: {removed_todo}")  # Debug print
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)