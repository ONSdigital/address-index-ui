import json
import os

from flask_login import login_required

import aims_ui
from aims_ui import app
from aims_ui.app_helpers.classification_utils.autosuggest import get_classification_autosuggest_list, get_full_classification_autosuggest, get_classification_autosuggest_list_reversed

# For the gz download

page_name = 'download_handler'


@login_required
@app.route('/autosuggest/<autosuggest_type>.json', methods=['GET', 'POST'])
def autosuggest_download_handler(autosuggest_type):
  """ Autosuggest data for various typeaheads """

  # Full classification (invludes reverse and right way!)
  if 'full_classification' in autosuggest_type:
    full_classification_list = get_full_classification_autosuggest()
    return json.dumps(full_classification_list)

  # Check for reverse classification first
  elif 'reversed_classification' in autosuggest_type:
    classification_list_reversed = get_classification_autosuggest_list_reversed(
    )
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
