import os
from flask import render_template, request, session
from flask_login import login_required
from werkzeug.utils import secure_filename
from . import app
from .cookie_utils import save_input, load_input, get_all_inputs, delete_input, load_save_store_inputs
from .api_interaction import api
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

  def final(
      error_description='', 
      error_type = '',):
    return render_template(
        f'{page_name}.html',
        error_description=error_description,
        error_type=error_type,
        endpoints=get_endpoints(called_from=page_name),
        results_page=True, ) 

  if request.method == 'POST':
    if 'file' not in request.files:
      return redirect(request.url)

    file = request.files['file']
    file_size = int(os.fstat(file.fileno()).st_size) / 1000000 # In MB


    if file.filename == '':
      return final(
          error_description='Select a file that is a CSV ', 
          error_type='file-error')

    if file_size > 2:
      return final(
          error_description='File size is too large. Please enter a file no larger than {max_file_size}', 
          error_type='file-size')

    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      print(file)
      return final()

  delete_input(session)
  return render_template(
      f'{page_name}.html',
      searchable_fields=get_fields(page_name),
      endpoints=get_endpoints(called_from=page_name),
  )
