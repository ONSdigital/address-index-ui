import os
import json
import requests
from . import app
from flask import render_template
from io import StringIO, BytesIO
from .models.get_endpoints import get_endpoints
from .models.get_addresses import get_addresses
from .page_error import page_error
import urllib
import csv


def get_params(all_user_input):
  """Return a list of parameters formatted for API header, from class list of inputs"""
  params = ['verbose=True']
  for param, value in all_user_input.items():
    if not str(value):
      continue
    if (os.getenv('FLASK_ENV') == 'development') and (param == 'epoch'):
      # do not add epoch for testing
      continue

    if type(value) == str:
      value = value.replace('%', '')
    quoted_param = urllib.parse.quote_plus(str(param))
    quoted_value = urllib.parse.quote_plus(str(value))
    params.append(quoted_param + '=' + quoted_value)

  return '&'.join(params)


def api(url, called_from, all_user_input):
  """API helper, all pages go through here to interact with API"""

  header = {
      "Content-Type": "application/json",
  }

  params = get_params(all_user_input)
  if (called_from == 'uprn') or (called_from == 'postcode'):
    url = app.config.get('API_URL') + url + all_user_input.get(called_from, '')
  elif called_from == 'singlesearch':
    url = app.config.get('API_URL') + url

  r = requests.get(
      url,
      params=params,
      headers=header,
  )

  return r


def multiple_address_match(file, all_user_input, download=False):
  csv_headers = ['id', 'inputAddress', 'matchedAddress', 'uprn', 'matchType', 'confidenceScore', 'documentScore', 'rank']  # yapf: disable

  contents = file.readlines()

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

    result = api(
        '/addresses',
        'singlesearch',
        all_user_input,
    )

    if result != 'error_connecting':
      matched_addresses = get_addresses(result.json(), 'singlesearch')
    else:
      return 'error_connecting', 'error_connecting'

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
