from flask import render_template, request, session
from flask_login import login_required

from aims_ui import app
from aims_ui.models.get_addresses import get_addresses
from aims_ui.models.get_endpoints import get_endpoints
from aims_ui.models.get_fields import get_fields
from aims_ui.page_helpers.api.api_interaction import api, get_response_attributes
from aims_ui.page_helpers.cookie_utils import delete_input, load_save_store_inputs, save_epoch_number
from aims_ui.page_helpers.error.error_utils import error_page_api_request, error_page_api_response, error_page_xml
from aims_ui.page_helpers.pages_location_utils import get_page_location
from aims_ui.page_helpers.security_utils import check_user_has_access_to_page, detect_xml_injection
from aims_ui.page_helpers.validation_utils import validate_limit
from aims_ui.page_controllers.f_error_pages.page_error_annotation_single import page_error_annotation_single

page_name = 'singlesearch'


@login_required
@app.route(f'/', methods=['GET', 'POST'])
def singlesearch():
  endpoints = get_endpoints(called_from=page_name)
  access = check_user_has_access_to_page(page_name)
  if access != True:
    return access
  page_location = get_page_location(endpoints, page_name)
  searchable_fields = get_fields(page_name)

  if request.method == 'GET':
    delete_input(session)
    return render_template(
        page_location,
        searchable_fields=searchable_fields,
        endpoints=endpoints,
    )

  all_user_input = load_save_store_inputs(
      searchable_fields,
      request,
      session,
  )

  user_input = all_user_input.get('input', '')
  xml_injection = detect_xml_injection(user_input)
  if xml_injection:
    return error_page_xml(page_name, user_input)

  # limit_invalid is none or the error message
  limit = all_user_input.get('limit', 1)
  limit_invalid = validate_limit(limit)
  if limit_invalid:
    return page_error_annotation_single(page_name, user_input, limit_invalid)

  try:
    result = api(
        '/addresses',
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
      page_location,
      endpoints=endpoints,
      searchable_fields=searchable_fields,
      results_page=True,
      matched_addresses=matched_addresses,
      matched_address_number=len(matched_addresses),
      responseAttributes=responseAttributes,
  )
