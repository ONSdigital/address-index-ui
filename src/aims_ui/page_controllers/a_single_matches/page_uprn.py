from flask import render_template, request, session
from requests.exceptions import ConnectionError
from flask_login import login_required
from aims_ui import app
from aims_ui.page_helpers.cookie_utils import delete_input, load_save_store_inputs, save_epoch_number
from aims_ui.page_helpers.api.api_interaction import api
from aims_ui.page_helpers.security_utils import detect_xml_injection, check_user_has_access_to_page
from aims_ui.page_helpers.pages_location_utils import get_page_location
from aims_ui.page_helpers.error.error_utils import error_page_xml, error_page_api_request, error_page_api_response
from aims_ui.models.get_endpoints import get_endpoints
from aims_ui.models.get_fields import get_fields
from aims_ui.models.get_addresses import get_addresses
from aims_ui.page_error import page_error

page_name = 'uprn'


@login_required
@app.route(f'/{page_name}', methods=['GET', 'POST'])
def uprn():
  endpoints = get_endpoints(called_from=page_name)
  access = check_user_has_access_to_page(page_name)
  if access != True:
    return access
  page_location = get_page_location(endpoints, page_name)

  if request.method == 'GET':
    delete_input(session)
    search_uprn = request.args.get('search_uprn')
    return render_template(
        page_location,
        searchable_fields=get_fields(page_name,
                                     include_UPRN_redirect=search_uprn),
        endpoints=endpoints,
    )

  searchable_fields = get_fields(page_name)
  all_user_input = load_save_store_inputs(
      searchable_fields,
      request,
      session,
  )

  user_input = all_user_input.get('uprn', '')
  xml_injection = detect_xml_injection(user_input)
  if xml_injection:
    return error_page_xml(page_name, user_input)

  try:
    result = api(
        '/addresses/uprn/',
        page_name,
        all_user_input,
    )

  # Deal with errors connecting to the API
  except Exception as e:
    return error_page_api_request(page_name, user_input, e)

  # Errors after sucessful Response
  if result.status_code != 200:
    return error_page_api_response(page_name, user_input, result)

  matched_addresses = get_addresses(result.json(), page_name)

  # Save epoch number
  save_epoch_number(session, all_user_input.get('epoch', ''))

  return render_template(
      page_location,
      endpoints=endpoints,
      searchable_fields=searchable_fields,
      results_page=True,
      matched_addresses=matched_addresses,
      matched_address_number=len(matched_addresses),
  )
