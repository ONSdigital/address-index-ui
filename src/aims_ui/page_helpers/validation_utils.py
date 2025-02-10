""" Validation for user inputs when it isn't handled by submitting to the API and dealing with the error """

from aims_ui.page_controllers.f_error_pages.page_error_annotation_single import page_error_annotation_single


def validate_limit(limit, validation_limit=50):
  try:
    limit = int(limit)
  except ValueError:
    return 'Limit parameter is not numeric'
  if limit > validation_limit:
    return f'Limit parameter is too large, maximum = {validation_limit}'
  return None


def validate_uprn(uprn):
  """ Check if a UPRN complies with valid format """
  # Raise exception with title 'Limit Parameter Error' and description 'Limit parameter must be a positive integer'

  basic_message = 'UPRN must be numeric. They can have up to 12 digits and have no leading zeros.'
  additional_message = ''
  if not uprn.isdigit():
    if uprn != '':
      additional_message = additional_message + '<br> The UPRN you entered is not numeric.'
    else:
      additional_message = additional_message + '<br> The UPRN you entered is blank.'

  # Check not longer than 12
  if len(uprn) > 12:
    additional_message = additional_message + '<br> The UPRN you entered is longer than 12.'

  # Check for leading zeros
  if str(uprn).startswith('0'):
    additional_message = additional_message + '<br> The UPRN you entered has leading zeros.'

  if additional_message != '':
    raise Exception('UPRN Parameter Error',
                    f'{basic_message} {additional_message}')
