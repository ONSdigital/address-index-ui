from flask import render_template, request, session
from flask_login import login_required
import json

from aims_ui import app
from aims_ui.models.get_addresses import get_addresses
from aims_ui.models.get_endpoints import get_endpoints
from aims_ui.models.get_fields import get_fields
from aims_ui.page_helpers.api.api_interaction import api, get_api_auth
from aims_ui.page_helpers.cookie_utils import delete_input, load_save_store_inputs, save_epoch_number
from aims_ui.page_helpers.error.error_utils import error_page_api_request, error_page_api_response
from aims_ui.page_helpers.pages_location_utils import get_page_location
from aims_ui.page_helpers.security_utils import check_user_has_access_to_page
from aims_ui.models.utilities.sibling_lookup import multiple_uprn_lookup

page_name = 'typeahead2'


@login_required
@app.route(f'/{page_name}', methods=['GET', 'POST'])
def typeahead2():
  endpoints = get_endpoints(called_from=page_name)
  access = check_user_has_access_to_page(page_name)
  if access != True:
    return access
  page_location = get_page_location(endpoints, page_name)
  searchable_fields = get_fields(page_name)


  # We are expecting to be handed a list of level2 siblings from session:
  level2_siblings = session.get('level2_siblings', [])
  print('\n\n\n\n The following sibling UPRNS have been handed:')
  print(level2_siblings)
  print('\n\n\n\n\n\n\n')

  # Use the list of endpoints to get address info. Use the multi-uprn endpoint:
  child_addresses_response = multiple_uprn_lookup(level2_siblings)
  print('Child addresses retrieved from multiple UPRN lookup:')
  child_addresses_info = child_addresses_response.json().get('response').get('addresses')
  print(child_addresses_info)

  # Current limitation is you have to point the autosuggest at a js file, however this could be hosted on an endpoint. More work tho. 
  # Could potentially request a change to be able to override this by handing a json directly. 

  if request.method == 'GET':
    delete_input(session)


    return render_template(
        page_location,
        page_name=page_name,
        searchable_fields=searchable_fields,
        endpoints=get_endpoints(called_from=page_name),
        api_auth=get_api_auth(),
    )

  all_user_input = load_save_store_inputs(
      searchable_fields,
      request,
      session,
  )
  all_user_input['uprn'] = request.form.get('address-uprn')
  save_epoch_number(session, all_user_input.get('epoch', ''))

  try:
    result = api(
        '/addresses/uprn/',
        'uprn',
        all_user_input,
    )

  # Note that error handling here only deals with serverside connections
  # and does not handle client side errors with the typeahead component
  except Exception as e:
    return error_page_api_request(page_name, all_user_input, e)

  # Errors after sucessful Response
  if result.status_code != 200:
    return error_page_api_response(page_name, all_user_input, result)

  matched_addresses = get_addresses(result.json(), 'uprn')

  return render_template(
      page_location,
      page_name=page_name,
      endpoints=get_endpoints(called_from=page_name),
      searchable_fields=searchable_fields,
      results_page=True,
      matched_addresses=matched_addresses,
      matched_address_number=len(matched_addresses),
      api_auth=get_api_auth(),
  )