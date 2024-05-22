import os
import json
import csv
import requests
from io import StringIO, BytesIO
from flask import render_template, request, session, send_file
from flask_login import login_required
from . import app, get_classifications_cached
from aims_ui.page_controllers.b_multiple_matches.utils.multiple_address_utils import job_url_if_authorised

# For the gz download
import urllib.request
import ssl
import gzip


def get_autosuggest_list():
  """Return the classifications list in the format expected by the autosuggest component"""
  formatted_class_list = []
  class_list = get_classifications_cached()

  for classification in class_list:
    formatted_class_list.append({
        'en': classification.get('code'),
        'category': classification.get('label'),
    })

  return formatted_class_list


@login_required
@app.route('/autosuggest/<autosuggest_type>.json', methods=['GET', 'POST'])
def autosuggest(autosuggest_type):
  """ Autosuggest data for various typeaheads """
  dir_path = os.path.dirname(os.path.realpath(__file__))

  if 'classification' in autosuggest_type:
    formatted_class_list = []
    class_list = get_classifications_cached()

    for classification in class_list:
      formatted_class_list.append({
          'en': classification.get('code'),
          'category': classification.get('label'),
      })
    if 'reverse' in autosuggest_type:
      # Add the reverse so the endpoint can be searched in reverse
      for classification in class_list:
        formatted_class_list.append({
            'en': classification.get('label'),
            'category': classification.get('code'),
        })

    return json.dumps(formatted_class_list)

  elif 'api-urls' in autosuggest_type:
    formatted_autosuggest_list = []

    file_path = f'{dir_path}/static/downloads/api-url-options.csv'
    with open(file_path, 'r', encoding='utf-8') as f:
      list_from_file = [line.strip() for line in f]

    # Convert options ['x', 'y'... to classification format
    for option in list_from_file:
      formatted_autosuggest_list.append({
          'en': option,
      })
    return json.dumps(formatted_autosuggest_list)

  return ('Invalid autosuggest type')


@login_required
@app.route(f'/downloads/<file_name>', methods=['GET', 'POST'])
def download_handler(file_name):
  # Create example_csv

  proxy = StringIO()
  writer = csv.writer(proxy)
  dir_path = os.path.dirname(os.path.realpath(__file__))

  if file_name == 'classifications_list':
    f = open(f'{dir_path}/static/downloads/classifications.csv', 'rb')

  elif file_name == 'example_multiple_address':
    f = open(f'{dir_path}/static/downloads/example_multiple_match_upload.csv',
             'rb')
  elif file_name == 'example_multiple_address_big':
    f = open(
        f'{dir_path}/static/downloads/example_multiple_match_5k_upload.csv',
        'rb')
  elif file_name == 'tool_tip_clerical_information':
    f = open(f'{dir_path}/static/downloads/tool_tip_clerical_information.csv',
             'rb')
  elif file_name == 'uprn_example_multiple_address':
    f = open(
        f'{dir_path}/static/downloads/uprn_example_multiple_match_upload.csv',
        'rb')

  elif 'googlefiledownload' in file_name:
    file_name = file_name.replace('googlefiledownload', '')
    # Now download that gzip location, extract and send as a download
    # The file name is now the JOBID (do a server lookup, find the download link to avoid injection

    url = job_url_if_authorised(file_name)

    # Download the csv.gz
    response = requests.get(url)
    file_name = 'results'

    # Download to memory
    f = BytesIO(response.content)

    return send_file(f,
                     mimetype='application/gzip',
                     download_name=f'{file_name}.csv.gz',
                     as_attachment=True)

  return send_file(f,
                   mimetype='text/csv',
                   download_name=f'{file_name}.csv',
                   as_attachment=True)
