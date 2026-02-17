from .builder import get_classification_file_content_as_dict
import logging

def get_full_classification_for_code_or_label(classification):
  """ Given a classification code, or label - return the code """

  classification_dict = get_classification_file_content_as_dict()

  # Standardise the provided classification - remove whitespace and enforce uppercase
  classification_code_or_label = classification.strip().upper()

  # Check that the classification code is valid
  if not classification_is_valid(classification_code_or_label):
    # Classification code is not valid, return original input and log error
    logging.error(f'Invalid classification code or label provided: {classification}')
    return classification

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

def classification_is_valid(classification_to_check):
  """ Explicit check against full list of classifications as API only checks strucutre """
  # Checks codes AND labels, accepts a match as valid (non case sensitive)

  # Get the classification dict [{'code': 'C', 'label': 'Commercial'}, ...]
  classifications_dict = get_classification_file_content_as_dict()

  # Append the label and code for each classification into a single, lowercase list
  full_classifications = [''] # Include blank as valid option
  for classification_and_label in classifications_dict:
    full_classifications.append(classification_and_label.get('code', '').lower())
    full_classifications.append(classification_and_label.get('label', '').lower())
  
  classification_to_check = classification_to_check.lower()
  
  if classification_to_check.lower() in full_classifications:
    return True
  return False

