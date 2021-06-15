import os
from . import app
from flask import render_template

@app.route('/auth/login')
def login():


  return render_template('login.html')
