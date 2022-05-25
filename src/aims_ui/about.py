import os
from . import app
from flask import render_template
from flask_login import login_required
from .models.get_endpoints import get_endpoints


@login_required
@app.route('/about')
def about():

  return render_template('about.html', endpoints=get_endpoints())
