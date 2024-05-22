import os
from flask import render_template, request, session
from flask_login import login_required
from . import app
from requests.exceptions import ConnectionError
from aims_ui.page_helpers.cookie_utils import save_input, load_input, get_all_inputs, delete_input, load_save_store_inputs, save_epoch_number
from aims_ui.page_helpers.api.api_interaction import api
from aims_ui.page_helpers.security_utils import detect_xml_injection, check_user_has_access_to_page
from aims_ui.models.get_endpoints import get_endpoints
from aims_ui.models.get_fields import get_fields
from aims_ui.models.get_addresses import get_addresses
from aims_ui.page_error import page_error
import json

page_name = 'postcode'
pages_location = app.config.get('AIMS_UI_PAGES_LOCATION', '')


@login_required
@app.route(f'/{page_name}', methods=['GET', 'POST'])
def postcode():
  endpoints = get_endpoints(called_from=page_name)
  access = check_user_has_access_to_page(page_name, endpoints)
  if access != True:
    return access

  if request.method == 'GET':
    delete_input(session)
    return render_template(
        f'{pages_location}{page_name}.html',
        searchable_fields=get_fields(page_name),
        endpoints=endpoints,
    )

  searchable_fields = get_fields(page_name)
  all_user_input = load_save_store_inputs(
      searchable_fields,
      request,
      session,
  )

  user_input = all_user_input.get('postcode', '')
  xml_injection = detect_xml_injection(user_input)
  if xml_injection:
    return page_error(None,
                      page_name,
                      all_user_input,
                      override_error_description=
                      'XML Attack Detected. This incident will be reported.')
  try:
    result = api(
        '/addresses/postcode/',
        page_name,
        all_user_input,
    )

  except ConnectionError as e:
    return page_error(None, e, page_name)

  if result.status_code == 200:
    matched_addresses = get_addresses(result.json(), page_name)
  elif result.status_code == 404:
    # No results but the api compelted the call successfully
    matched_addresses = ''
  else:
    return page_error(result, page_name)

  # Save epoch
  save_epoch_number(session, all_user_input.get('epoch', ''))

  return render_template(
      f'{pages_location}{page_name}.html',
      endpoints=endpoints,
      searchable_fields=searchable_fields,
      results_page=True,
      matched_addresses=matched_addresses,
      matched_address_number=len(matched_addresses),
  )
