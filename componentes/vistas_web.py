from flask import Flask, render_template, request, redirect, session, jsonify
from conexion_db import config_db as c_db
from componentes.modelos import User,Users,Data_login,User_dl
from main import app

@app.route('/',methods=['GET', 'POTS'])
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'userName'in request.form and 'userPassword':
        _userName = request.form['userName']
        _userPassword = request.form['userPassword']
        print(_userName)
        print(_userPassword)
        try:
            lista_login = Data_login().lista_data_login
        except TypeError:
            # Si el usuario no existe, devolver error 404 (No encontrado)
            return jsonify({'mensaje': 'login no encontrado'}), 404
        print(lista_login) 
        if _userName in lista_login[0]["userName"]:
            if   lista_login[0]["userPassword"] == _userName:
                return render_template('/base.html')
        else:
            return render_template('auth/login.html')

        

    return render_template('auth/login.html')


