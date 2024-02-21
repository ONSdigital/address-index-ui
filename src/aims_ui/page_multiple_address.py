import json
import logging
import csv
from time import sleep
import os
from flask import render_template, request, session, send_file
from requests.exceptions import ConnectionError
from flask_login import login_required
from werkzeug.utils import secure_filename
from . import app
from .cookie_utils import save_input, load_input, get_all_inputs, delete_input, load_save_store_inputs
from .api_interaction import api
from .multiple_match_lookup import multiple_address_match
from .models.get_endpoints import get_endpoints
from .models.get_fields import get_fields
from .models.get_addresses import get_addresses
from .upload_utils import check_valid_upload
from .page_error import page_error
from .upload_utils import FileUploadException
from .security_utils import check_user_has_access_to_page

page_name = 'multiple_address'


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
def multiple_address():
  endpoints = get_endpoints(called_from=page_name)
  access = check_user_has_access_to_page(page_name, endpoints)
  if access != True:
    return access

  current_group = get_current_group()
  if username in current_group.get('usernames'):
    reduced = True
    limit = current_group.get('limit_mini_bulk')
  else:
    reduced = False
    limit = 5000



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
        endpoints=endpoints,
        limit=limit,
    )

  if request.method == 'POST':
    searchable_fields = get_fields(page_name)
    all_user_input = load_save_store_inputs(
        searchable_fields,
        request,
        session,
    )

    file = request.files['file']

    try:
      # Validate file
      file_valid, error_description, error_title = check_valid_upload(
          file, limit=1000000)
    except FileUploadException as e:
      return final(searchable_fields,
                   error_description=e.error_description,
                   error_title=e.error_title)

    if file_valid:
      multiple_address_match(file, all_user_input, download=True)
      return final(all_user_input)


def final(all_user_input,
          error_description='',
          error_title='',
          results_summary_table='',
          table_results=''):
  searchable_fields = get_fields(page_name)

  return render_template(
      f'{page_name}.html',
      error_description=error_description,
      error_title=error_title,
      endpoints=endpoints,
      searchable_fields=searchable_fields,
      table_results=table_results,
      results_summary_table=results_summary_table,
      results_page=True,
      limit=limit,
  )
