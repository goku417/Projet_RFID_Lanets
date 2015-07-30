#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Benevole import Benevole
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
liste_benevole = []

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
@app.route('/gerer')
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

@app.route('/chercher', methods=['GET', 'POST'])
def chercher_benevole():
    personne = None
    if request.method == 'GET':
        return render_template('chercher.html')
    elif request.method == 'POST':
        conn = mysql.connect
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Benevoles where rfid = %s''', (request.form['rfid'],))
        data = cur.fetchall()

        if data is None :
            return render_template('notfound.html')
        else:
            if len(liste_benevole) > 0:
                for benevole in liste_benevole:
                    if benevole.get_rfid() == request.form['rfid']:
                        personne = benevole
            else:
                print data[0][1]
                print data[0][2]
                print data[0][3]
                personne = Benevole(data[0][1],data[0][2], data[0][3])
                liste_benevole.append(personne)

        return render_template('resultat.html', prenom=personne.get_first_name(),
                               nom=personne.get_last_name(), rfid=personne.get_rfid(),
                               nb_repas=personne.liste_coupons.get_count_liste('repas'),
                               nb_collations=personne.liste_coupons.get_count_liste('collation'))

@app.route('/ajouter', methods=['POST'])
def ajouter_coupon():
    rfid = request.form['rfid']
    type_coupon = request.form['coupon']
    for x in liste_benevole:
        if x.get_rfid() == rfid:
            conn = mysql.connect
            cur = conn.cursor()
            if type_coupon == 'repas':
                cur.execute('''SELECT Repas FROM Benevoles WHERE rfid=%s''', (rfid,))
                data = cur.fetchall()
                nombre = int(data[0][0]) + 1
                cur.execute('''UPDATE Benevoles SET Repas=%s WHERE rfid=%s''', (nombre,rfid,))
                conn.commit()
                cur.execute('''SELECT TotalRepas FROM Coupons''')
                data = cur.fetchall()
                nombre_total = int(data[0][0]) + 1
                cur.execute('''UPDATE Coupons SET TotalRepas = %s''', (nombre_total,))
                conn.commit()
            elif type_coupon == 'collation':
                cur.execute('''SELECT Collations FROM Benevoles WHERE rfid=%s''', (rfid,))
                data = cur.fetchall()
                nombre = int(data[0][1]) + 1
                cur.execute('''UPDATE Benevoles SET Collations=%s WHERE rfid=%s''', (nombre,rfid,))
                conn.commit()
                cur.execute('''SELECT TotalCollation FROM Coupons''')
                data = cur.fetchall()
                nombre_total = int(data[0][0]) + 1
                cur.execute('''UPDATE Coupons SET TotalCollation = %s''', (nombre_total,))
                conn.commit()

    return render_template('ajouter.html', prenom=request.form['prenom'], coupon=type_coupon)

if __name__ == '__main__':
    app.debug = True
    app.run()
