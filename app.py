from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime

app = Flask(__name__, template_folder="templates")

todos = [{'task': "Sample ToDo", 'done': False, 'due_date': None}]


@app.route("/")
def index():
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    todo = request.form["todo"]
    due_date_str = request.form["due_date"]
    due_date = datetime.strptime(due_date_str, '%Y-%m-%dT%H:%M')

    todos.append({"task": todo, "done": False, "due_date": due_date})
    return redirect(url_for("index"))


@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    todo = todos[index]
    if request.method == 'POST':
        todo['task'] = request.form["todo"]
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo, index=index)


@app.route("/check/<int:index>")
def check(index):
    todos[index]["done"] = not todos[index]["done"]
    return redirect(url_for("index"))


@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for("index"))


@app.route("/events")
def get_events():
    event_data = []
    for index, todo in enumerate(todos):
        event = {
            'id': index,
            'title': todo['task'],
            'start': todo['due_date'].strftime('%Y-%m-%dT%H:%M') if todo['due_date'] else None,
        }
        event_data.append(event)
    return jsonify(event_data)


if __name__ == '__main__':
    app.run(debug=True)
