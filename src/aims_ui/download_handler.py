import os
from . import app
import json
import csv
import requests
from .models.utilities.classifications import get_class_list
from io import StringIO, BytesIO
from flask import render_template, request, session, send_file
from flask_login import login_required


@login_required
@app.route('/autosuggest/<autosuggest_type>.json', methods=['GET', 'POST'])
def autosuggest(autosuggest_type):
  """ Autosuggest data for various typeaheads """
  if autosuggest_type == 'classification':
    formatted_class_list = []
    classifications_api_url = app.config.get('API_URL') + '/classifications'
    class_call = requests.get(classifications_api_url)
    class_list = json.loads(class_call.text).get('classifications')

    for classification in class_list:
      formatted_class_list.append(
          {'en': classification.get('code'),
           'category': classification.get('label') })

    return json.dumps(formatted_class_list)

  return ('Invalid autosuggest type')


@login_required
@app.route(f'/downloads/<file_name>', methods=['GET', 'POST'])
def download_handler(file_name):
  # Create example_csv

  proxy = StringIO()
  writer = csv.writer(proxy)

  if file_name == 'classifications_list':
    f = open('src/aims_ui/static/downloads/classifications.csv', 'rb')

  elif file_name == 'example_multiple_address':
    f = open('src/aims_ui/static/downloads/example_multiple_match_upload.csv',
             'rb')

  return send_file(f,
                   mimetype='text/csv',
                   attachment_filename=f'{file_name}.csv',
                   as_attachment=True)
