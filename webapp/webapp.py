import random
from flask import Flask, jsonify, request
from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
from flask_wtf import Form
import requests
from google_images_download import google_images_download






app = Flask(__name__,static_url_path='')


base_url = 'http://178.128.40.45/api/'
metodos = {'palindromo':'palindromo/','contador':'contador_de_palabras/','factorial':'factorial/','cifrado':'cifrado/','descifrado':'descifrado/','capital':'paises_por_capital/'}


@app.route('/')
def my_form():
    return render_template('test.html')

@app.route('/', methods=['POST'])
def my_form_post():

    cadena_palindromo = request.form['cadena_palindromo']
    if cadena_palindromo:
        palindromo = requests.get(base_url+metodos['palindromo']+cadena_palindromo+'/').json()['result']

    cadena_contar = request.form['cadena_contar']
    if cadena_contar:    
        recuento_cadena = requests.get(base_url+metodos['contador']+cadena_contar+'/').json()['result']

    numero_fact = request.form['numero_fact']
    if numero_fact:
        resultado_factorial = requests.get(base_url+metodos['factorial']+numero_fact+'/').json()['result']

    cadena_cifrar = request.form['cadena_cifrar']
    if cadena_cifrar:
        cadena_cifrada = requests.get(base_url+metodos['cifrado']+cadena_cifrar+'/').json()['result']

    cadena_descifrar = request.form['cadena_descifrar']
    if cadena_descifrar:
        cadena_descifrada = requests.get(base_url+metodos['descifrado']+cadena_descifrar+'/').json()['result']

    capital = request.form['capital']
    if capital:
        pais = requests.get(base_url+metodos['capital']+capital+'/').json()['result']
        response = google_images_download.googleimagesdownload()   #class instantiation
        busqueda = pais+'flag'
        arguments = {"keywords":busqueda,"output_directory" : './static',"image_directory" : '/',"limit":1,"print_urls":False}   #creating list of arguments
        imgpath = response.download(arguments)[busqueda][0].split('/')[-1]
    
    return render_template('resultados.html',**locals())




app.run(host='0.0.0.0',port=80)
