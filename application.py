import os

from flask import Flask,render_template,request,flash
from flask_socketio import SocketIO, emit
from env import Config

app = Flask(__name__)
#app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

app.config.from_object(Config)
socketio = SocketIO(app)


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        pseudo = request.form['pseudo']
        return pseudo
    else: 
        return 'Bienvenue a la page de chatte' 
    


@app.route('/login')
def login():

    return render_template('login.html')