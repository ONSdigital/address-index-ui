import logging
from flask import render_template
from aims_ui import app
from aims_ui.models.get_endpoints import get_endpoints
from aims_ui.page_controllers.f_error_pages.page_error import page_error
from aims_ui.models.get_fields import get_fields
from aims_ui.page_helpers.pages_location_utils import get_page_location
from aims_ui.page_helpers.google_utils import get_current_group
""" Manage errors specific to multiple match pages """


def page_error_annotation_multiple(
    page_name_with_error,
    user_input,
    primary_error_message,
    override_input_name=None,
):
  logging.error('Error on page: {}'.format(page_name_with_error))
  logging.error('Error message: {}'.format(primary_error_message))

  endpoints = get_endpoints(called_from=page_name_with_error)
  page_location = get_page_location(endpoints, page_name_with_error)

  # Get the bulk limits info
  current_group = get_current_group()
  bulk_limits = current_group.get('bulk_limits')

  # Get the fields that are on the page with the error
  searchable_fields = get_fields(page_name_with_error)

  # Knowing the error from the API, get the databasename of the feild that matches the error
  name_of_broken_field = match_api_error_message_to_name_of_field(
      primary_error_message)

  # Override the input name if it's been set as a parameter
  if override_input_name:
    name_of_broken_field = override_input_name

  # Loop through all fields on the page, set it's "error_message" to the primary_error_message from the API
  for field in searchable_fields:
    if field.database_name == name_of_broken_field:
      field.error_message = primary_error_message
      print('Error message: {}'.format(primary_error_message))
      print('on field: {}'.format(field.database_name))

  return render_template(
      page_location,
      endpoints=endpoints,
      searchable_fields=searchable_fields,
      bulk_limits=bulk_limits,
  )


def match_api_error_message_to_name_of_field(primary_error_message):
  """ Given an error message, return the name of the field that caused the error """
  if 'Record Limit Exceeded' in primary_error_message:
    return 'file_upload'

  return 'file_upload'  # Default to file
