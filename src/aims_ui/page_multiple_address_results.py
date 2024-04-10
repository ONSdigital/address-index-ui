import os
from flask_login import login_required
from flask import render_template, request, session, send_file, url_for
from . import app
from .models.get_endpoints import get_endpoints
from .api_interaction import api, job_result_formatter
from .table_utils import create_table
from .security_utils import check_user_has_access_to_page
from .google_utils import get_username, get_current_group
from .multiple_address_utils import get_tag_data, job_data_by_current_user
import json
import csv

page_name = 'multiple_address_results'


@login_required
@app.route(f'/multiple_address_results', methods=['GET', 'POST'])
def multiple_address_results():
  endpoints = get_endpoints(called_from=page_name)
  access = check_user_has_access_to_page(page_name, endpoints)
  if access != True:
    return access

  username = get_username()
  current_group = get_current_group()
  if username in current_group.get('usernames'):
    reduced = True
    limit = current_group.get('limit_mini_bulk')
  else:
    reduced = False
    limit = 5000

  #TODO Set To FALSE (debug only)----------------------------------------------
  if False:
    headers = [
        'JOBID', 'NAME', 'STATUS', 'USER ID', 'HEADER ROW', 'RECS PROCESSED', 'DOWNLOAD LINK'
    ]
    job_id = 6

    endpoints = get_endpoints(called_from=page_name)
    formatted_results = [
        [
            '22', 'Example', '10,000 of A Jillion', 'bob', 'True', 'complete',
            f'<a href="/downloads/googlefiledownload{job_id}">job_id {job_id}</a>'
        ],
    ]

    jobs = create_table(headers, formatted_results)

    # Download the zip

    return render_template(
        f'{page_name}.html',
        endpoints=endpoints,
        jobs=jobs,
        reduced=reduced,
        limit=limit,
    )

  #TODO SET TO FALSE --------------------------------------------------

  endpoints = get_endpoints(called_from=page_name)
  username = get_username()

  headers = [
     'JOBID', 'NAME', 'STATUS', 'USER ID', 'HEADER ROW', 'RECS PROCESSED', 'DOWNLOAD LINK'
  ]
  results = job_data_by_current_user()

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
      f'{page_name}.html',
      endpoints=endpoints,
      jobs=jobs,
      reduced=reduced,
      limit=limit,
  )
