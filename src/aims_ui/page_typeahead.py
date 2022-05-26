import os
from flask import render_template, request, session
from flask_login import login_required
from . import app
from requests.exceptions import ConnectionError
from .cookie_utils import save_input, load_input, get_all_inputs, delete_input, load_save_store_inputs
from .api_interaction import api, get_api_auth
from .models.get_endpoints import get_endpoints
from .models.get_fields import get_fields
from .models.get_addresses import get_addresses
import json

page_name = 'typeahead'


@login_required
@app.route(f'/{page_name}', methods=['GET', 'POST'])
def typeahead():

  if request.method == 'GET':
    delete_input(session)

    return render_template(
        f'{page_name}.html',
        searchable_fields=get_fields(page_name),
        endpoints=get_endpoints(called_from=page_name),
        api_auth=get_api_auth(),
    )

  searchable_fields = get_fields(page_name)
  all_user_input = load_save_store_inputs(
      searchable_fields,
      request,
      session,
  )
  all_user_input['uprn'] = request.form.get('address-uprn')
  print(all_user_input)

  try:
    result = api(
        '/addresses/uprn/',
        'uprn',
        all_user_input,
    )

  except ConnectionError as e:
    return page_error(None, e, page_name)

  if result.status_code == 200:
    matched_addresses = get_addresses(result.json(), 'uprn')
  else:
    matched_addresses = ''

  return render_template(
      f'{page_name}.html',
      endpoints=get_endpoints(called_from=page_name),
      searchable_fields=searchable_fields,
      results_page=True,
      matched_addresses=matched_addresses,
      matched_address_number=len(matched_addresses),
      api_auth=get_api_auth(),
  )

