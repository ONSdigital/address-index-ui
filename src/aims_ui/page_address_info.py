import os
from . import app
from .models.get_endpoints import get_endpoints
from .api_interaction import api
from .models.get_addresses import get_addresses
from flask import render_template
from flask_login import login_required
import json


@login_required
@app.route('/address_info/<uprn>')
def address_info(uprn):
  """Show all info about an address given the UPRN"""

  result = api(
      '/addresses/uprn/',
      'uprn',
      {'uprn': uprn},
  )

  if result.status_code == 200:
    matched_addresses = get_addresses(result.json(), 'uprn', app)
  elif result.status_code == 404:
    # No results but the api compelted the call successfully
    matched_addresses = ''
  else:
    return page_error(result, page_name)

  return render_template(
      'address_info.html',
      endpoints=get_endpoints(),
      matched_addresses=matched_addresses,
  )
