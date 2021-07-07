import os
from flask import render_template, request, session
from flask_login import login_required
from . import app
from .cookie_utils import save_input, load_input, get_all_inputs, delete_input, load_save_store_inputs
from .api_interaction import api
from .models.get_endpoints import get_endpoints
from .models.get_fields import get_fields
from .models.get_addresses import get_addresses
import json


page_name =  'typeahead'

@login_required
@app.route(f'/{page_name}', methods=['GET', 'POST'])
def typeahead():

  if request.method == 'GET':
    delete_input(session)
    return render_template(
        f'{page_name}.html',
        searchable_fields=get_fields(page_name),
        endpoints=get_endpoints(called_from=page_name),
    )

  searchable_fields = get_fields(page_name)
  all_user_input = load_save_store_inputs(searchable_fields,request,session,)


  result = api(
      '/addresses/uprn/',
      page_name,
      all_user_input.get(page_name),
  )

  if result.status_code == 200:
    matched_addresses = get_addresses(result.json(),page_name)
  else:
    matched_addresses = ''

  return render_template(
      f'{page_name}.html',
      endpoints=get_endpoints(called_from=page_name),
      searchable_fields=searchable_fields,
      results_page=True,
      matched_addresses=matched_addresses,
  )
