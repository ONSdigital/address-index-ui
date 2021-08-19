import os
import json
import requests
from . import app
from flask import render_template
from io import StringIO, BytesIO
from .models.get_endpoints import get_endpoints
from .models.get_addresses import get_addresses
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
    proposed_params = {k: v for k, v in all_user_input.items() if v}

  r = requests.get(
      url,
      params=params,
      headers=header,
  )

  return r


def multiple_address_match(file, all_user_input, download=False):
  final_csv = 'id, inputAddress, matchedAddress, uprn, matchType, confidenceScore, documentScore, rank\n\r'
  ths = [{'value': x, 'ariaSort': None} for x in final_csv.split(',')]
  trs = []

  contents = file.readlines()
  if download:
    proxy = StringIO()
    writer = csv.writer(proxy)
    writer.writerow(final_csv.split(','))

  line_count = 0
  for line in contents:
    line = line.strip().decode("utf-8")
    given_id = line.split(',')[0]
    address_to_lookup = line.split(',')[1]
    all_user_input['input'] = address_to_lookup

    result = api(
        '/addresses',
        'singlesearch',
        all_user_input,
    )

    matched_addresses = get_addresses(result.json(), 'singlesearch')
    if len(matched_addresses) > 1:
      match_type = 'M' if download else '<p style="background-color:orange;">M</p>' 
    else:
      match_type = 'S' if download else '<p style="background-color:orange;">S</p>' 
    rank = 1

    # Set 'write' type depending on if the results are to be downloaded or shown in browser
    if download:
      def write(id, addr, m_addr, uprn, m_type, confid_score, doc_score, rank):
        writer.writerow([
            given_id, address_to_lookup, adrs.formatted_address_nag.value,
            adrs.uprn.value, match_type, adrs.confidence_score.value,
            adrs.underlying_score.value, rank ])

      def finalize(line_count, ths, trs):
        # Creating the byteIO object from the StringIO Object
        mem = BytesIO()
        mem.write(proxy.getvalue().encode())
        mem.seek(0)
        proxy.close()
        return mem, line_count

    else:
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
            ] })
      def finalize(line_count, ths, trs):
        return {'ths': ths, 'trs': trs}

    for adrs in matched_addresses:
      line_count = line_count + 1
      write(given_id,address_to_lookup,adrs.formatted_address_nag.value,adrs.uprn.value,match_type, \
        adrs.confidence_score.value,adrs.underlying_score.value,rank,)
      rank = rank + 1

  return finalize(line_count, ths, trs)

