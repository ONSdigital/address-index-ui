import os
from flask import render_template, request, session
from requests.exceptions import ConnectionError
from flask_login import login_required
from . import app
from .cookie_utils import save_input, load_input, get_all_inputs, delete_input, load_save_store_inputs, save_epoch_number
from .api_interaction import api
from .security_utils import detect_xml_injection
from .models.get_endpoints import get_endpoints
from .models.get_fields import get_fields
from .models.get_addresses import get_addresses
from .page_error import page_error
import json

page_name = 'custom_response'


@login_required
@app.route(f'/{page_name}', methods=['GET', 'POST'])
def custom_response():

  if request.method == 'GET':
    delete_input(session)
    search_uprn = request.args.get('search_uprn')
    return render_template(
        f'{page_name}.html',
        searchable_fields=get_fields('uprn',
                                     include_UPRN_redirect=search_uprn),
        endpoints=get_endpoints(called_from=page_name),
    )

  print(request.form)
  print(request.form.get('uprn'))

  return render_template(
      f'{page_name}.html',
      endpoints=get_endpoints(called_from='uprn'),
      searchable_fields=get_fields('uprn'),
  )


