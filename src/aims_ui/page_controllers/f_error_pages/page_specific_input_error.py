from flask import render_template
from aims_ui import app
from aims_ui.models.get_endpoints import get_endpoints
from aims_ui.page_controllers.f_error_pages.page_error import page_error
from aims_ui.models.get_fields import get_fields
from aims_ui.page_helpers.pages_location_utils import get_page_location
""" When an error message would be better shown next to an input in the Design System, manage that here """


def page_specific_input_error(
    page_name_with_error,
    user_input,
    primary_error_message,
):
  endpoints = get_endpoints(called_from=page_name_with_error)
  page_location = get_page_location(
      endpoints, page_name_with_error)
  # Get the fields that are on the page with the error
  searchable_fields = get_fields(page_name_with_error)

  # Knowing the error from the API, get the databasename of the feild that matches the error 
  name_of_broken_field = match_api_error_message_to_name_of_field(
      primary_error_message)

  # Loop through all fields on the page, set it's "error_message" to the primary_error_message from the API
  for field in searchable_fields:
    if field.database_name == name_of_broken_field:
      field.error_message = primary_error_message

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
  if 'UPRNs must be numeric' in primary_error_message:
    return 'uprn'
  if 'UPRN request didn' in primary_error_message:
    return 'uprn'