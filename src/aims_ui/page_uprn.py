import os
from flask import render_template, request
from flask_login import login_required
from . import app
from .api_interaction import api
from .models.get_endpoints import get_endpoints
from .models.get_fields import get_fields
import json

@login_required
@app.route('/uprn', methods=['GET', 'POST'])
def uprn():

  if request.method == 'GET':
    return render_template(
        'uprn.html',
        searchable_fields=get_fields('uprn'),
        endpoints=get_endpoints(),
    )

  def get_val(value_html_id):
    return request.form.get(value_html_id)

  num_addresses = get_val('num_address')
  include_aux = get_val('include_aux')
  classification = get_val('classification')
  inc_historical_address_data = get_val('inc_historical_address_data')
  epoch = get_val('epoch')
  uprn_input = get_val('uprn')

  uprn_result = api(
      '/addresses/uprn/',
      'uprn',
      uprn_input, )

  print(uprn_result.json())


  return render_template(
      'uprn.html',
      endpoints=get_endpoints(),
      serchable_fields=get_fields('uprn'),
      uprn_result=uprn_result,
      results_page=True,
  )
