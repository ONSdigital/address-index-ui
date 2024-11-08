import logging

from aims_ui.page_controllers.b_multiple_matches.utils.multiple_match_utils import jsonify_address, remove_header_row
from aims_ui.page_controllers.f_error_pages.page_error import page_error
from aims_ui.page_helpers.api.api_interaction import submit_mm_job

page_name = 'multiple_match_submit'


def multiple_address_match(file, all_user_input, download=False):
  # Process the uploaded file from th euser
  contents = file.readlines()
  remove_header_row(contents)

  mm_dict = {}  # mm = multiple match
  addresses = []
  for line in contents:
    line = line.strip().decode('utf-8')
    given_id, address_to_lookup = line.split(',', maxsplit=1)
    address_to_lookup = jsonify_address(address_to_lookup)
    current_address = {'id': given_id, 'address': address_to_lookup}
    addresses.append(current_address)
  mm_dict['addresses'] = addresses[:]

  try:
    # Submit Multiple Match to API
    submit_mm_job('a', mm_dict, all_user_input)
  except Exception as e:
    logging.error('Error on a multiple match API call')
    return page_error(None, e, 'multiple_address')
