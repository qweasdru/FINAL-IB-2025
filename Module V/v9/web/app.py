from flask import Flask, render_template, request
import subprocess, uuid, random, threading
import os

app = Flask(__name__)
TTL = 300
CHALLENGES = [f"service{i}" for i in range(1, 7)]
sessions = {}

@app.route("/")
def index():
    return render_template("index.html", challenges=CHALLENGES)

@app.route("/start/<cid>", methods=["POST"])
def start(cid):
    if cid not in CHALLENGES:
        return f"Unknown service: {cid}"
    port = random.randint(20000, 40000)
    image = f"black_astra_{cid}"
    path = f"/services/{cid}"
    container_name = f"{cid}_{uuid.uuid4().hex[:6]}"

    try:
        subprocess.run(["docker", "build", "-t", image, path], check=True)
        subprocess.run([
            "docker", "run", "-d",
            "-p", f"{port}:1337",
            "--rm",
            "--name", container_name,
            image
        ], check=True)
    except subprocess.CalledProcessError as e:
        return f"Ошибка при запуске: {e}", 500

    return f"{cid} started on port {port}"

@app.route("/launch/<int:mid>")
def launch_mission(mid):
    if 1 <= mid <= 6:
        cid = f"service{mid}"
        # просто вызываем тот же механизм, что и в /start/<cid>
        try:
            response = start(cid)
            if isinstance(response, tuple):  # error
                return response
            port = int(response.split()[-1])
            return render_template("challenge.html", mission=cid, port=port, ttl=TTL)
        except Exception as e:
            return f"Ошибка при запуске миссии: {e}", 500
    return "Invalid mission ID", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
