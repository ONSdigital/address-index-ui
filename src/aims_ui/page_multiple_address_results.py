import os
from flask_login import login_required
from flask import render_template, request, session, send_file, url_for
from . import app
from .models.get_endpoints import get_endpoints
from .api_interaction import api, all_jobs
from .table_utils import create_table
import json
import csv

page_name = 'multiple_address_results'


@login_required
@app.route(f'/multiple_address_results', methods=['GET', 'POST'])
def multiple_address_results():
  endpoints = get_endpoints(called_from=page_name)

  for endpoint in endpoints:
    endpoint.current_selected_endpoint = url_for(page_name)

  headers = ['JOBID','STATUS', 'RECS PROCESSED','DOWNLOAD LINK']
  results = all_jobs()
  print(results)
  #TODO remove testing only
  results = [{'-', '10,000 of 67,924', 'in-progress', '42'}]
  jobs = []
  jobs = create_table(headers, results)

  return render_template(
      f'{page_name}.html',
      endpoints=endpoints,
      jobs=jobs,
  )

