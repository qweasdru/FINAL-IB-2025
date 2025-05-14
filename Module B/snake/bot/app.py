
from flask import Flask, request, render_template, redirect, session
from jinja2 import Template
import os
from flask_session import Session

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Класс, который можно вызвать из шаблона через __subclasses__()
class FlagReader:
    def __init__(self, path):
        self.path = path
    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

@app.route("/")
def index():
    return redirect("/snake")

@app.route("/snake")
def snake_game():
    return render_template("snake.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "")
    score = request.form.get("score", "0")
    if "scores" not in session:
        session["scores"] = []
    session["scores"].append({"name": name, "score": score})
    return redirect("/scoreboard")

@app.route("/scoreboard")
def scoreboard():
    scores = session.get("scores", [])
    rendered_scores = []
    for entry in scores:
        try:
            tmpl = Template(entry["name"])
            name_rendered = tmpl.render()
        except Exception as e:
            name_rendered = f"Error: {e}"
        rendered_scores.append({"name": name_rendered, "score": entry["score"]})
    return render_template("scoreboard.html", scores=rendered_scores)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7008)
