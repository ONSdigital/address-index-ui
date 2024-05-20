import dataclasses
import json
import os
import urllib.request
from . import app
from .models.get_endpoints import get_endpoints
from .api_interaction import api
from .page_error import page_error
from .table_utils import create_table, create_hierarchy_table
from .models.get_addresses import get_addresses
from .cookie_utils import load_epoch_number
from .models.address import Address
from requests.exceptions import ConnectionError
from flask import render_template, request, session
from flask_login import login_required
from aims_ui import get_cached_tooltip_data

page_name = 'address_info'
pages_location = app.config.get('AIMS_UI_PAGES_LOCATION', '')


@login_required
@app.route('/address_info/<uprn>')
def address_info(uprn):
  """Show all info about an address given the UPRN"""
  endpoints = get_endpoints(called_from=page_name)
  epoch_version_number = load_epoch_number(session)

  try:
    result = api(
        '/addresses/uprn/',
        'uprn',
        {
            'uprn': uprn,
            'epoch': epoch_version_number
        },
    )

  except ConnectionError as e:
    return page_error(None, e, page_name)

  if result.status_code == 200:
    matched_addresses = get_addresses(result.json(),
                                      'uprn',
                                      underlying_score=0,
                                      confidence_score=0)
  elif result.status_code == 404:
    # No results but the api compelted the call successfully
    return page_error(result, 'Detailed Information')
  else:
    return page_error(result, 'Detailed Information')

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

  tool_tip_data = get_cached_tooltip_data()
  link_data = [
      {
          'attribute_name': 'confidence_score',
          'url': '/help/confidence_score',
      },
  ]

  return render_template(
      f'{pages_location}{page_name}.html',
      endpoints=endpoints,
      matched_addresses=matched_addresses,
      clerical_info=clerical_info,
      hierarchy_table=hierarchy_table,
      tool_tip_data=tool_tip_data,
      link_data=link_data,
  )
