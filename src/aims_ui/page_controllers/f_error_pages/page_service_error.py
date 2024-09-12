from flask import render_template
from aims_ui import app
from aims_ui.models.get_endpoints import get_endpoints
from aims_ui.page_helpers.pages_location_utils import get_error_page_location

""" User friendly error for service issues"""

def page_service_error(
    called_from_page_name,
    error_title,
    error_description,
):
  endpoints = get_endpoints(called_from=called_from_page_name)
  page_location = get_error_page_location('service_error')

  # Error description is an array of bulletpoints - convert to expected format for nunjucks
  error_description = [{'text': desc} for desc in error_description]

  return (render_template(
      page_location,
      error_title=error_title,
      error_description=error_description,
      endpoints=endpoints,
  ))
