import os
from flask import render_template, request
from flask_login import login_required
from . import app
from .api_interaction import api
from .models.get_endpoints import get_endpoints
from .models.get_endpoints import get_endpoints

@login_required
@app.route('/uprn', methods=['GET', 'POST'])
def uprn():

  if request.method =='GET':
    return render_template('uprn.html', endpoints = get_endpoints() )

  response = api('/addresses/uprn/',{'uprn':request.form.get('uprn_input')},)
  print(response)



  return render_template('uprn.html', 
      endpoints = get_endpoints(),
      uprn_result = '',

      )
    


