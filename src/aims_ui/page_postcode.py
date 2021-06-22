import os
from . import app
from flask import render_template, request
from flask_login import login_required
from .models.get_endpoints import get_endpoints

@login_required
@app.route('/postcode', methods=['GET', 'POST'])
def postcode():

  if request.method =='POST':
    print(request)


  return render_template('postcode.html' )
