import os
from flask import render_template, request, session
from flask_login import login_required
from . import app
from .cookie_utils import save_input, load_input, get_all_inputs, delete_input, load_save_store_inputs
from .api_interaction import api
from .models.get_endpoints import get_endpoints
from .models.get_fields import get_fields
from .models.get_addresses import get_addresses
import json

page_name = 'multiple_address'

from werkzeug.utils import secure_filename
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@login_required
@app.route(f'/{page_name}', methods=['GET', 'POST'])
def multiple_address():

  if request.method == 'POST':
    print('POST happening now')
    # check if the post request has the file part
    if 'file' not in request.files:
      print('No file part')
      return redirect(request.url)
    file = request.files['file']
    print(file)
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
      print('No selected file')
      return redirect(request.url)
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      print(file)
      return 'Upload sucessful i think lol'

  print('get happening')
  delete_input(session)

  return render_template(
      f'{page_name}.html',
      searchable_fields=get_fields(page_name),
      endpoints=get_endpoints(called_from=page_name),
  )


  print("POST IS HAPPENING!")
  print(request.files)
  return render_template(
      f'{page_name}.html',
      endpoints=get_endpoints(called_from=page_name),
      results_page=True,
  )
