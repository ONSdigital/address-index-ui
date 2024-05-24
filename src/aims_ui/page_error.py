from flask import render_template
import logging
from aims_ui import app
from aims_ui.models.get_endpoints import get_endpoints
from aims_ui.page_helpers.pages_location_utils import get_page_location_non_endpoint


def page_error(
    api_response,
    page_name,
    connection_error=False,
    override_error_description='',
    override_error_name='',
):

  page_location = get_page_location_non_endpoint('error')

  if override_error_name != '':
    error_name = override_error_name
  if override_error_description != '':
    error_description = override_error_description

  else:
    error_name = 'Error interacting with API',
    if not connection_error:
      api_errors = api_response.json().get('errors', [])
      if len(api_errors) > 0:
        error_description = api_errors[0].get('message')
      else:
        error_description = f'Expected 200 response, got {api_response.status_code}. Response is {api_response}'
    else:
      # Connection error - AIMS service is unavailable
      error_description = f'Sorry, there is a problem with the service right now. <a href="mailto:ai.users@ons.gov.uk?Subject=Error%20Report&Body=Page:{page_name}%0D%0AProblem%20Details:">Contact Us </a> to report the problem and request support'

  logging.error(error_description)

  return (render_template(
      page_location,
      endpoints=get_endpoints(called_from=page_name),
      error_name=error_name,
      error_description=error_description,
  ))
