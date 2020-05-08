"""
activar nuestro entorno con: source venv/bin/activate
SE CORRE EN EL ENTORNO VIRTUAL Y DEFINIMOS VARIABLES DE ENTORNO PARA QUE FUNCIONE 
export FLASK_APP=main.py
export FLASK_DEBUG=1
"""
from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

todos  = ['TODO 1','TODO 2','TODO 3']

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/hello')
def hello():
    user_ip = request.remote_addr
    context = {
        'user_ip': user_ip,
        'todos': todos
    }
    return render_template('hello.html', **context)
