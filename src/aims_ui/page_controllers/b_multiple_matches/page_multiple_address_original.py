import os
from flask import render_template, request, session, send_file
from requests.exceptions import ConnectionError
from flask_login import login_required
from werkzeug.utils import secure_filename
from . import app
from aims_ui.page_helpers.cookie_utils import save_input, load_input, get_all_inputs, delete_input, load_save_store_inputs
from aims_ui.page_helpers.api.api_interaction import api
from aims_ui.models.get_endpoints import get_endpoints
from aims_ui.models.get_fields import get_fields
from aims_ui.models.get_addresses import get_addresses
from aims_ui.page_helpers.security_utils import check_user_has_access_to_page
from aims_ui.page_helpers.google_utils import get_username, get_current_group
from aims_ui.page_error import page_error
from .utils.multiple_match_lookup import multiple_address_match_original
from .utils.upload_utils import check_valid_upload, FileUploadException
import json
import csv
from time import sleep

page_name = 'multiple_address_original'
pages_location = app.config.get('AIMS_UI_PAGES_LOCATION', '')


def final(
    bulk_limits,
    searchable_fields,
    error_description='',
    error_title='',
    results_summary_table='',
    table_results='',
):

  current_group = get_current_group()
  bulk_limits = current_group.get('bulk_limits')

  searchable_fields = get_fields(
      page_name)  # This should be handled with error checking in future
  return render_template(
      f'{pages_location}{page_name}.html',
      error_description=error_description,
      error_title=error_title,
      endpoints=get_endpoints(called_from=page_name),
      searchable_fields=searchable_fields,
      table_results=table_results,
      results_summary_table=results_summary_table,
      results_page=True,
      bulk_limits=bulk_limits,
  )


# In the event of a file being too large, send this custom template
@app.errorhandler(413)
def request_entity_too_large(error):
  # TODO searchable fields unable to set page values to what they were before error
  searchable_fields = get_fields(page_name)

  for field in searchable_fields:
    if field.database_name == 'display-type':
      field.set_radio_status('Download')

  return final(
      searchable_fields,
      'File size is too large. Please enter a file no larger than 2 MB',
      'File Size Error')


@login_required
@app.route(f'/{page_name}', methods=['GET', 'POST'])
def multiple_address_original():
  endpoints = get_endpoints(called_from=page_name)
  access = check_user_has_access_to_page(page_name, endpoints)
  if access != True:
    return access

  current_group = get_current_group()
  bulk_limits = current_group.get('bulk_limits')

  if request.method == 'GET':
    delete_input(session)
    searchable_fields = get_fields(page_name)
    # Set default selected radio
    for field in searchable_fields:
      if field.database_name == 'display-type':
        field.set_radio_status('Download')

    return render_template(
        f'{page_name}.html',
        searchable_fields=searchable_fields,
        endpoints=get_endpoints(called_from=page_name),
        bulk_limits=bulk_limits,
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
        file, bulk_limits.get('limit_mini_bulk'))
  except FileUploadException as e:
    return final(searchable_fields,
                 bulk_limits,
                 error_description=e.error_description,
                 error_title=e.error_title)

  if not file_valid:
    # File invalid? Return error
    return final(searchable_fields,
                 bulk_limits,
                 error_description=error_description,
                 error_title=error_title)
  else:
    for field in searchable_fields:
      if field.database_name == 'display-type':
        results_type = field.get_selected_radio()

    if results_type == 'Download':
      try:
        full_results, line_count = multiple_address_match_original(
            file, all_user_input, download=True)
      except ConnectionError as e:
        return page_error(None, e, page_name)

      return send_file(full_results,
                       mimetype='text/csv',
                       download_name=f'result_size_{line_count}.csv',
                       as_attachment=True)

    elif results_type == 'Display':
      try:
        table_results, results_summary_table = multiple_address_match_original(
            file, all_user_input, download=False)
      except ConnectionError as e:
        return page_error(None, e, page_name)

      return final(searchable_fields,
                   bulk_limits,
                   table_results=table_results,
                   results_summary_table=results_summary_table)
