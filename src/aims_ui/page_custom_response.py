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

  if request_type == 'GET':
    r = requests.get(
        api_url,
        headers=header,
    )

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
  )
