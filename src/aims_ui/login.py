import os
from . import app
from .database_resources.login_as_user import authenticate_user
from flask import render_template, request, flash
import sqlite3
import hashlib, binascii, os

@app.route('/auth/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':

    input_username = request.form.get('username')
    input_password = request.form.get('password')

    if authenticate_user(input_username, input_password):
      flash("Login Successful")
      print("AUTHENTICATED")
    else:
      flash("Login Successful")
      print("ACCESS  DENIED FOR " + str(input_username))


    return render_template('login.html')
  else:
    return render_template('login.html')



