import os
from flask import render_template, request, session, send_file
from requests.exceptions import ConnectionError
from flask_login import login_required
from . import app
from .cookie_utils import save_input, load_input, get_all_inputs, delete_input, load_save_store_inputs, save_epoch_number
from .api_interaction import api
from .models.get_endpoints import get_endpoints
from .models.get_fields import get_fields
from .models.get_addresses import get_addresses
from .page_error import page_error
import json
from .upload_utils import check_valid_upload, FileUploadException
from .multiple_match_lookup import uprn_multiple_address_match_original

page_name = 'uprn_multiple_match'


@login_required
@app.route(f'/{page_name}', methods=['GET', 'POST'])
def uprn_multiple_match():

  if request.method == 'GET':
    delete_input(session)
    searchable_fields = get_fields(page_name)

    return render_template(
        f'{page_name}.html',
        searchable_fields=searchable_fields,
        endpoints=get_endpoints(called_from=page_name),
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
      file_valid, error_description, error_title = check_valid_upload(file)
    except FileUploadException as e:
      return final(searchable_fields,
                   error_description=e.error_description,
                   error_title=e.error_title)

    if not file_valid:
      # File invalid? Return error
      return final(searchable_fields,
                   error_description=error_description,
                   error_title=error_title)

    try:
      full_results, line_count = uprn_multiple_address_match_original(
          file, all_user_input)
    except ConnectionError as e:
      return page_error(None, e, page_name)

    return send_file(full_results,
                     mimetype='text/csv',
                     attachment_filename=f'result_size_{line_count}.csv',
                     as_attachment=True)

def final(searchable_fields,
          error_description='',
          error_title='',
          results_summary_table='',
          table_results=''):

  return render_template(
      f'{page_name}.html',
      error_description=error_description,
      error_title=error_title,
      endpoints=get_endpoints(called_from=page_name),
      searchable_fields=searchable_fields,
      table_results=table_results,
      results_summary_table=results_summary_table,
      results_page=True,
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


