import os
import json
import requests
from . import app
from flask import render_template
from io import StringIO, BytesIO
from .models.get_endpoints import get_endpoints
from .models.get_addresses import get_addresses
from .page_error import page_error
from .download_handler import get_autosuggest_list
import urllib
import csv


def get_classifications():
  """Return classification endpoint result as json pairs"""

  r = api(
      '/classifications',
      'singlesearch',
      [],
  )
  return r

def check_reverse_classification(value):
  autosuggest_list = get_autosuggest_list()
  for category in autosuggest_list:
    if value == category.get('category'):
      return category.get('en')

  return value 

def get_api_auth():
  """Get the auth type, and subsequent required authorisation parameters"""
  api_auth = {}
  if app.config.get('API_AUTH_TYPE') == 'JWT':
    api_auth['API_AUTH_TYPE'] = 'JWT'
    api_auth['JWT_TOKEN'] = app.config.get('JWT_TOKEN')
  elif app.config.get('API_AUTH_TYPE') == 'BASIC_AUTH':
    api_auth['API_AUTH_TYPE'] = 'BASIC_AUTH'
    api_auth['API_BSC_AUTH_USERNAME'] = app.config.get('API_BSC_AUTH_USERNAME')
    api_auth['API_BSC_AUTH_PASSWORD'] = app.config.get('API_BSC_AUTH_PASSWORD')
  return api_auth


def get_params(all_user_input):
  """Return a list of parameters formatted for API header, from class list of inputs"""
  params = ['verbose=True']
  print(all_user_input)
  for param, value in all_user_input.items():
    if not str(value):
      continue
    if (os.getenv('FLASK_ENV') == 'development') and (param == 'epoch'):
      # do not add epoch for testing
      continue

    if type(value) == str:
      value = value.replace('%', '')

    # Check if the value is for the classifications, if so, check to see if it needs reversing 
    if param == 'classificationfilter':
      value = check_reverse_classification(value)

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
