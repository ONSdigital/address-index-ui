import csv
import json
import os
from io import BytesIO, StringIO

import requests
from flask import send_file
from flask_login import login_required

from aims_ui import app
from aims_ui.app_helpers.classification_utils.autosuggest import get_classification_autosuggest_list, get_full_classification_autosuggest, get_classification_autosuggest_list_reversed
from aims_ui.page_controllers.b_multiple_matches.large_multiple_match.utils.multiple_match_api_utils import job_url_if_authorised
from aims_ui.page_controllers.f_error_pages.page_error import page_error

# For the gz download

page_name = 'download_handler'


@login_required
@app.route(f'/downloads/large_multiple_match/<file_name>',
           methods=['GET', 'POST'])
def large_multiple_address_download_handler(file_name):
  # Create example_csv

  proxy = StringIO()
  csv.writer(proxy)

  current_file_path = os.path.dirname(os.path.realpath(__file__))
  root_dir_path = os.path.dirname(os.path.dirname(current_file_path))

  if 'googlefiledownload' not in file_name:
    return page_error(
        called_from_page_name=page_name,
        error_title='404 - File not found',
        error_description=[
            'This file does not exist or has been removed.',
            'Please contact the AIMS team if you think this is an error.'
        ])

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
