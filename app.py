import random
from flask import Flask, jsonify, request
from flasgger import Swagger
from logic import es_palindromo,contador_de_palabras,factorial,cifrador,descifrador,encontrar_paises_por_capital
from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
from flask_wtf import Form
from wtforms import TextField


 
app = Flask(__name__)
Swagger(app)






'''@app.route('/')
def my_form():
    return render_template('test.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text'
    processed_text = es_palindromo(text) and contador_de_palabras(text) == 4
    return render_template('test.html',**locals())


app.run(debug=True)
'''


@app.route('/api/palindromo/<string:cadena>/', methods=['GET'])
def palindromo(cadena):
    """
    This is the cadena palindromo's API
    Call this api passing a cadena  and get back if it's palindromo
    ---
    tags:
      - Awesomeness Cadena API
    parameters:
      - name: cadena
        in: path
        type: string
        required: true
        description: check if cadena is palindromo.
    responses:
      200:
        description: A cadena  is palindromo or not
                    

    """

    return jsonify(
        cadena=cadena,
        result=es_palindromo(cadena)
    )

@app.route('/api/contador_de_palabras/<string:cadena>/', methods=['GET'])
def contador(cadena):
    """
    This is the cadena  contador de palabras API
    Call this api passing a cadena  and get back how many words it has.
    ---
    tags:
      - Awesomeness Cadena API
    parameters:
      - name: cadena
        in: path
        type: string
        required: true
        description: check if cadena is palindromo.
    responses:
      200:
        description: number of words in cadena
                    

    """

    return jsonify(
        cadena=cadena,
        result=contador_de_palabras(cadena)
    )

@app.route('/api/factorial/<int:num>/', methods=['GET'])
def fact(num):
    """
    This is the num factorial API
    Call this api passing a num  and get back num!.
    ---
    tags:
      - Awesomeness Cadena API
    parameters:
      - name: num
        in: path
        type: num
        required: true
        description: calculate the factorial of num
    responses:
      200:
        description: factorial of num
                    

    """

    return jsonify(
        num=num,
        result=int(factorial(num))
    )


@app.route('/api/cifrado/<string:cadena>/', methods=['GET'])
def cifrado(cadena):
    """
    This is the cadena cypher API
    Call this api passing a cadena  and get it back encrypted.
    ---
    tags:
      - Awesomeness Cadena API
    parameters:
      - name: cadena
        in: path
        type: string
        required: true
        description: return the cadena encrypted
    responses:
      200:
        description: encrypted cadena
                    

    """

    return jsonify(
        cadena=cadena,
        result=cifrador(cadena)
    )


@app.route('/api/descifrado/<string:cadena>/', methods=['GET'])
def descifrado(cadena):
    """
    This is the cadena uncypher API
    Call this api passing a cadena encrypted  and get it back unencrypted.
    ---
    tags:
      - Awesomeness Cadena API
    parameters:
      - name: cadena
        in: path
        type: string
        required: true
        description: return the cadena unencrypted
    responses:
      200:
        description: unencrypted cadena
                    

    """

    return jsonify(
        cadena=cadena,
        result=descifrador(cadena)
    )

@app.route('/api/paises_por_capital/<string:capital>/', methods=['GET'])
def encontrar_pais_por_capital(capital):
    """
    This is the find contry by capital API
    Call this api passing a capital and get the country it belongs.
    ---
    tags:
      - Awesomeness Cadena API
    parameters:
      - name: capital
        in: path
        type: string
        required: true
        description: return the country
    responses:
      200:
        description: country
                    

    """

    return jsonify(
        capital=capital,
        result=encontrar_paises_por_capital(capital)
    )




app.run(debug=True)
