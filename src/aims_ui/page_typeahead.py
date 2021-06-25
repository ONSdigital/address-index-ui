import os
from . import app
from flask import render_template, request
from flask_login import login_required
from .models.get_endpoints import get_endpoints
from .models.get_endpoints import get_endpoints

@login_required
@app.route('/typeahead', methods=['GET', 'POST'])
def typeahead():

  if request.method =='POST':
    print(request)


  return render_template('typeahead.html', endpoints = get_endpoints())
