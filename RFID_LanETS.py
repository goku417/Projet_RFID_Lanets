#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask_mysqldb import MySQL
from hashlib import md5

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_USER'] = 'bhtan'
app.config['MYSQL_PASSWORD'] = 'bacon123'
app.config['MYSQL_DB'] = 'rfid_lanets'
mysql.init_app(app)
authorize = False
username = None

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        authorization = authentification(request.form['username'], request.form['password'])
        if authorization:
            global authorize
            authorize = authorization
            global username
            username = request.form['username']
            return render_template('manage.html', username=username)
        else:
            return render_template('error.html')
    elif request.method == 'GET':
        if authorize:
            return render_template('manage.html', username=username)
        else:
            return render_template('error.html')

def gerer():
    return render_template('manage.html')

def authentification(username, password):
    authorize = False
    cur = mysql.connection.cursor()
    cur.execute('''SELECT password FROM Admins where username= %s''', (username,))
    data = cur.fetchall()
    print str(data[0][0])
    if md5(password).hexdigest() == data[0][0]:
        authorize =  True
    else:
        authorize = False
    return authorize

@app.route('/creer', methods=['GET', 'POST'])
def creer_benevole():
    if request.method == 'GET':
        return render_template('creer.html')
    elif request.method == 'POST':
        prenom = request.form['prenom']
        nom = request.form['nom']
        rfid = request.form['rfid']
        conn = mysql.connect
        cur = conn.cursor()
        cur.execute('''INSERT INTO Benevoles (Prenom, Nom, rfid) VALUES (%s, %s, %s)''', (prenom, nom, rfid,))
        conn.commit()
        return render_template('succes.html', user=prenom)

if __name__ == '__main__':
    app.debug = True
    app.run()
