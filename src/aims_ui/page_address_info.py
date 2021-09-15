import os
from . import app
from .models.get_endpoints import get_endpoints
from .api_interaction import api
from .table_utils import create_table
from .models.get_addresses import get_addresses
from requests.exceptions import ConnectionError
from flask import render_template
from flask_login import login_required
import json


@login_required
@app.route('/address_info/<uprn>')
def address_info(uprn):
  """Show all info about an address given the UPRN"""

  try:
    result = api(
        '/addresses/uprn/',
        'uprn',
        {'uprn': uprn},
    )

  except ConnectionError as e:
    return page_error(None, e, page_name)

  if result.status_code == 200:
    matched_addresses = get_addresses(result.json(), 'uprn')
  elif result.status_code == 404:
    # No results but the api compelted the call successfully
    matched_addresses = ''
  else:
    return page_error(result, page_name)

  # Clerical headers will always be constant
  ths = ['Name', 'Value']
  trs = []
  special_responses = ['paf', 'nag']
  # Create clerical info, from endpoints
  for attribute_name, address_attribute in matched_addresses[0].__dict__.items(
  ):
    if attribute_name in special_responses:
      for nag_name, nag_attribute in address_attribute.value.__dict__.items():
        if nag_name in address_attribute.value.clerical_values:
          trs.append([f'[{attribute_name}]  ' + nag_name, nag_attribute.value])

    trs.append([attribute_name, address_attribute.value])

  return render_template(
      'address_info.html',
      endpoints=get_endpoints(),
      matched_addresses=matched_addresses,
      clerical_info=create_table(ths, trs),
  )
