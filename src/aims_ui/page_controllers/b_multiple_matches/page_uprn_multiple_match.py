from flask import render_template, request, send_file, session
from flask_login import login_required
from requests.exceptions import ConnectionError

from aims_ui import app
from aims_ui.models.get_endpoints import get_endpoints
from aims_ui.models.get_fields import get_fields
from aims_ui.page_controllers.b_multiple_matches.utils.multiple_match_file_upload_utils import (
    FileUploadException,
    check_valid_upload
)
from aims_ui.page_controllers.b_multiple_matches.utils.submit_multiple_match_uprn import uprn_multiple_address_match
from aims_ui.page_helpers.cookie_utils import delete_input, load_save_store_inputs
from aims_ui.page_helpers.error.error_utils import error_page_connection
from aims_ui.page_helpers.google_utils import get_current_group
from aims_ui.page_helpers.pages_location_utils import get_page_location
from aims_ui.page_helpers.security_utils import check_user_has_access_to_page

page_name = 'uprn_multiple_match'


@login_required
@app.route(f'/{page_name}', methods=['GET', 'POST'])
def uprn_multiple_match():
  endpoints = get_endpoints(called_from=page_name)
  access = check_user_has_access_to_page(page_name)
  if access != True:
    return access
  page_location = get_page_location(endpoints, page_name)

  current_group = get_current_group()
  bulk_limits = current_group.get('bulk_limits')
  uprn_bulk_limit = bulk_limits.get('limit_uprn_match')

  if request.method == 'GET':
    delete_input(session)
    searchable_fields = get_fields(page_name)

    return render_template(
        page_location,
        uprn_bulk_limit=uprn_bulk_limit,
        searchable_fields=searchable_fields,
        endpoints=get_endpoints(called_from=page_name),
    )

  searchable_fields = get_fields(page_name)
  all_user_input = load_save_store_inputs(
      searchable_fields,
      request,
      session,
  )

  file = request.files['file']

  try:
    file_valid, error_description, error_title = check_valid_upload(
        file, uprn_bulk_limit, called_from='uprn')
  except FileUploadException as e:
    return error_response(searchable_fields,
                          error_description=e.error_description,
                          error_title=e.error_title)

  if not file_valid:
    # File invalid? Return error
    return error_response(searchable_fields,
                          page_location,
                          error_description=error_description,
                          error_title=error_title)

  try:
    full_results, line_count = uprn_multiple_address_match(
        file, all_user_input)
  except ConnectionError as e:
    return error_page_connection(page_name, all_user_input, e)

  return send_file(full_results,
                   mimetype='text/csv',
                   download_name=f'result_size_{line_count}.csv',
                   as_attachment=True)


def error_response(searchable_fields,
                   page_location,
                   error_description='',
                   error_title='',
                   results_summary_table='',
                   table_results=''):

  current_group = get_current_group()
  bulk_limits = current_group.get('bulk_limits')
  uprn_bulk_limit = bulk_limits.get('limit_uprn_match')

  return render_template(
      page_location,
      uprn_bulk_limit=uprn_bulk_limit,
      error_description=error_description,
      error_title=error_title,
      endpoints=get_endpoints(called_from=page_name),
      searchable_fields=searchable_fields,
      table_results=table_results,
      results_summary_table=results_summary_table,
  )


# In the event of a file being too large, send this custom template
@app.errorhandler(413)
def request_entity_too_large(error):
  # TODO searchable fields unable to set page values to what they were before error
  searchable_fields = get_fields(page_name)

  for field in searchable_fields:
    if field.database_name == 'display-type':
      field.set_radio_status('Download')

  return error_response(
      searchable_fields,
      'File size is too large. Please enter a file no larger than 2 MB',
      'File Size Error')
