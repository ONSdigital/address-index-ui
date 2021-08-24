import os
from flask import render_template, request, session, send_file
from flask_login import login_required
from werkzeug.utils import secure_filename
from . import app
from .cookie_utils import save_input, load_input, get_all_inputs, delete_input, load_save_store_inputs
from .api_interaction import api, multiple_address_match
from .models.get_endpoints import get_endpoints
from .models.get_fields import get_fields
from .models.get_addresses import get_addresses
from .upload_utils import check_valid_upload
import json
import csv

page_name = 'multiple_address'
 
def final(searchable_fields,
          error_description='',
          error_title='',
          table_results=''):

  return render_template(
      f'{page_name}.html',
      error_description=error_description,
      error_title=error_title,
      endpoints=get_endpoints(called_from=page_name),
      searchable_fields=searchable_fields,
      table_results=table_results,
      results_page=True,
  )

# In the event of a file being too large, send this custom template
@app.errorhandler(413)
def request_entity_too_large(error):
    return final(get_fields(page_name), 
        f'File size is too large. Please enter a file no larger than 2 MB',
        'File Size Error')

@login_required
@app.route(f'/{page_name}', methods=['GET', 'POST'])
def multiple_address():

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
    )


  if request.method == 'POST':

    searchable_fields = get_fields(page_name)
    all_user_input = load_save_store_inputs(
        searchable_fields,
        request,
        session,
    )

    file = request.files['file']

    file_valid, error_description, error_title = check_valid_upload(file)

    if file_valid:
      for field in searchable_fields:
        if field.database_name == 'display-type':
          results_type = field.get_selected_radio()

      if results_type == 'Download':
        full_results, line_count = multiple_address_match(file, {},
                                                          download=True)

        return send_file(full_results,
                         mimetype='text/csv',
                         attachment_filename=f'result_size_{line_count}.csv',
                         as_attachment=True)
      elif results_type == 'Display':
        table_results = multiple_address_match(file, {}, download=False)
        return final(searchable_fields, table_results=table_results)
    else:
      return final(searchable_fields,
                   error_description=error_description,
                   error_title=error_title)

