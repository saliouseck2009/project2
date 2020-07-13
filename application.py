import os

from flask import Flask, render_template, request, flash
from flask_socketio import SocketIO, emit
#from venv import Config

app = Flask(__name__)
#app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

#pp.config.from_object(Config)
socketio = SocketIO(app)


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        pseudo = request.form['pseudo']
        return pseudo


@app.route('/login')
def login():

    return render_template('login.html')
