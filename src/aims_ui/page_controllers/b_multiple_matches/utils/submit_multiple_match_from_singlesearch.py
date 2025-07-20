import csv
from io import BytesIO, StringIO

from aims_ui.models.get_addresses import get_addresses
from aims_ui.page_controllers.b_multiple_matches.utils.multiple_match_utils import (
    get_preffered_format_of_address, remove_header_row)
from aims_ui.page_helpers.api.api_interaction import api, get_response_attributes

from .multiple_match_file_upload_utils import remove_script_and_html_from_str

page_name = 'multiple_match_submit'

def multiple_address_match_from_singlesearch_display(file, all_user_input):
  csv_headers = [
      'id', 'inputAddress', 'matchedAddress', 'uprn', 'matchType',
      'confidenceScore', 'documentScore', 'rank', 'addressType(Paf/Nag)', 'aiRating'
  ]  # yapf: disable

  custom_attributes = all_user_input.get('custom-bulk-attributes')
  if len(custom_attributes) > 0:
      custom_attributes = custom_attributes.rstrip(" ")
      for att in custom_attributes.split(" "):
          csv_headers.append(att)

  contents = file.readlines()
  remove_header_row(contents)

  # Showing the results in HTML means we need to escape any html injection
  ths = [{'value': x, 'ariaSort': None} for x in csv_headers]
  trs = []

  # data = [given_id,
  #         address_to_lookup,
  #         preffered_address_format,
  #         actual_address_type,
  #         adrs.uprn.value,
  #         match_type,
  #         adrs.confidence_score.value,
  #         adrs.underlying_score.value,
  #         rank,
  #         adrs.airRating.value



  def write(data):
    tdlist =  [
            {'value': remove_script_and_html_from_str(data[0])},
            {'value': remove_script_and_html_from_str(data[1])},
            {'value': data[2]},
            {'value': data[4]},
            {'value': data[5]},
            {'value': data[6]},
            {'value': data[7]},
            {'value': data[8]},
            {'value': data[3]},
            {'value': data[9]},
        ]

    if len(custom_attributes) > 0:
        startnum = 10
        endnum = len(data)
        for i in range(startnum, endnum):
            tdlist.append({'value': data[i]})

    trs.append({'tds' : tdlist})  # yapf: disable


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

    # If there's an error it should be caught by the calling function
    result = api(
        '/addresses',
        'multiple',
        all_user_input,
    )

    matched_addresses = get_addresses(result.json(), 'multiple')

    # Get the attributes of the Response a user might want
    get_response_attributes(result.json())

    no_results = len(matched_addresses)
    if no_results == 1:
      single_match_total += 1
    elif no_results > 1:
      multiple_match_total += no_results
    elif no_results == 0:
      no_match_total += 1

    match_type = get_match_type(no_results)
    no_addresses_searched += 1

    for rank, adrs in enumerate(matched_addresses, start=1):
      line_count += 1
      actual_address_type, preffered_address_format = \
          get_preffered_format_of_address(adrs, all_user_input)
      # write(
      #     given_id,
      #     address_to_lookup,
      #     preffered_address_format,
      #     actual_address_type,
      #     adrs.uprn.value,
      #     match_type,
      #     adrs.confidence_score.value,
      #     adrs.underlying_score.value,
      #     rank,
      #     adrs.airRating.value,
      # )

      data = [given_id,
          address_to_lookup,
          preffered_address_format,
          actual_address_type,
          adrs.uprn.value,
          match_type,
          adrs.confidence_score.value,
          adrs.underlying_score.value,
          rank,
          adrs.airRating.value
      ]
      if len(custom_attributes) > 0:
          for att in custom_attributes.split(" "):
              data.append(eval(f'adrs.{att}.value'))

      write(data)

  # Unindent the following code so it's outside the 'for line in contents:' loop
  headers = [
      'Number of addresses searched:', 'Single matches:', 'Multiple Matches',
      'No Match:'
  ]
  answers = [
      no_addresses_searched, single_match_total, multiple_match_total,
      no_match_total
  ]

  results_summary_table_trs = [{
      'tds': [{'value': headers[x]}, {'value': answers[x]}]
  } for x in range(len(headers))]  # yapf: disable

  return {'ths': ths, 'trs': trs}, {'ths': [], 'trs': results_summary_table_trs}  # yapf: disable



def multiple_address_match_from_singlesearch_download(file, all_user_input):
  csv_headers = ['id', 'inputAddress',  'matchedAddress', 'uprn', 'matchType', 'confidenceScore', 'documentScore', 'rank', 'addressType(Paf/Nag)', 'aiRating']  # yapf: disable

  custom_attributes = all_user_input.get('custom-bulk-attributes')
  if len(custom_attributes) > 0:
      custom_attributes = custom_attributes.rstrip(" ")
      for att in custom_attributes.split(" "):
          csv_headers.append(att)

  contents = file.readlines()
  remove_header_row(contents)

  proxy = StringIO()
  writer = csv.writer(proxy)

  if all_user_input.get('header_row_export') == 'True':
    writer.writerow(csv_headers)

  def write(id, addr, m_addr, address_type, uprn, m_type, confid_score,
            doc_score, rank, ai_rating):
    data = [given_id,
        address_to_lookup.replace('"', ''),
        m_addr,
        adrs.uprn.value,
        match_type,
        adrs.confidence_score.value,
        adrs.underlying_score.value,
        rank,
        address_type,
        ai_rating]
    if len(custom_attributes) > 0:
        for att in custom_attributes.split(" "):
            data.append(eval(f'adrs.{att}.value'))

    writer.writerow(data)


  def get_match_type(n_addr):
    return 'M' if n_addr > 1 else 'S'

  line_count = 0
  no_addresses_searched = 0
  single_match_total = 0
  multiple_match_total = 0
  no_match_total = 0

  for line in contents:
    line = line.strip().decode('utf-8')
    given_id, address_to_lookup = line.split(',', maxsplit=1)

    all_user_input['input'] = address_to_lookup

    # Errors should be caught by the calling function
    result = api(
        '/addresses',
        'multiple',
        all_user_input,
    )

    matched_addresses = get_addresses(result.json(), 'multiple')

    # Get the attributes of the Response a user might want
    get_response_attributes(result.json())

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
          get_preffered_format_of_address(adrs, all_user_input)
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
          adrs.airRating.value,
      )

  # Creating the byteIO object from the StringIO Object
  mem = BytesIO()
  mem.write(proxy.getvalue().encode())
  mem.seek(0)
  proxy.close()

  return mem, line_count
