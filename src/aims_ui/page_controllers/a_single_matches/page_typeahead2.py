from flask import render_template, request, session
from flask_login import login_required
import os

import json

from aims_ui import app
from aims_ui.models.get_endpoints import get_endpoints
from aims_ui.models.get_fields import get_fields
from aims_ui.page_helpers.api.api_interaction import get_api_auth
from aims_ui.page_helpers.cookie_utils import delete_input
from aims_ui.page_helpers.pages_location_utils import get_page_location
from aims_ui.page_helpers.security_utils import check_user_has_access_to_page
from aims_ui.models.utilities.sibling_lookup import multiple_uprn_lookup

page_name = 'typeahead2'

def format_addresses_for_sub_typeahead(address_info):
  # Take just the name and the uprn and format into objects like this: 
  # { 'en': Address Name, 'uprn': UPRN } 
  formatted_addresses = []
  for address in address_info:
    formatted_addresses.append({
        'en': address.get('formattedAddress'),
        'uprn': address.get('uprn')
    })
  return formatted_addresses

@login_required
@app.route(f'/{page_name}', methods=['GET', 'POST'])
def typeahead2():
  endpoints = get_endpoints(called_from=page_name)
  access = check_user_has_access_to_page(page_name)
  if access != True:
    return access
  page_location = get_page_location(endpoints, page_name)
  searchable_fields = get_fields(page_name)


  if request.method == 'GET':
    # We are expecting to be handed a list of level2 siblings from session:
    level2_siblings = session.get('level2_siblings', [])
    print('\n\n\n\n The following sibling UPRNS have been handed:')
    print(level2_siblings)
    print('\n\n\n\n\n\n\n')

    # Use the list of endpoints to get address info. Use the multi-uprn endpoint:
    child_addresses_response = multiple_uprn_lookup(level2_siblings)
    child_addresses_info = child_addresses_response.json().get('response').get('addresses')

    addresses_in_typeahead_format = format_addresses_for_sub_typeahead(child_addresses_info)
    print(f'\nAddresses in typeahead format: {addresses_in_typeahead_format}\n\n\n\n')

    # Write the formatted addresses into test_for_typeahead_child_addresses.json
    file_path = os.path.join(app.static_folder, 'downloads', 'test_for_typeahead_child_addresses.json')
    with open(file_path, 'w', encoding='utf-8') as f:
      json.dump(addresses_in_typeahead_format, f)

    delete_input(session)
  else:
    print(request.form.get('url-input-autosuggest', ''))

  return render_template(
      page_location,
      page_name=page_name,
      endpoints=get_endpoints(called_from=page_name),
      searchable_fields=searchable_fields,
      api_auth=get_api_auth(),
  )