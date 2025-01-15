from flask_login import login_required
from flask import render_template, request
from aims_ui import app
from .utils.multiple_match_api_utils import get_tag_data, job_data_by_current_user
from aims_ui.page_helpers.security_utils import check_user_has_access_to_page
from aims_ui.page_helpers.table_utils import create_table
from aims_ui.models.get_endpoints import get_endpoints
from aims_ui.page_helpers.pages_location_utils import get_page_location
from aims_ui.page_helpers.api.api_interaction import job_result_formatter
from aims_ui.page_helpers.google_utils import get_username, get_current_group

page_name = 'multiple_address_results'


@login_required
@app.route(f'/multiple_address_results', methods=['GET', 'POST'])
def multiple_address_results():
  endpoints = get_endpoints(called_from=page_name)
  access = check_user_has_access_to_page(page_name)
  if access != True:
    return access
  page_location = get_page_location(endpoints, page_name)

  username = get_username()
  current_group = get_current_group()
  bulk_limits = current_group.get('bulk_limits')

  headers = [
      'JOBID', 'NAME', 'STATUS', 'USER ID', 'HEADER ROW', 'RECS PROCESSED',
      'DOWNLOAD LINK'
  ]

  endpoints = get_endpoints(called_from=page_name)

  # Load testing values for testing mode
  if app.config.get('FLASK_ENV') == 'TESTING':
    job_id = 6

    formatted_results = [
        [
            '22', 'Example', '10,000 of A Jillion', 'bob', 'True', 'complete',
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

  results = job_data_by_current_user(include_old_jobs)

  formatted_results = [[
      job.get('jobid'),
      get_tag_data(job.get('userid')).get('user_tag'),
      job.get('status'),
      get_tag_data(job.get('userid')).get('username'),
      get_tag_data(job.get('userid')).get('header_row_export', 'NA'),
      f"{job.get('recssofar')}  of  {job.get('totalrecs')}",
      job_result_formatter(job.get('jobid'))
  ] for job in results]

  # EXAMPLE results format
  # results = [
  #   ['34', '10,000 of 67,924', 'in-progress', '-'],
  #   ['80', '30,501 of 80,924', 'in-progress', '-'],
  #   ['212', '23 of 924', 'in-progress', '-'],
  #   ['4', '40,000 of 40,000', 'complete', 'http://www.example.com'],
  #   ]

  jobs = []
  jobs = create_table(headers, formatted_results)

  return render_template(
      page_location,
      endpoints=endpoints,
      jobs=jobs,
      bulk_limits=bulk_limits,
  )
