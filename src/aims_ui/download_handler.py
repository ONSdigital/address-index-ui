import os
from . import app, get_classifications_cached
import json
import csv
import requests
from io import StringIO, BytesIO
from flask import render_template, request, session, send_file
from flask_login import login_required
from .multiple_address_utils import downloadZipToMemory

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
  elif file_name == 'tool_tip_clerical_information':
    f = open(f'{dir_path}/static/downloads/tool_tip_clerical_information.csv',
             'rb')
  elif 'googlefiledownload' in file_name:
    file_name = file_name.replace('googlefiledownload', '')
    # Now download that gzip location, extract and send as a download
    # The file name is now the JOBID (do a server lookup, find the download link to avoid injection

    url = 'https://drive.google.com/u/0/uc?id=1KYT-DDeY_EKMfjeycCleibmOBVK1AeGf&export=download'
    # create an SSL context without certificate verification

    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    # download the file using urllib.request.urlopen() with the SSL context
    with urllib.request.urlopen(url, context=context) as u:
      file_content = u.read()


    # download the gzipped file using urllib.request.urlopen() with the SSL context
    with urllib.request.urlopen(url, context=context) as u:
      compressed_data = u.read()

    # unzip the contents of the gzipped file in memory
    with BytesIO(compressed_data) as bio:
      with gzip.GzipFile(mode="rb", fileobj=bio) as decompressed_file:
        csv_content = decompressed_file.read().decode('utf-8')

    final_csv = 'inputAddress, matchedAdress, uprn, matchType, confidenceScore, documentScore \n'
    # Now we can adjust csv content
    csv_rows = list(csv.reader(csv_content.splitlines()))
    for row in csv_rows:
      if (str(row) != "['id', 'inputaddress', 'response']") and (len(row) > 2):
        # extract the API response string from the third column of the row
        api_response = row[2]
        searched_address = str(row[1])

        # parse the API response string as JSON
        api_data = json.loads(api_response)
        r = api_data.get('response', {})

        addresses = r.get('addresses', [{}])
        for address in addresses:
          matched_add = address.get('formattedAddress','NA')
          matched_uprn = address.get('uprn','NA')
          many_or_single = 'M' if len(addresses) > 1 else 'S' 
          matched_confidence_score = address.get('confidenceScore','NA')
          matched_underlying_score = address.get('underlyingScore','NA')
          result_string = f'"{str(searched_address)}","{str(matched_add)}",{str(matched_uprn)},{many_or_single},{str(matched_confidence_score)},{str(matched_underlying_score)}'
          final_csv = final_csv + result_string + '\n'


    # create an in-memory file-like object
    f = BytesIO(final_csv.encode('utf-8'))

  return send_file(f,
                   mimetype='text/csv',
                   attachment_filename=f'{file_name}.csv',
                   as_attachment=True)
