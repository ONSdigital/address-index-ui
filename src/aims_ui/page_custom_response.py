from flask import render_template, request
from flask_login import login_required
from . import app
from .security_utils import detect_xml_injection
from .models.get_endpoints import get_endpoints
from .models.get_addresses import get_addresses
from .page_error import page_error
from .api_interaction import get_header
import json, requests

page_name = 'custom_response'


@login_required
@app.route(f'/{page_name}', methods=['GET', 'POST'])
def custom_response():

  if request.method == 'GET':
    return render_template(
        f'{page_name}.html',
        endpoints=get_endpoints(called_from=page_name),
    )

  base_url = app.config.get('API_URL') 
  api_url = base_url + request.form.get('url-input-autosuggest') # End of url, e.g. /addresses
  request_body = request.form.get('request-body-text-area') # Body of request
  request_type = request.form.get('request-type') # GET or POST

  header = get_header(request)

  try:
    if request_type == 'GET':
      r = requests.get(api_url, headers=header)
    elif request_type == 'POST':
      r = requests.post(api_url, headers=header, body=request_body)

    # If sucessful request (but maybe a bad request) check response code
    if r.status_code != 200:
      # Get details about the failed response
      json_response = r.json()
      status = json_response.get('status')
      errors = json_response.get('errors')
      errors_formatted = [
        {'text': f"Error {error['code']}. {error['message']}"} for error in errors ]
      return render_template(
        f'{page_name}.html',
        endpoints=get_endpoints(called_from=page_name),
        error_title=f"Status Code: {status.get('code')} - {status.get('message')}",
        errors_formatted=errors_formatted,
        show_error=True,
      )     

  except requests.exceptions.HTTPError as http_err:
    # Specific errors related to HTTP responses
    print(f"HTTP error occurred: {http_err}")
  except requests.exceptions.ConnectionError as conn_err:
    # Errors related to connecting to the server
    print(f"Connection error occurred: {conn_err}")
  except requests.exceptions.Timeout as timeout_err:
    # Timeout errors
    print(f"Timeout error occurred: {timeout_err}")
  except requests.exceptions.RequestException as req_err:
    # Catch-all for any request-related error
    print(f"An error occurred: {req_err}")


  plaintext_response = r.json()
  formatted_text_response = json.dumps(plaintext_response, indent=2)
  if r.status_code != 200:
    return page_error(r, page_name)
  matched_addresses = get_addresses(r.json(), page_name)

  return render_template(
      f'{page_name}.html',
      endpoints=get_endpoints(called_from=page_name),
      formatted_text_response=formatted_text_response,
      matched_addresses=matched_addresses,
      matched_address_number=len(matched_addresses),
      results_page=True,
  )
