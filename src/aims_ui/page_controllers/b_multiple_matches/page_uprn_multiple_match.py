from flask import render_template, request, send_file, session
from flask_login import login_required
from requests.exceptions import ConnectionError

from aims_ui import app
from aims_ui.models.get_endpoints import get_endpoints
from aims_ui.models.get_fields import get_fields
from aims_ui.page_controllers.b_multiple_matches.utils.multiple_match_file_upload_utils import check_valid_upload
from aims_ui.page_controllers.b_multiple_matches.utils.submit_multiple_match_uprn import uprn_multiple_address_match
from aims_ui.page_controllers.f_error_pages.page_error_annotation_multiple import page_error_annotation_multiple
from aims_ui.page_helpers.cookie_utils import delete_input, load_save_store_inputs
from aims_ui.page_helpers.error.error_utils import error_page_connection
from aims_ui.app_helpers.google_utils import get_current_group
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

  searchable_fields = get_fields(page_name)

  if request.method == 'GET':
    delete_input(session)

    return render_template(
        page_location,
        bulk_limits=bulk_limits,
        searchable_fields=searchable_fields,
        endpoints=get_endpoints(called_from=page_name),
    )

  try:
    all_user_input = load_save_store_inputs(
        searchable_fields,
        request,
        session,
    )
  except Exception as e:
    return page_error_annotation_multiple(page_name, {}, e)

  file = request.files['file_upload']

  try:
    file_valid, error_description, error_title = check_valid_upload(
        file, bulk_limits.get('limit_uprn_match'), called_from='uprn')
  except Exception as e:
    return page_error_annotation_multiple(page_name, all_user_input,
                                          e.error_description)

  if not file_valid:
    return page_error_annotation_multiple(page_name, all_user_input,
                                          e.error_description)

  try:
    full_results, line_count = uprn_multiple_address_match(
        file, all_user_input)
  except ConnectionError as e:
    return error_page_connection(page_name, all_user_input, e)

  return send_file(full_results,
                   mimetype='text/csv',
                   download_name=f'result_size_{line_count}.csv',
                   as_attachment=True)
