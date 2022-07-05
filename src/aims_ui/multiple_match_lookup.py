import json
from io import StringIO, BytesIO
from aims_ui.api_interaction import api
import csv
from .models.get_endpoints import get_endpoints
from .models.get_addresses import get_addresses
from .page_error import page_error
import logging


def remove_header_row(contents):
  remove_index = None
  for i in range(0, len(contents)):
    line = contents[i]
    line = line.strip().decode('utf-8')
    if (line == 'id,address') or (line == 'id,searchAddress'):
      remove_index = i

  if remove_index != None:
    contents.pop(remove_index)


def multiple_address_match(file, all_user_input, download=False):
  csv_headers = ['id', 'inputAddress', 'matchedAddress', 'uprn', 'matchType', 'confidenceScore', 'documentScore', 'rank']  # yapf: disable

  contents = file.readlines()
  remove_header_row(contents)

  # Set 'write' type depending on if the results are to be downloaded or shown in browser
  if download:
    proxy = StringIO()
    writer = csv.writer(proxy)
    writer.writerow(csv_headers)

    def write(id, addr, m_addr, uprn, m_type, confid_score, doc_score, rank):
      writer.writerow([
          given_id, address_to_lookup, adrs.formatted_address_nag.value,
          adrs.uprn.value, match_type, adrs.confidence_score.value,
          adrs.underlying_score.value, rank
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
    ths = [{'value': x, 'ariaSort': None} for x in csv_headers]
    trs = []

    def write(id, addr, m_addr, uprn, m_type, confid_score, doc_score, rank):
      trs.append({
          'tds': [
              {'value': given_id},
              {'value': address_to_lookup},
              {'value': adrs.formatted_address_nag.value},
              {'value': adrs.uprn.value},
              {'value': match_type},
              {'value': adrs.confidence_score.value},
              {'value': adrs.underlying_score.value},
              {'value': rank},
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
          'singlesearch',
          all_user_input,
      )
    except:
      logging.error(
          'Error on a singlesearch API call for:\n "{all_user_input}"')
      return page_error(None, e, page_name)

    # For testing the API <Response [429]> too many requests issue
    #print(result)
    #print(result.json())

    matched_addresses = get_addresses(result.json(), 'singlesearch')

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
      write(
          given_id,
          address_to_lookup,
          adrs.formatted_address_nag.value,
          adrs.uprn.value,
          match_type,
          adrs.confidence_score.value,
          adrs.underlying_score.value,
          rank,
      )

  return finalize(line_count, no_addresses_searched, single_match_total,
                  multiple_match_total, no_match_total)
