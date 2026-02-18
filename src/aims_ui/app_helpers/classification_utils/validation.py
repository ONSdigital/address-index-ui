from .builder import get_classification_file_content_as_dict
import logging

def get_full_classification_for_code_or_label(classification):
  """ Given a classification code, or label - return the code """

  classification_dict = get_classification_file_content_as_dict()

  # Standardise the provided classification:
  # remove whitespace, enforce uppercase, remove "*"
  classification_code_or_label = classification.strip()
  classification_code_or_label = classification_code_or_label.upper()
  classification_code_or_label = classification_code_or_label.replace('*', '')

  code_to_return = classification_code_or_label
  for classification in classification_dict:
    # If the label matches
    if classification_code_or_label == classification.get('label').upper():
      code_to_return = classification.get('code')

    # If the code matches
    if classification_code_or_label == classification.get('code').upper():
      code_to_return = classification.get('code')

  # Return blank
  if code_to_return == '':
    return ''

  # Ensure all codes end with * (except '')
  code_to_return = code_to_return + '*'

  return code_to_return

def classification_is_valid(classification_code_or_label):
  """ Given a clasification code or label, check it's valid """
  classification_code_to_check = get_full_classification_for_code_or_label(classification_code_or_label)
  # Now if it was entered with * or without, it will now have one
  # If the user entered a string version, it will now be the code

  # Get the classification dict [{'code': 'C', 'label': 'Commercial'}, ...]
  classifications_dict = get_classification_file_content_as_dict()

  # Create full list of classifications
  full_classifications = [ x.get('code') + '*' for x in classifications_dict ]
  full_classifications.append('') # Include blank as valid option
  
  if classification_code_to_check in full_classifications:
    return True
  return False
