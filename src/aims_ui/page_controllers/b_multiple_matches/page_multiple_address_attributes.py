from flask_login import login_required
from flask import render_template, request
from aims_ui import app
from .utils.multiple_match_api_utils import get_tag_data, job_data_by_current_user
from aims_ui.page_helpers.security_utils import check_user_has_access_to_page
from aims_ui.page_helpers.table_utils import create_table
from aims_ui.models.get_endpoints import get_endpoints
from aims_ui.page_helpers.pages_location_utils import get_page_location
from aims_ui.page_helpers.google_utils import get_username, get_current_group
from aims_ui.page_controllers.b_multiple_matches.utils.multiple_address_results import get_results_plus_metadata
import json

page_name = 'multiple_address_attributes'


@login_required
@app.route(f'/multiple_address_attributes', methods=['GET', 'POST'])
def multiple_address_attributes():
  endpoints = get_endpoints(called_from=page_name)
  access = check_user_has_access_to_page(page_name)
  if access != True:
    return access
  page_location = get_page_location(endpoints, page_name)

  username = get_username()
  current_group = get_current_group()
  bulk_limits = current_group.get('bulk_limits')

  headers = [
      'JOBID', 'NAME', 'STATUS', 'USER ID', 'HEADER ROW', 'PAF OR NAG', 'RECS PROCESSED',
      'DOWNLOAD LINK'
  ]

  endpoints = get_endpoints(called_from=page_name)

  # Load testing values for testing mode
  if app.config.get('FLASK_ENV') == 'TESTING':
    job_id = 6

    formatted_results = [
        [
            '22', 'Example', '10,000 of A Jillion', 'bob', 'True', 'PAF' 'complete',
            f'<a href="/downloads/googlefiledownload{job_id}">job_id {job_id}</a>'
        ],
    ]

    jobs = create_table(headers, formatted_results)

    # Download the zip
    return render_template(
        page_location,
        endpoints=endpoints,
        jobs=jobs,
        bulk_limits=bulk_limits,
    )

  # Get the "include_old_jobs" query parameter, default to "false
  include_old_jobs = request.args.get('include_old_jobs',
                                      default='false').lower()
  # Sanetise the input
  include_old_jobs = True if include_old_jobs == 'true' else False

  jobs_data = job_data_by_current_user(include_old_jobs)
  jobs_data_plus_metadata = get_results_plus_metadata(jobs_data)

  # Format the info for each job to appear in the UI table
  jobs_data_plus_metadata_table_rows = [[
      job.get('jobid'),
      job.get('jobname'),
      job.get('status'),
      job.get('username'),
      job.get('header_row_export'),
      job.get('paf_nag_preference'),
      job.get('recssofarmessage'),
      job.get('downloadlink'),
  ] for job in jobs_data_plus_metadata]

  # EXAMPLE results format
  # results = [
  #   ['200', 'da', 'progress', USER ID, HEADER ROW, PAF OR NAG, RECS PROCESSED, DOWNLOAD LINK]
  #   [JOBID, NAME, STATUS, USER ID, HEADER ROW, PAF OR NAG, RECS PROCESSED, DOWNLOAD LINK]

  jobs_table = []
  jobs_table = create_table(headers, jobs_data_plus_metadata_table_rows)

  return render_template(
      page_location,
      endpoints=endpoints,
      jobs=jobs_table,
      bulk_limits=bulk_limits,
  )
