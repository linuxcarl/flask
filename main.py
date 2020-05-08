"""
SE CORRE EN EL ENTORNO VIRTUAL Y DEFINIMOS VARIABLES DE ENTORNO PARA QUE FUNCIONE 
export FLASK_APP=main.py
export FLASK_DEBUG=1
"""
from flask import Flask, request, make_response, redirect

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response =  make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response

@app.route('/hello')
def hello():
    user_ip = request.remote_addr
    return "Tu ip local es {}".format(user_ip)