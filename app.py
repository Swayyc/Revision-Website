from flask import Flask, render_template, request, redirect, url_for
import sys

from flask import Flask, render_template

import mysql.connector

config = {
    'user': 'tl_S2401729',
    'password':'tl_S2401729',
        'host': 'ND-COMPSCI',
    'database':'tl_s2401729_revision'
}



app= Flask(__name__)


@app.route("/",methods=["GET","POST"])
def main(): # put application's code here
    error= None
    if request.method =="POST":

        username = request.form['username']
        password =request.form['password']
        email = request.form['email']
        if not username or not password:
            return redirect(url_for('Register_Page'))
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO users (username, password, email) 
                         VALUES (%s, %s, %s)""", [username, password, email])
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as ex:
            print(ex)
    return render_template("Register_Page.html")
@app.route('/HomePg`')
def homepg(): #put application's code here
    return render_template("HomePg.html")
@app.route('/Subjects`')
def subjects(): #put application's code here
    return render_template("Subjects.html")


if __name__ == '__main__':
    app.run()
