from flask import render_template, request, send_file, session
from flask_login import login_required

from aims_ui import app
from aims_ui.models.get_endpoints import get_endpoints
from aims_ui.models.get_fields import get_fields
from aims_ui.page_controllers.f_error_pages.page_error_annotation_multiple import page_error_annotation_multiple
from aims_ui.page_helpers.cookie_utils import delete_input, load_save_store_inputs
from aims_ui.page_helpers.google_utils import get_current_group
from aims_ui.page_helpers.pages_location_utils import get_page_location
from aims_ui.page_helpers.security_utils import check_user_has_access_to_page

from .utils.multiple_match_file_upload_utils import check_valid_upload
from .utils.submit_multiple_match_from_singlesearch import (
    multiple_address_match_from_singlesearch_display,
    multiple_address_match_from_singlesearch_download
)

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

  endpoints = get_endpoints(called_from=page_name)
  page_location = get_page_location(endpoints, page_name)

  searchable_fields = get_fields(
      page_name)  # This should be handled with error checking in future
  return render_template(
      page_location,
      endpoints=endpoints,
      error_description=error_description,
      error_title=error_title,
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
  access = check_user_has_access_to_page(page_name)
  if access != True:
    return access
  page_location = get_page_location(endpoints, page_name)

  current_group = get_current_group()
  bulk_limits = current_group.get('bulk_limits')
  limit_mini_bulk = bulk_limits.get('limit_mini_bulk')
  searchable_fields = get_fields(page_name)

  if request.method == 'GET':
    delete_input(session)
    return render_template(
        page_location,
        searchable_fields=searchable_fields,
        endpoints=endpoints,
        bulk_limits=bulk_limits,
    )

  all_user_input = load_save_store_inputs(
      searchable_fields,
      request,
      session,
  )

  file = request.files['file_upload']

  try:
    file_valid, error_description, error_title = check_valid_upload(
        file, limit_mini_bulk)
  # File Upload issues appear inside upload component
  except Exception as e:
    return page_error_annotation_multiple(page_name, all_user_input,
                                          e.error_description)

  if not file_valid:
    print('FILE IS NOT VALID')
    return page_error_annotation_multiple(page_name, all_user_input,
                                          error_description)

  for field in searchable_fields:
    if field.database_name == 'display-type':
      results_type = field.get_selected_radio()

  if results_type == 'Download':
    try:
      full_results, line_count = multiple_address_match_from_singlesearch_download(
          file, all_user_input)
    except Exception as e:
      return page_error_annotation_multiple(page_name, all_user_input, e)

    return send_file(full_results,
                     mimetype='text/csv',
                     download_name=f'result_size_{line_count}.csv',
                     as_attachment=True)

  elif results_type == 'Display':
    try:
      table_results, results_summary_table = multiple_address_match_from_singlesearch_display(
          file, all_user_input)
    except Exception as e:
      return page_error_annotation_multiple(page_name, all_user_input, e)

    return final(searchable_fields,
                 bulk_limits,
                 table_results=table_results,
                 results_summary_table=results_summary_table)
