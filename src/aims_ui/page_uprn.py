import os
from . import app
from flask import render_template
from flask_login import login_required
from .models.get_endpoints import get_endpoints

@login_required
@app.route('/uprn')
def uprn():


  return render_template('uprn.html' )
