from flask import Flask, request, jsonify, session
from flask_session import Session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

with open('secret_flag.txt') as f:
    FLAG = f.read().strip()

@app.route('/', methods=['GET'])
def index():
    return 'ChatBot is running on /chat'

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    
    # Инициализация сессии
    if 'history' not in session:
        session['history'] = []

    session['history'].append(user_input)

    # Простенький ответ
    if "hello" in user_input.lower():
        return jsonify({'response': 'Hi there! I am ChatBot.'})

    # Уязвимость: eval на определенное условие (например, если input начинается с "_exec:")
    if user_input.startswith('_exec:'):
        try:
            code = user_input[len('_exec:'):].strip()
            # ⚠️ Уязвимый eval
            result = eval(code, {"__builtins__": {}}, {"flag": FLAG})
            return jsonify({'response': str(result)})
        except Exception as e:
            return jsonify({'response': f'Error: {e}'})

    return jsonify({'response': 'I am not sure how to respond to that.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7007)
