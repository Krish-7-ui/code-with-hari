from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database"
todos = [
    {"id": 1, "task": "Buy milk", "done": False},
    {"id": 2, "task": "Read book", "done": False}
]

# Home route
@app.route('/')
def home():
    return "Welcome to the Simple Todo API!"

# Get all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# Get a single todo by ID
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    return jsonify(todo) if todo else ('Not found', 404)

# Create a new todo
@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    new_todo = {
        "id": todos[-1]['id'] + 1 if todos else 1,
        "task": data.get('task', ''),
        "done": False
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

# Update an existing todo
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if not todo:
        return ('Not found', 404)
    todo.update({
        "task": data.get('task', todo['task']),
        "done": data.get('done', todo['done'])
    })
    return jsonify(todo)

# Delete a todo
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t['id'] != todo_id]
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)
