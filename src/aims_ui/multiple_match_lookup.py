import json
from io import StringIO, BytesIO
from aims_ui.api_interaction import api, submit_mm_job
import csv
from .models.get_endpoints import get_endpoints
from .models.get_addresses import get_addresses
from .page_error import page_error
import logging

page_name = 'multiple_match_submit'

def remove_header_row(contents):
  remove_index = None
  for i in range(0, len(contents)):
    line = contents[i]
    line = line.strip().decode('utf-8')
    if (line.casefold() == 'id,address'.casefold()) or (line.casefold() == 'id,searchAddress'.casefold()):
      remove_index = i

  if remove_index != None:
    contents.pop(remove_index)

def multiple_address_match(file, all_user_input, download=False):
  csv_headers = ['id', 'inputAddress', 'matchedAddress', 'uprn', 'matchType', 'confidenceScore', 'documentScore', 'rank']  # yapf: disable

  contents = file.readlines()
  remove_header_row(contents)

  mm_dict = {} # mm = multiple match
  addresses = []
  for line in contents:
    line = line.strip().decode('utf-8')
    given_id, address_to_lookup = line.split(',', maxsplit=1)
    current_address = {'id': given_id, 'address': address_to_lookup}
    addresses.append(current_address)
  mm_dict['addresses'] = addresses[:]
  
  submit_mm_job('a',mm_dict)
  try:
    # Submit Multiple Match to API
    submit_mm_job('a',mm_dict)
  except Exception as e:
    logging.error('Error on a multiple match API call')
    return page_error(None, e, page_name)

