from flask import render_template
from .models.get_endpoints import get_endpoints


class PageErrorException(Exception):
  """Exception raised for errors from the API response"""
  def __init__(self, error_title='', error_description=''):
    self.error_title = error_title
    self.error_description = error_description
    super().__init__(self.error_title)


def page_error(
    api_response,
    page_name,
    connection_error=False,
):

  if not connection_error:
    api_errors = api_response.json().get('errors', [])
    if len(api_errors) > 0:
      error_description = api_errors[0].get('message')
    else:
      error_description = f'Expected 200 response, got {api_response.status_code}. Response is {api_response}'
  else:
    # Connection error - AIMS service is unavailable
    error_description = f'Sorry, there is a problem with the service right now. <a href="mailto:ai.users@ons.gov.uk?Subject=Error%20Report&Body=Page:{page_name}%0D%0AProblem%20Details:">Contact Us </a> to report the problem and request support'

  return (render_template(
      'error.html',
      endpoints=get_endpoints(called_from=page_name),
      error_name='Error interacting with API',
      error_description=error_description,
  ))
