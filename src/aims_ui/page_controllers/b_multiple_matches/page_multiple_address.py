from flask import redirect, render_template, request, session, url_for
from flask_login import login_required

import config.base
from aims_ui import app
from aims_ui.models.get_endpoints import get_endpoints
from aims_ui.models.get_fields import get_fields
from aims_ui.page_controllers.f_error_pages.page_error_annotation_multiple import page_error_annotation_multiple
from aims_ui.page_helpers.cookie_utils import delete_input, load_save_store_inputs
from aims_ui.page_helpers.google_utils import get_current_group
from aims_ui.page_helpers.pages_location_utils import get_page_location
from aims_ui.page_helpers.security_utils import check_user_has_access_to_page

from .utils.multiple_match_file_upload_utils import check_valid_upload, validate_limit_parameter
from .utils.submit_multiple_match_api import multiple_address_match
from .utils.multiple_match_api_utils import count_active_jobs

page_name = 'multiple_address'

max_jobs = config.base.BM_MAX_JOBS

@login_required
@app.route(f'/{page_name}', methods=['GET', 'POST'])
def multiple_address():
  endpoints = get_endpoints(called_from=page_name)
  access = check_user_has_access_to_page(page_name)
  if access != True:
    return access
  page_location = get_page_location(endpoints, page_name)

  current_group = get_current_group()
  bulk_limits = current_group.get('bulk_limits')

  searchable_fields = get_fields(page_name)

  if request.method == 'GET':
    delete_input(session)
    return render_template(
        page_location,
        searchable_fields=searchable_fields,
        endpoints=endpoints,
        bulk_limits=bulk_limits,
    )

  try:
    all_user_input = load_save_store_inputs(
        searchable_fields,
        request,
        session,
    )
    validate_limit_parameter(all_user_input, limit_name='limitperaddress')
  except Exception as e:
    return page_error_annotation_multiple(page_name, {}, e)

  file = request.files['file_upload']

  try:
    file_valid, error_description, error_title = check_valid_upload(
        file, bulk_limits.get('limit_vast_bulk'))
  except Exception as e:
    return page_error_annotation_multiple(page_name, all_user_input,
                                          e.error_description)

  if not file_valid:
    return page_error_annotation_multiple(page_name, all_user_input,
                                          error_description)

  jobcount = count_active_jobs()
  if jobcount > max_jobs:
    jobs_error_description = 'Bulk service too busy, please try again later'
    return page_error_annotation_multiple(page_name, all_user_input,
                                     jobs_error_description)


  multiple_address_match(file, all_user_input, download=True)

  # Using urlfor get the location of the results page and forward the user
  return redirect(
      url_for('multiple_address_results').replace('http', 'https', 1))
