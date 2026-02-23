from flask import render_template, session
from flask_login import login_required
from requests.exceptions import ConnectionError

from aims_ui import app
from aims_ui.models.get_addresses import get_addresses
from aims_ui.models.get_endpoints import get_endpoints
from aims_ui.page_controllers.f_error_pages.page_error import page_error
from aims_ui.page_helpers.api.api_interaction import api
from aims_ui.page_helpers.cookie_utils import load_epoch_number
from aims_ui.page_helpers.pages_location_utils import get_page_location_non_endpoint
from aims_ui.page_helpers.table_utils import create_hierarchy_table, create_table

page_name = 'address_info'


@login_required
@app.route('/address_info/<uprn>')
def address_info(uprn):
  """Show all info about an address given the UPRN"""
  endpoints = get_endpoints(called_from=page_name)
  epoch_version_number = load_epoch_number(session)
  page_location = get_page_location_non_endpoint(page_name)

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

  link_data = [
      {
          'attribute_name': 'confidence_score',
          'url': '/help/confidence_score',
      },
  ]

  return render_template(
      page_location,
      endpoints=endpoints,
      page_name=page_name,
      matched_addresses=matched_addresses,
      clerical_info=clerical_info,
      hierarchy_table=hierarchy_table,
      link_data=link_data,
  )
