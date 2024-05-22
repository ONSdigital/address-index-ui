import json, requests
from flask import render_template, request
from flask_login import login_required
from aims_ui import app
from aims_ui.page_helpers.api.api_helpers import get_header
from aims_ui.page_helpers.security_utils import detect_xml_injection, check_user_has_access_to_page
from aims_ui.models.get_endpoints import get_endpoints
from aims_ui.models.get_addresses import get_addresses
from aims_ui.page_error import page_error

page_name = 'custom_response'
pages_location = app.config.get('AIMS_UI_PAGES_LOCATION', '')


def return_error_to_custom_response(error_title, errors_formatted,
                                    r_json_readable):
  return render_template(
      f'{page_name}.html',
      endpoints=get_endpoints(called_from=page_name),
      error_title=error_title,
      errors_formatted=errors_formatted,
      r_json_readable=r_json_readable,
  )


@login_required
@app.route(f'/{page_name}', methods=['GET', 'POST'])
def custom_response():
  endpoints = get_endpoints(called_from=page_name)
  access = check_user_has_access_to_page(page_name, endpoints)
  if access != True:
    return access

  if request.method == 'GET':
    return render_template(
        f'{page_name}.html',
        endpoints=get_endpoints(called_from=page_name),
    )

  base_url = app.config.get('API_URL')
  api_url = base_url + request.form.get(
      'url-input-autosuggest')  # End of url, e.g. /addresses
  request_body = request.form.get('request-body-text-area')  # Body of request
  request_type = request.form.get('request-type')  # GET or POST

  header = get_header()

  try:
    if request_type == 'GET':
      r = requests.get(api_url, headers=header)
    elif request_type == 'POST':
      r = requests.post(api_url,
                        headers=header,
                        data=request_body.encode('utf-8'))

    # Get the json response and formatted version for user output
    r_json = r.json()
    r_json_readable = json.dumps(r_json, indent=2)

    # If sucessful request (but maybe a bad request) check response code
    if r.status_code != 200:
      # Get details about the failed response

      status = r_json.get('status')
      error_title = f"Status Code: {status.get('code')} - {status.get('message')}"

      errors = r_json.get('errors', 'NA')
      if errors != 'NA':
        errors_formatted = [{
            'text':
            f"Error {error['code']}. {error['message']}"
        } for error in errors]
        return return_error_to_custom_response(error_title, errors_formatted,
                                               r_json_readable)
      else:
        return return_error_to_custom_response(error_title,
                                               [{
                                                   'text': 'Error in request'
                                               }], r_json_readable)

  except requests.exceptions.HTTPError as http_err:
    errors_formatted = [{'text': 'Error in HTTP response'}]
    return return_error_to_custom_response('HTTP error occured',
                                           errors_formatted,
                                           'No Response from Server')
  except requests.exceptions.ConnectionError as conn_err:
    errors_formatted = [{'text': 'Error Connecting to Server'}]
    return return_error_to_custom_response('Connection Error',
                                           errors_formatted,
                                           'No Response from Server')
  except requests.exceptions.Timeout as timeout_err:
    errors_formatted = [{
        'text':
        'A timeout has occured. Retrying might fix this'
    }]
    return return_error_to_custom_response('Timeout Error', errors_formatted,
                                           'No Response from Server')
  except requests.exceptions.RequestException as req_err:
    errors_formatted = [{'text': str(req_err)}]
    return return_error_to_custom_response('Unknown Error', errors_formatted,
                                           'No Response from Server')

  # Check to see if response actually contains addresses:
  matched_addresses = []
  if 'response' in r_json:
    r_resp = r_json.get('response')
    if ('addresses' in r_resp):
      matched_addresses = get_addresses(r_json, page_name)
    elif ('address' in r_resp):
      matched_addresses = get_addresses(r_json, 'uprn')

  return render_template(
      f'{pages_location}{page_name}.html',
      endpoints=get_endpoints(called_from=page_name),
      r_json_readable=r_json_readable,
      matched_addresses=matched_addresses,
      matched_address_number=len(matched_addresses),
      results_page=True,
  )
