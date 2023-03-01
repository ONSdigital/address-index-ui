import os
from flask_login import login_required
from flask import render_template, request, session, send_file, url_for
from . import app
from .models.get_endpoints import get_endpoints
from .api_interaction import api, job_data_by_user_id, job_result_formatter
from .table_utils import create_table
import json
import csv

page_name = 'multiple_address_results'


@login_required
@app.route(f'/multiple_address_results', methods=['GET', 'POST'])
def multiple_address_results():

  #TODO REMOVE

  headers = ['JOBID', 'STATUS', 'USER ID', 'RECS PROCESSED', 'DOWNLOAD LINK']

  endpoints = get_endpoints(called_from=page_name)
  formatted_results =[['22', '10,000 of A Jillion','bob' 
                       , 'complete' , 
                        '<a href="/downloads/googlefiledownload32">Download Job {job_id} Here</a>'
                       ]]

  jobs = create_table(headers, formatted_results)

  # Download the zip

  return render_template(
      f'{page_name}.html',
      endpoints=endpoints,
      jobs=jobs,
  )

  #TODO REMOVE

  endpoints = get_endpoints(called_from=page_name)

  user_email = request.headers.get('X-Goog-Authenticated-User-Email',
                                   'UserNotLoggedIn')

  user_email = user_email.replace('accounts.google.com:', '')
  user_email = user_email.replace('@ons.gov.uk', '')

  headers = ['JOBID', 'STATUS', 'USER ID', 'RECS PROCESSED', 'DOWNLOAD LINK']
  results = job_data_by_user_id(user_email).json().get('jobs', [])
  formatted_results = [[
      job.get('jobid'),
      job.get('status'),
      job.get('userid'), f"{job.get('recssofar')}  of  {job.get('totalrecs')}",
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
  )
