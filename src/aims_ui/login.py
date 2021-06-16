import os
from . import app
from flask import render_template, request
import sqlite3
import hashlib, binascii, os

@app.route('/auth/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':

    con = sqlite3.connect('./aims_ui/testing_resources/auth.db')
    cur = con.cursor()

    def get_pass(uname):
      for hashed_password in cur.execute ('SELECT password FROM USERS WHERE username=?', (uname,) )  :
        return hashed_password[0]

    username = request.form.get('username')
    input_password = request.form.get('password')
    stored_password = get_pass(username)

    def verify_password(stored_password, provided_password):
      """Verify a stored password against one provided by user"""
      salt = stored_password[:64]
      stored_password = stored_password[64:]
      pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                provided_password.encode('utf-8'), 
                                salt.encode('ascii'), 
                                100000)
      pwdhash = binascii.hexlify(pwdhash).decode('ascii')
      return pwdhash == stored_password

    print('Password Correct?:  ' )
    print(verify_password(stored_password, input_password))

    con.close()


    return render_template('login.html')
  else:
    return render_template('login.html')



