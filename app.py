#!/usr/bin/python3

from flask import Flask, jsonify, request
import datetime as dt
import random

app = Flask(__name__)

number = random.randint(0,99)

jsonlist = [
  {'num_random': number, 'date': dt.datetime.now()}
]

@app.route('/api')
def get_jsonlist():
  return jsonify(jsonlist)

@app.route("/")
def hello_world():
    return "<h1>Desafio Stone! </h1> <p> para testar a aplicação colocar /api no URI <p>"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
 