import os
from . import app
from .models.get_endpoints import get_endpoints
from .api_interaction import api
from .table_utils import create_table, create_hierarchy_table
from .models.get_addresses import get_addresses
from requests.exceptions import ConnectionError
from flask import render_template
from flask_login import login_required
import dataclasses
from .models.address import Address
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
  # All attributes of 'Address' are added to the table
  for attribute_name, address_attribute in matched_addresses[0].__dict__.items(
  ):
    if attribute_name != 'hierarchy':
      if attribute_name in special_responses:
        for nag_name, nag_attribute in address_attribute.value.__dict__.items(
        ):
          if nag_name in address_attribute.value.clerical_values:
            trs.append(
                [f'[{attribute_name}]  ' + nag_name, nag_attribute.value])
    else:
      # If attribute name is 'hierarchy'
      if address_attribute.value != None:
        hierarchy_table = create_hierarchy_table(address_attribute.value)


    trs.append([attribute_name, address_attribute.value])

  to_hide = [
      'hierarchy',
      'formatted_confidence_score',
      'paf',
      'nag',
  ]

  # Remove hierarchy info from clerical data
  final_trs = [x if x[0] not in to_hide else '' for x in trs]

  clerical_info = create_table(ths, final_trs)

  return render_template(
      'address_info.html',
      endpoints=get_endpoints('address_info'),
      matched_addresses=matched_addresses,
      clerical_info=clerical_info,
      hierarchy_table=hierarchy_table,
  )
