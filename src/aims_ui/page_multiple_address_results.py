import os
from flask_login import login_required
from flask import render_template, request, session, send_file, url_for
from . import app
from .models.get_endpoints import get_endpoints
from .api_interaction import api, job_data_by_user_id, job_result_formatter
from .table_utils import create_table
from .security_utils import check_user_has_access_to_page
from .google_utils import get_username, get_current_group
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
        'JOBID', 'NAME', 'STATUS', 'USER ID', 'RECS PROCESSED', 'DOWNLOAD LINK'
    ]
    job_id = 6

    endpoints = get_endpoints(called_from=page_name)
    formatted_results = [
        [
            '22', 'Example', '10,000 of A Jillion', 'bob', 'complete',
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
      'JOBID', 'NAME', 'STATUS', 'USER ID', 'RECS PROCESSED', 'DOWNLOAD LINK'
  ]
  results = job_data_by_user_id(username).json().get('jobs', [])

  formatted_results = [[
      job.get('jobid'),
      extract_username_and_tag(job, 'tag'),
      job.get('status'),
      extract_username_and_tag(job, 'username'),
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


def extract_username_and_tag(job, returnType):
  full_user_id = job.get('userid')
  parts = full_user_id.split("::")
  # Check if the string contains the "::" separator
  if len(parts) > 1:
    username = parts[0]
    tag = parts[1]
  else:
    # If the separator is not present, treat the whole string as the username
    username = full_user_id
    tag = ""
  if returnType == 'username':
    return username
  return tag


# Felix
