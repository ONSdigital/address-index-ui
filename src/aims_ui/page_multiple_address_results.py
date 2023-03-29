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

  #TODO Set To FALSE (debug only)----------------------------------------------
  if True:
    headers = ['JOBID', 'STATUS', 'USER ID', 'RECS PROCESSED', 'DOWNLOAD LINK']
    testUrl = 'https://storage.googleapis.com/results_4_179270555351/results_4.csv.gz?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=compute%40ons-aims-analysis-prod.iam.gserviceaccount.com%2F20230327%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230327T073312Z&X-Goog-Expires=900&X-Goog-SignedHeaders=host&X-Goog-Signature=32fd599993be98e58072c29e47deaa9982594cf37587af9a56adff099ddb468a35b26eb26d8279ddd2a6de57f2c0a38ca3462e369a158850e78514e053952e5d98bd9fe1dd8774848048b846f568e09399bf51f46b2b66f984ac9dd7445d40cd3cd7e74e5a644e254f468a2a1608e0888af16bf2131221052bbf3d8d3d8b01341f76f773151cb22e37d34d8c631d94de3a4e80af936099bb059828d495cb76ae2e1e77dd0cb1b475cf9c38dd2a689e227bfc237d319cc958e4ac63988ecbb3fe0878472bf4eecbf1fae0486ba8515f3bfa8ee66118d9cc1e091114058a85e51c1c3454666cf95f5af30b235eba09021cef41b03d433b9456cba8710a17e897ca'


    endpoints = get_endpoints(called_from=page_name)
    formatted_results =[
        ['22', '10,000 of A Jillion','bob' , 'complete' ,  f'<a href="{testUrl}">job_id1</a>'], 
        ['22', '10,000 of A Jillion','bob' , 'complete' ,  f'<a href="{testUrl}">job_id2</a>'], 
        ['22', '10,000 of A Jillion','bob' , 'complete' ,  f'<a href="{testUrl}">job_id3</a>'], 
        ['22', '10,000 of A Jillion','bob' , 'complete' ,  f'<a href="{testUrl}">job_id4</a>'], 
                        ]

    jobs = create_table(headers, formatted_results)

    # Download the zip

    return render_template(
        f'{page_name}.html',
        endpoints=endpoints,
        jobs=jobs,
    )

  #TODO SET TO FALSE --------------------------------------------------

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
