from flask import render_template
import logging
from aims_ui import app
from aims_ui.models.get_endpoints import get_endpoints
from aims_ui.page_helpers.pages_location_utils import get_page_location_non_endpoint

# def page_error(
#     api_response,
#     page_name,
#     connection_error=False,
#     override_error_description='',
#     override_error_name='',
# ):


def page_error(
    called_from_page_name,
    error_title,
    error_description,
):
  page_location = get_page_location_non_endpoint('error')
  # Error description is an array of bulletpoints - convert to expected format for nunjucks
  error_description = [{'text': desc} for desc in error_description]

  return (render_template(
      page_location,
      error_title=error_title,
      error_description=error_description,
      endpoints=get_endpoints(called_from=called_from_page_name),
  ))
