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
import json
import os 

page_name = 'multiple_address'

ALLOWED_EXTENSIONS = {'csv'}
def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@login_required
@app.route(f'/{page_name}', methods=['GET', 'POST'])
def multiple_address():

  if request.method == 'GET':
    delete_input(session)
    searchable_fields=get_fields(page_name)
    # Set default selected radio
    for field in searchable_fields:
      if field.database_name=='display-type':
        field.set_radio_status('Download')

    return render_template(
        f'{page_name}.html',
        searchable_fields=searchable_fields,
        endpoints=get_endpoints(called_from=page_name),)


  def final(
      searchable_fields,
      error_description='', 
      error_title = '',):

      return render_template(
          f'{page_name}.html',
          error_description=error_description,
          error_type=error_title,
          endpoints=get_endpoints(called_from=page_name),
          searchable_fields=searchable_fields,
          results_page=True, ) 

  if request.method == 'POST':

    searchable_fields = get_fields(page_name)
    all_user_input = load_save_store_inputs(
        searchable_fields,
        request,
        session, )

    file = request.files['file']
    file_size = int(os.fstat(file.fileno()).st_size) / 1000000 # In MB
    max_file_size = 1 # In MB

    if file.filename == '':
      return final(
          searchable_fields,
          error_description='Select a file that is a CSV ', 
          error_title='File Type Error')

    if file_size > max_file_size:
      return final(
          searchable_fields,
          error_description=f'File size is too large. Please enter a file no larger than {max_file_size} MB', 
          error_title='File Size Error')

    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      # 1. Work out how to differenciate between "Downlaod results" button and "View results" BUtton

      full_results = multiple_address_match(file, {}, app)

      return send_file(full_results,
                     mimetype='text/csv',
                     attachment_filename='YouJustUploadedMe.csv',
                     as_attachment=True)


