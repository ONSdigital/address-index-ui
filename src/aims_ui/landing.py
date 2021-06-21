import os
from . import app
from flask import render_template
from  flask_login import login_required

@login_required
@app.route('/landing')
def landing():


  return render_template('landing.html')
