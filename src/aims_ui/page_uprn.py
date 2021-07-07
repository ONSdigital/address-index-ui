import os
from flask import render_template, request, session
from flask_login import login_required
from . import app
from .cookie_utils import save_input, load_input, get_all_inputs, delete_input
from .api_interaction import api
from .models.get_endpoints import get_endpoints
from .models.get_fields import get_fields
import json


@login_required
@app.route('/uprn', methods=['GET', 'POST'])
def uprn():

  if request.method == 'GET':
    delete_input(session)
    return render_template(
        'uprn.html',
        searchable_fields=get_fields('uprn'),
        endpoints=get_endpoints(),
        matched_addresses=[1, 2, 3, 4, 5],  # REMOVE THIS
    )

  searchable_fields = get_fields('uprn')

  # Dic of {'API name / HTML ID' : User Input }
  all_user_input = get_all_inputs(searchable_fields, request)
  print(all_user_input)

  # Save all_user_input into session
  save_input(all_user_input, session)

  # Load any previous values into the searchfields
  load_input(all_user_input, session, searchable_fields)

  uprn_result = api(
      '/addresses/uprn/',
      'uprn',
      all_user_input.get('uprn'),
  )

  print(uprn_result.json())
  uprn_result = 'Blank'

  return render_template(
      'uprn.html',
      endpoints=get_endpoints(),
      searchable_fields=searchable_fields,
      uprn_result=uprn_result,
      results_page=True,
      matched_addresses=[1, 2, 3, 4, 5],
  )
