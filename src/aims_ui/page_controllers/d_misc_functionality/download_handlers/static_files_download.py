import csv
import os
from io import BytesIO, StringIO

import requests
import aims_ui
from flask import send_file
from flask_login import login_required

from aims_ui import app
from aims_ui.page_controllers.b_multiple_matches.utils.multiple_match_api_utils import job_url_if_authorised
from aims_ui.page_controllers.f_error_pages.page_error import page_error

# For the gz download

page_name = 'download_handler'


@login_required
@app.route(f'/downloads/static/<file_name>', methods=['GET'])
def static_files_download_handler(file_name):
  # Create example_csv

  proxy = StringIO()
  csv.writer(proxy)

  # Use the aims_ui to find the root dir and then navigate to the file from there to avoid issues with different file structures in testing/production
  project_root = os.path.dirname(os.path.abspath(aims_ui.__file__))
  download_files_location = f'{project_root}/static/downloads'

  # Initially set file to None for 404 not found handling
  f = None

  if file_name == 'classifications_list':
    f = open(f'{download_files_location}/classifications.csv', 'rb')
  elif file_name == 'example_multiple_address':
    f = open(f'{download_files_location}/example_multiple_match_upload.csv',
             'rb')
  elif file_name == 'example_multiple_address_big':
    f = open(f'{download_files_location}/example_multiple_match_5k_upload.csv',
             'rb')
  elif file_name == 'uprn_example_multiple_address':
    f = open(
        f'{download_files_location}/uprn_example_multiple_match_upload.csv',
        'rb')

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
