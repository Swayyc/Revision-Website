import sys

from flask import Flask, render_template

import mysql.connector

config = {
    'user': 'tl_S2401729',
    'password':'tl_S2401729',
        'host': 'ND-COMPSCI',
    'database':'tl_s2401729_revision'
}

try:
    cnx = mysql.connector.connect(**config)
    cnx.close()
    print("connected!")
except mysql.connector.Error as e:
    print("#"*len(e.msg))
    print(e.msg)
    print("#"*len(e.msg))
    sys.exit()

app= Flask(__name__)

users = {}