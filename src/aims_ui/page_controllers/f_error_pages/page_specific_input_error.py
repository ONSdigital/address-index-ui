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
    result,
):
  endpoints = get_endpoints(called_from=page_name_with_error)
  page_location = get_page_location(endpoints, page_name_with_error) # I.e. singlesearch's location
  searchable_fields=get_fields('singlesearch')
  
  # {'response': 'Error calling API', 'status': {'code': 400, 'message': 'Missing parameter: input'}}
  json_result = result.json()
  api_response = json_result.get('status', {})
  api_error_message = api_response.get(
      'message', 'No further information available. Please check your inputs.')

  print(api_response)
  print(api_error_message)

  name_of_broken_field = match_api_error_message_to_name_of_field(api_error_message) 

  # Loop through all fields and find the one that matches the name of the broken field
  for field in searchable_fields:
    if field.database_name == name_of_broken_field:
      field.error_message = api_error_message

  return render_template(
      page_location,
      endpoints=endpoints,
      searchable_fields=searchable_fields,
  )

def match_api_error_message_to_name_of_field(api_error_message):
  return 'classificationfilter' 