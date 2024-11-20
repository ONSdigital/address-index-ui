import logging

from flask import render_template, request

from aims_ui.models.get_endpoints import get_endpoints
from aims_ui.models.get_fields import get_fields
from aims_ui.page_helpers.google_utils import get_current_group
from aims_ui.page_helpers.pages_location_utils import get_page_location

""" Manage errors specific to multiple match pages """


def page_error_annotation_multiple(
    page_name_with_error,
    user_input,
    primary_error_message,
    override_input_name=None,
):
  logging.error('Error on page: {}'.format(page_name_with_error))
  logging.error('Error message: {}'.format(primary_error_message))

  # Convert the primary error message to a string if it's an exception
  primary_error_message = convert_exception_to_error_message(
      primary_error_message)

  endpoints = get_endpoints(called_from=page_name_with_error)
  page_location = get_page_location(endpoints, page_name_with_error)

  # Get the bulk limits info
  current_group = get_current_group()
  bulk_limits = current_group.get('bulk_limits')

  # Get the fields that are on the page with the error
  searchable_fields = get_fields(page_name_with_error)

  # Knowing the error from the API, get the databasename of the feild that matches the error
  name_of_broken_field = match_api_error_message_to_name_of_field(
      primary_error_message, page_name_with_error)

  # Override the input name if it's been set as a parameter
  if override_input_name:
    name_of_broken_field = override_input_name

  # Loop through all fields on the page, set it's "error_message" to the primary_error_message from the API
  for field in searchable_fields:
    if field.database_name == name_of_broken_field:
      field.error_message = primary_error_message
      print('Error message: {}'.format(primary_error_message))
      print('on field: {}'.format(field.database_name))

  # Set the limit to whatever it was before
  limit = request.form.get('limit')
  for field in searchable_fields:
    if field.database_name == 'limit':
      field.previous_value = limit

  return render_template(
      page_location,
      endpoints=endpoints,
      searchable_fields=searchable_fields,
      bulk_limits=bulk_limits,
      uprn_bulk_limit=400,
  )


def convert_exception_to_error_message(primary_error_message):
  """ Convert an exception to a string """

  # If the primary error message is an instance of an Exception
  if isinstance(primary_error_message, Exception):
    primary_error_message = str(primary_error_message)

  if 'Expecting value: line 2 column 1' in primary_error_message:
    # Error message when there's a connection error to the API
    return 'Connection error to the API'

  if 'Request Entity Too Large' in primary_error_message:
    # User friendly error message when the file is too large
    primary_error_message = 'File size is too large. Please enter a file no larger than 2 MB'
    return primary_error_message

  if 'Limit Parameter Error' in primary_error_message:
    # User friendly error message when the limit parameter is not a positive integer
    primary_error_message = f'Limit parameter must be a positive integer between 1 and 10'
    return primary_error_message

  return primary_error_message


def match_api_error_message_to_name_of_field(primary_error_message,
                                             page_name_with_error):
  """ Given an error message, return the name of the field that caused the error """
  default_element_for_error_message = 'file_upload'

  # If the primary error message is a string, decide which element to return based on the error message
  if 'Record Limit Exceeded' in primary_error_message:
    return 'file_upload'

  if 'Limit parameter' in primary_error_message:
    return 'limit'

  return default_element_for_error_message
