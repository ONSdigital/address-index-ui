# Based on the static file, create the classification code lookup json
# as well as the reversed version and make vailable attached to the app object.

# Classification processing is then done elsewhere

import csv

import aims_ui
from pathlib import Path

def parse_classification_csv_content():
  """ Return CSV as a list of dicts, with whitespace stripped """

  # Start at package root (aims_ui), then navigate to the csv file
  root_path = Path(aims_ui.__file__).resolve().parent
  file_path = root_path / 'static' / 'downloads' / 'classifications.csv'

  # Use csv reader to convert csv into list of dicts
  with open(file_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, skipinitialspace=True)

    content = []
    for row in reader:
      # Remove whitespace if it's a string, otherwise leave as is
      cleaned_row = {
        key: value.strip() if isinstance(value, str) else value
        for key, value in row.items()
      }

      content.append(cleaned_row)

  return content

def get_classification_file_content_as_dict():
  """ Get the content of the classifications CSV as a dict """
  # In the format [{'code': 'C', 'label': 'Commercial'}, ...]

  classification_csv_content = parse_classification_csv_content()

  # Currently in the format: {'Concatenated': 'ZW99TP', 'Class_Desc': 'Temple', 'Pr...
  # We want to convert to: {'code': 'ZW99TP', 'label': 'Temple'}

  classification_dict = []
  for row in classification_csv_content:
    classification_row = {
        'code': row.get('Concatenated', ''),
        'label': row.get('Class_Desc', ''),
        'primary_code': row.get('Primary_Code', ''),
        'secondary_code': row.get('Secondary_Code', ''),
        'tertiary_code': row.get('Tertiary_Code', ''),
        'quaternary_code': row.get('Quaternary_Code', ''),
        'primary_desc': row.get('Primary_Desc', ''),
        'secondary_desc': row.get('Secondary_Desc', ''),
        'tertiary_desc': row.get('Tertiary_Desc', ''),
        'quaternary_desc': row.get('Quaternary_Desc', ''),
    }
    classification_dict.append(classification_row)
  
  # Now it's standardised, deal with outlier issues
  classification_dict = handle_ancillary_duplicates(classification_dict)

  return classification_dict


def handle_ancillary_duplicates(class_list):
  """ Residential, Commercial, Militaery and Land have duplicate ancillary descriptions"""
  # Replace the english decriptions with additional hierarchey descriptions
  # From an array like: [{'code': 'ZW99TP', 'label': 'Temple'}, ...]

  codes_and_replacemnt_labels = [
      {
          'code': 'RB',
          'label': 'Residential Ancillary Building'
      },
      {
          'code': 'LB',
          'label': 'Land Ancillary Building'
      },
      {
          'code': 'CB',
          'label': 'Commercial Ancillary Building'
      },
      {
          'code': 'MB',
          'label': 'Military Ancillary Building'
      },
  ]

  for class_option in class_list:
    for replacement in codes_and_replacemnt_labels:
      aquired_code = class_option.get('code', '')

      if replacement.get('code') == aquired_code:
        class_option['label'] = replacement.get('label')

  return class_list

