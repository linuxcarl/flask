"""
SE CORRE EN EL ENTORNO VIRTUAL Y DEFINIMOS VARIABLES DE ENTORNO PARA QUE FUNCIONE 
export FLASK_APP=main.py
export FLASK_DEBUG=1
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello flask PY"