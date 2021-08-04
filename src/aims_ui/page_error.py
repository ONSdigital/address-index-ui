from flask import render_template
from .models.get_endpoints import get_endpoints


def page_error(
    api_response,
    page_name,
):

  if len(api_response.json().get('errors', [])) > 0:
    error_description = api_response.json().get('errors',[''])[0].get('message',None) 
  else:
    error_description = f'Expected 200 response, got {api_response.status_code}. Response is {api_response}'


  return (render_template(
      'error.html',
      endpoints=get_endpoints(called_from=page_name),
      error_name='Error interacting with API',
      error_description=error_description,
  ))
