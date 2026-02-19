import csv
import json
import os
from io import BytesIO, StringIO

import requests
from flask import send_file
from flask_login import login_required

import aims_ui
from aims_ui import app
from aims_ui.app_helpers.classification_utils.autosuggest import get_classification_autosuggest_list, get_full_classification_autosuggest, get_classification_autosuggest_list_reversed
from aims_ui.page_controllers.b_multiple_matches.utils.multiple_match_api_utils import job_url_if_authorised
from aims_ui.page_controllers.f_error_pages.page_error import page_error

# For the gz download

page_name = 'download_handler'


@login_required
@app.route('/autosuggest/<autosuggest_type>.json', methods=['GET', 'POST'])
def autosuggest(autosuggest_type):
  """ Autosuggest data for various typeaheads """

  # Full classification (invludes reverse and right way!)
  if 'full_classification' in autosuggest_type:
    full_classification_list = get_full_classification_autosuggest()
    return json.dumps(full_classification_list)

  # Check for reverse classification first
  elif 'reversed_classification' in autosuggest_type:
    classification_list_reversed = get_classification_autosuggest_list_reversed()
    return json.dumps(classification_list_reversed)

  # Cover normal classification
  elif 'classification' in autosuggest_type:
    classification_list = get_classification_autosuggest_list()
    return json.dumps(classification_list)

  elif 'api-urls' in autosuggest_type:
    formatted_autosuggest_list = []

    project_root = os.path.dirname(os.path.abspath(aims_ui.__file__))
    file_path = f'{project_root}/static/downloads/api-url-options.csv'

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
  csv.writer(proxy)

  current_file_path = os.path.dirname(os.path.realpath(__file__))
  root_dir_path = os.path.dirname(os.path.dirname(current_file_path))

  # Initially set file to None for 404 not found handling
  f = None

  if file_name == 'classifications_list':
    f = open(f'{root_dir_path}/static/downloads/classifications.csv', 'rb')

  elif file_name == 'example_multiple_address':
    f = open(
        f'{root_dir_path}/static/downloads/example_multiple_match_upload.csv',
        'rb')
  elif file_name == 'example_multiple_address_big':
    f = open(
        f'{root_dir_path}/static/downloads/example_multiple_match_5k_upload.csv',
        'rb')
  elif file_name == 'uprn_example_multiple_address':
    f = open(
        f'{root_dir_path}/static/downloads/uprn_example_multiple_match_upload.csv',
        'rb')

  elif 'googlefiledownload' in file_name:
    file_name = file_name.replace('googlefiledownload', '')
    # Now download that gzip location, extract and send as a download
    # The file name is now the JOBID (do a server lookup, find the download link to avoid injection

    # False if user is not authorised
    url = job_url_if_authorised(file_name)

    if not url:
      return page_error(
          called_from_page_name=page_name,
          error_title='401 - User is not authorised',
          error_description=[
              'You are not authorised to download this file.',
              'Please contact the AIMS team if you think this is an error.'
          ])

    # Download the csv.gz
    response = requests.get(url)
    file_name = 'results'

    # Download to memory
    f = BytesIO(response.content)

    return send_file(f,
                     mimetype='application/gzip',
                     download_name=f'{file_name}.csv.gz',
                     as_attachment=True)

  # if the file_name is not found, return a 404
  if not f:
    return page_error(
        called_from_page_name=page_name,
        error_title='404 - File not found',
        error_description=[
            'This file does not exist or has been removed.',
            'Please contact the AIMS team if you think this is an error.'
        ])

  return send_file(f,
                   mimetype='text/csv',
                   download_name=f'{file_name}.csv',
                   as_attachment=True)
