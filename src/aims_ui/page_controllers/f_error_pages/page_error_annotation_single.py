import logging

from flask import render_template

from aims_ui.models.get_endpoints import get_endpoints
from aims_ui.models.get_fields import get_fields
from aims_ui.page_helpers.pages_location_utils import get_page_location
""" When an error message would be better shown next to an input in the Design System, manage that here """


def page_error_annotation_single(
    page_name_with_error,
    user_input,
    primary_error_message,
    override_input_name=None,
):
  endpoints = get_endpoints(called_from=page_name_with_error)
  page_location = get_page_location(endpoints, page_name_with_error)
  # Get the fields that are on the page with the error
  searchable_fields = get_fields(page_name_with_error)

  # Knowing the error from the API, get the databasename of the feild that matches the error
  name_of_broken_field = page_name_with_error  # Default to the "input" for the page!
  name_of_broken_field = match_api_error_message_to_name_of_field(
      primary_error_message)

  # Override the input name if it's been set as a parameter
  if override_input_name:
    logging.warning(
        'overriding "{}"'.format(name_of_broken_field) +
        ' with "{}"'.format(override_input_name) +
        '. This is probably expected if a user has input a blank value. User input is: "{}"'
        .format(user_input))
    name_of_broken_field = override_input_name

  # Loop through all fields on the page, set it's "error_message" to the primary_error_message from the API
  for field in searchable_fields:
    if field.database_name == name_of_broken_field:
      field.error_message = primary_error_message
    if field.database_name == 'input':
      field.previous_value = user_input

  return render_template(
      page_location,
      endpoints=endpoints,
      searchable_fields=searchable_fields,
  )


def match_api_error_message_to_name_of_field(primary_error_message):
  """ Given an API error message, return the name of the field that caused the error """
  if 'Missing parameter: input' in primary_error_message:
    return 'input'
  if 'Invalid classification filter value provided' in primary_error_message:
    return 'classificationfilter'
  if 'Requested Epoch is not available' in primary_error_message:
    return 'epoch'
  if 'Limit parameter is ' in primary_error_message:
    return 'limit'

  # UPRN specific errors
  if 'UPRN' in primary_error_message:
    return 'uprn'

  if 'Postcode supplied is not valid according to the UK addresses' in primary_error_message:
    return 'postcode'
