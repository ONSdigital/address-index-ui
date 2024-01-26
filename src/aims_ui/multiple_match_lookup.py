import json
from io import StringIO, BytesIO
from aims_ui.api_interaction import api, submit_mm_job, submit_uprn_mm_job, get_response_attributes
import csv
from .models.get_endpoints import get_endpoints
from .models.get_addresses import get_addresses
from .upload_utils import remove_script_and_html_from_str
from .page_error import page_error
import logging

page_name = 'multiple_match_submit'


def get_preffered_format_of_address(adrs, all_user_input):
  address_prefference = all_user_input.get('paf-nag-prefference', 'default')
  default_address = adrs.formatted_address.value
  paf_address = adrs.formatted_address_paf.value
  nag_address = adrs.formatted_address_nag.value

  if address_prefference == 'PAF':
    if paf_address != '':
      return 'PAF', paf_address
  elif address_prefference == 'NAG':
    if nag_address != '':
      return 'NAG', nag_address
  # Default Addresses are all NAG
  return 'NAG', default_address


def remove_header_row(contents):
  # Remove these header rows (if they exist, there may be no header row)
  header_rows = ['id,address', 'id,searchAddress', '<feff>id,address']
  remove_index = None
  for i in range(0, len(contents)):
    line = contents[i]
    line = line.strip().decode('utf-8')
    line = line.casefold()
    # Remove utf8-sig Byte Object Mark
    line = line.replace('\ufeff', '')
    for header_row in header_rows:
      if line == header_row.casefold():
        remove_index = i

  if remove_index != None:
    contents.pop(remove_index)


def jsonify_address(address_to_lookup):
  # If the address contains a "'" character then contain the address
  if "'" in address_to_lookup:
    return '"' + address_to_lookup + '"'
  return address_to_lookup


def multiple_address_match(file, all_user_input, download=False):
  csv_headers = ['id', 'inputAddress', 'matchedAddress', 'uprn', 'matchType', 'confidenceScore', 'documentScore', 'rank']  # yapf: disable

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
    return page_error(None, e, page_name)


def multiple_address_match_original(file, all_user_input, download=False):
  csv_headers = ['id', 'inputAddress',  'matchedAddress', 'uprn', 'matchType', 'confidenceScore', 'documentScore', 'rank', 'addressType(Paf/Nag)', 'recommendationCode']  # yapf: disable

  contents = file.readlines()
  remove_header_row(contents)

  # Set 'write' type depending on if the results are to be downloaded or shown in browser
  if download:
    proxy = StringIO()
    writer = csv.writer(proxy)
    writer.writerow(csv_headers)

    def write(id, addr, m_addr, address_type, uprn, m_type, confid_score,
              doc_score, rank, recommendationCode):
      writer.writerow([
          given_id,
          address_to_lookup.replace('"', ''), m_addr, adrs.uprn.value,
          match_type, adrs.confidence_score.value, adrs.underlying_score.value,
          rank, address_type, recommendationCode,
      ])

    def finalize(line_count, no_addresses_searched, single_match_total,
                 multiple_match_total, no_match_total):
      # Creating the byteIO object from the StringIO Object
      mem = BytesIO()
      mem.write(proxy.getvalue().encode())
      mem.seek(0)
      proxy.close()
      return mem, line_count

    def get_match_type(n_addr):
      return 'M' if n_addr > 1 else 'S'

  else:
    # Showing the results in HTML means we need to escape any html injection
    ths = [{'value': x, 'ariaSort': None} for x in csv_headers]
    trs = []

    def write(id, addr, m_addr, address_type, uprn, m_type, confid_score,
              doc_score, rank, recommendationCode):
      trs.append({
          'tds': [
              {'value': remove_script_and_html_from_str(given_id) },
              {'value': remove_script_and_html_from_str(address_to_lookup) },
              {'value': m_addr},
              {'value': adrs.uprn.value},
              {'value': match_type},
              {'value': adrs.confidence_score.value},
              {'value': round(float(adrs.underlying_score.value), 2)},
              {'value': rank},
              {'value': address_type},
              {'value': recommendationCode},
          ]
      }) # yapf: disable

    def finalize(line_count, no_addresses_searched, single_match_total,
                 multiple_match_total, no_match_total):
      headers = [
          'Number of addresses searched:', 'Single matches:',
          'Multiple Matches', 'No Match:'
      ]
      answers = [
          no_addresses_searched, single_match_total, multiple_match_total,
          no_match_total
      ]
      results_summary_table_trs = [{
          'tds': [{
              'value': headers[x]
          }, {
              'value': answers[x]
          }]
      } for x in range(0, len(headers))]

      return {
          'ths': ths,
          'trs': trs
      }, {
          'ths': [],
          'trs': results_summary_table_trs
      },

    def get_match_type(n_addr):
      return '<p style="background-color:orange;">M</p>' if n_addr > 1 else '<p style="background-color:Aquamarine;">S</p>'

  line_count = 0
  no_addresses_searched = 0
  single_match_total = 0
  multiple_match_total = 0
  no_match_total = 0

  for line in contents:
    line = line.strip().decode('utf-8')
    given_id, address_to_lookup = line.split(',', maxsplit=1)

    all_user_input['input'] = address_to_lookup

    try:
      result = api(
          '/addresses',
          'multiple',
          all_user_input,
      )
    except Exception as e:
      logging.error(
          'Error on a singlesearch API call for:\n "{all_user_input}"')
      return page_error(None, e, page_name)

    # For testing the API <Response [429]> too many requests issue
    #print(result)
    #print(result.json())

    matched_addresses = get_addresses(result.json(), 'multiple')

    # Get the attributes of the Response a user might want
    responseAttributes = get_response_attributes(result.json());

    no_results = len(matched_addresses)
    if no_results == 1:
      single_match_total += 1
    elif no_results > 1:
      multiple_match_total += no_results
    elif no_results == 0:
      no_match_total += 1

    match_type = get_match_type(len(matched_addresses))
    no_addresses_searched += 1

    for rank, adrs in enumerate(matched_addresses, start=1):
      line_count += 1
      actual_address_type, preffered_address_format = \
          get_preffered_format_of_address(adrs,all_user_input)
      write(
          given_id,
          address_to_lookup,
          preffered_address_format,
          actual_address_type,
          adrs.uprn.value,
          match_type,
          adrs.confidence_score.value,
          adrs.underlying_score.value,
          rank,
          responseAttributes.get('recommendationCode'),
      )

  return finalize(line_count, no_addresses_searched, single_match_total,
                  multiple_match_total, no_match_total)


def uprn_multiple_address_match_original(file, all_user_input):
  # Only provide downloadable output
  csv_headers = ['uprn', 'matchedAddress', 'confidenceScore']

  contents = file.readlines()
  remove_header_row(contents)

  proxy = StringIO()
  writer = csv.writer(proxy)
  writer.writerow(csv_headers)

  line_count = 0

  file_content_formatted = []
  for line in contents:
    line = line.strip().decode('utf-8')
    given_id, uprn = line.split(',', maxsplit=1)
    file_content_formatted.append({'id': given_id, 'uprn': uprn})

  try:
    result = submit_uprn_mm_job(file_content_formatted, all_user_input)
  except:
    logging.error(
        f'Error on a UPRN Multiple API call for:\n "{all_user_input}"')
    return page_error(None, e, page_name)

  matched_addresses = get_addresses(result.json(), 'multiple_uprn')

  def finalize(line_count):
    # Creating the byteIO object from the StringIO Object
    mem = BytesIO()
    mem.write(proxy.getvalue().encode())
    mem.seek(0)
    proxy.close()
    return mem, line_count

  for adrs in matched_addresses:
    line_count += 1
    actual_address_type, preffered_address_format = \
        get_preffered_format_of_address(adrs,all_user_input)
    writer.writerow([
        adrs.uprn.value,
        adrs.formatted_address.value,
        adrs.confidence_score.value,
    ])

  return finalize(line_count)
