import os
import urllib

from aims_ui.page_helpers.classification_utilities import check_reverse_classification


def remove_non_existant_parameters(params):
  """ Given a dict of params, remove any that the API won't recognise """

  # Deffine the only acceptable parameters (regardless of page) (see https://github.com/ONSdigital/aims-api/blob/main/api-definitions/explore-the-api/readme.md)
  acceptable_parameters = ['input', 'name', 'offset', 'limit', 'classificationfilter', 'rangekm', 'lat', 'lon', 'historical', 'matchthreshold', 'verbose', 'epoch', 'eboost', 'nboost', 'sboost', 'wboost', 'lboost', 'mboost', 'jboost', 'pafdefault', 'fallback', 'highlight', 'favourpaf', 'favourwelsh', 'includeauxiliarysearch', 'limitperaddress', 'groupfullpostcodes']

  # Remove any parameters that are not in the acceptable list
  params = {k: v for k, v in params.items() if k in acceptable_parameters}

  return params

def remove_epoch_in_testing_environment(params):
  """ Remove the "Epoch" parameter in development environmment """
  if os.getenv('FLASK_ENV') == 'development':
    if 'epoch' in params:
      params.pop('epoch')
  return params

def adjust_parameter_for_each_page(params, called_from_page_name):
  """ Make page specific adjustments to parameters """

  # If the page is for multiple addresses, enforce "verbose=False" for speed
  if (called_from_page_name == 'multiple'):
    # Always set verbose to False
    params['verbose'] = 'False'
  
  if (called_from_page_name == 'radiussearch'):
    # If the input is blank, ensure that a blank input is still sent!
    if not params.get('input'):
      params['input'] = ''
  
  return params

def adjust_params_for_all_pages(params):
  """ Make parameter adjustments that apply to all pages """

  # Do a reverse classification lookup if the classification filter is present
  if 'classificationfilter' in params:
    entered_classification = params['classificationfilter']
    classification = check_reverse_classification(entered_classification)
    params['classificationfilter'] = classification
  
  # Ensure historical is never None, default to False
  if 'historical' in params:
    historical_value = str(params['historical'])
    if historical_value == 'None':
      params['historical'] = 'False'
  
  # Replace the paf-nag preference with pafdefault
  if 'paf-nag-preference' in params:
    user_paf_nag_preference = params.get('paf-nag-preference')
    # Set the pafdefault value based on the user's preference
    paf_default_value = 'true' if user_paf_nag_preference == 'PAF' else 'false'
    params['pafdefault'] = paf_default_value

  # Remove any '%' characters from matchthreshold
  if 'matchthreshold' in params:
    current_threshold = str(params['matchthreshold'])
    new_threshold = current_threshold.replace('%', '')
    params['matchthreshold'] = new_threshold
  
  return params


def cleanup_parameters(params, called_from_page_name):
  """ Remove empty parameters add others that might be required"""

  print('Initial parameters: ' + str(params))

  # Adjustments for environment
  params = remove_epoch_in_testing_environment(params)

  # Now do page specific adjustments
  params = adjust_parameter_for_each_page(params, called_from_page_name)

  # Now do changes for all pages
  params = adjust_params_for_all_pages(params)

  # Remove any params that the API won't recognise
  params = remove_non_existant_parameters(params) # DO THIS LAST

  print('Cleaned up parameters: ' + str(params))
  return params



def format_params_as_string(cleaned_user_input):
  """Return a list of parameters formatted for API header, from class list of inputs"""

  # Standard URL encoding
  return urllib.parse.urlencode(cleaned_user_input, quote_via=urllib.parse.quote_plus)
