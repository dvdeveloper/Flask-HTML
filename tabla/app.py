from flask import Flask,render_template

app = Flask(__name__,template_folder='views')
#set FLASK_ENV=development -> activar modo debug on en windows
#export FLASK_ENV=development -> activar modo debug on en linux

@app.route('/')
def index():
    users = [ 'Rosalia','Adrianna','Victoria' ]
    return render_template('index.html',usuarios = users)