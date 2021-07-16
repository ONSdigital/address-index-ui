import os
from . import app, get_db
from flask_login import current_user, login_user
from .models.user_model import User
from .models.get_endpoints import get_endpoints
from flask import (
    render_template,
    request,
    flash,
    abort,
    redirect,
    url_for,
)

import sqlite3
import hashlib, binascii, os


@app.route('/', methods=['GET', 'POST'])
def login():

  if request.method == 'POST':

    username = request.form.get('username')
    password = request.form.get('password')

    user = User()
    if user.is_authenticated(username, password, get_db().cursor()):

      login_user(user)

      flash('Logged in successfully.')
      return redirect(url_for('landing'))

  return render_template('login.html',
                         endpoints=get_endpoints(),
                         remove_nav=True)
