import os
import json
from flask import render_template, request, session
from flask_login import login_required
from requests.exceptions import ConnectionError
from . import app
from .cookie_utils import save_input, load_input, get_all_inputs, delete_input, load_save_store_inputs, save_epoch_number
from .api_interaction import api, get_response_attributes
from .security_utils import detect_xml_injection, check_user_has_access_to_page
from .models.get_endpoints import get_endpoints
from .models.get_fields import get_fields
from .models.get_addresses import get_addresses
from .page_error import page_error

page_name = 'singlesearch'


@login_required
@app.route(f'/', methods=['GET', 'POST'])
def singlesearch():
  endpoints = get_endpoints(called_from=page_name)
  access = check_user_has_access_to_page(page_name, endpoints)
  if access != True:
    return access

  if request.method == 'GET':
    delete_input(session)
    return render_template(
        f'{page_name}.html',
        searchable_fields=get_fields(page_name),
        endpoints=endpoints,
    )

  searchable_fields = get_fields(page_name)
  all_user_input = load_save_store_inputs(
      searchable_fields,
      request,
      session,
  )

  user_input = all_user_input.get('input', '')
  xml_injection = detect_xml_injection(user_input)
  if xml_injection:
    return page_error(None,
                      page_name,
                      all_user_input,
                      override_error_description=
                      'XML Attack Detected. This incident will be reported.')

  try:
    result = api(
        '/addresses',
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

  # Save a list of UPRNs and their respective confidence scores
  save_epoch_number(session, all_user_input.get('epoch', ''))

  # Check to see if showing the comfortable redirect is appropriate
  ss_input = all_user_input.get('input')
  if ss_input.isdigit():
    searchable_fields = get_fields(page_name, include_UPRN_redirect=ss_input)
    all_user_input = load_save_store_inputs(
        searchable_fields,
        request,
        session,
    )

  # Get the attributes of the Response a user might want
  responseAttributes = get_response_attributes(result.json())

  return render_template(
      f'{page_name}.html',
      endpoints=endpoints,
      searchable_fields=searchable_fields,
      results_page=True,
      matched_addresses=matched_addresses,
      matched_address_number=len(matched_addresses),
      responseAttributes=responseAttributes,
  )
