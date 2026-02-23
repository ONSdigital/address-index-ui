import csv
import json
import os
from io import BytesIO, StringIO

import requests
from flask import request, send_file
from flask_login import login_required

from aims_ui import app
from aims_ui.app_helpers.classification_utils.autosuggest import get_classification_autosuggest_list, get_full_classification_autosuggest, get_classification_autosuggest_list_reversed
from aims_ui.page_controllers.b_multiple_matches.utils.multiple_match_api_utils import job_url_if_authorised
from aims_ui.page_controllers.f_error_pages.page_error import page_error

# For the gz download

page_name = 'download_handler'

print('askjdhskj')


@login_required
@app.route(f'/downloads/small_multiple_match', methods=['POST'])
def small_multiple_address_download_handler():
  # Following body was posted:

  form_data = request.form
  print()
  print()
  print()
  print('aslkhdkjshkjh')
  print(form_data)
  print()
  print()
  print()
  print()

