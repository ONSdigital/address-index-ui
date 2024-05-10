import os
from flask import render_template, request, session, send_file
from requests.exceptions import ConnectionError
from flask_login import login_required
from werkzeug.utils import secure_filename
from . import app
from .cookie_utils import save_input, load_input, get_all_inputs, delete_input, load_save_store_inputs
from .api_interaction import api
from .multiple_match_lookup import multiple_address_match_original
from .models.get_endpoints import get_endpoints
from .models.get_fields import get_fields
from .models.get_addresses import get_addresses
from .upload_utils import check_valid_upload
from .page_error import page_error
from .upload_utils import FileUploadException
from .security_utils import check_user_has_access_to_page
from .google_utils import get_username, get_current_group
import json
import csv
from time import sleep
import logging

page_name = 'multiple_address_original'


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
  removed_pages = current_group.get('pages_to_remove', [])

  searchable_fields = get_fields(
      page_name)  # This should be handled with error checking in future
  return render_template(
      f'{page_name}.html',
      error_description=error_description,
      error_title=error_title,
      endpoints=get_endpoints(called_from=page_name),
      searchable_fields=searchable_fields,
      table_results=table_results,
      results_summary_table=results_summary_table,
      results_page=True,
      bulk_limits=bulk_limits,
      removed_pages=removed_pages,
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
  group_name = current_group.get('name')
  bulk_limits = current_group.get('bulk_limits')
  removed_pages = current_group.get('pages_to_remove', [])
  logging.error('Current gorup: ' + str(current_group))
  logging.error('Current groupname: ' + str(group_name))
  logging.error('Current remvoed pages: ' + str(removed_pages))

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
        removed_pages=removed_pages,
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
            file, all_user_input, group_name=group_name, download=True)
      except ConnectionError as e:
        return page_error(None, e, page_name)

      return send_file(full_results,
                       mimetype='text/csv',
                       download_name=f'result_size_{line_count}.csv',
                       as_attachment=True)

    elif results_type == 'Display':
      try:
        table_results, results_summary_table = multiple_address_match_original(
            file, all_user_input, group_name=group_name, download=False)
      except ConnectionError as e:
        return page_error(None, e, page_name)

      return final(searchable_fields,
                   bulk_limits,
                   table_results=table_results,
                   results_summary_table=results_summary_table)
