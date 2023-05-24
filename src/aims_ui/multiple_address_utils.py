import requests
import tarfile
import io
import json
from flask import request
from . import app


def job_data_by_job_id(job_id):
  url = f'/bulk-progress/{job_id}'
  r = job_api(url)
  return r


def job_api(url):
  """API helper for job endpoints """
  user_email = request.headers.get('X-Goog-Authenticated-User-Email', '')
  user_email = user_email.replace('accounts.google.com:', '')
  user_email = user_email.replace('@ons.gov.uk', '')

  url = app.config.get('BM_API_URL') + url

  header = {
      "Content-Type": "application/json",
      "Authorization": app.config.get('JWT_TOKEN_BEARER'),
      "user": 'UUItesst',
  }

  r = requests.get(
      url,
      headers=header,
  )

  return r


def job_result_by_job_id(job_id):
  url = f'/bulk-result/{job_id}'
  r = job_api(url)
  r = r.json()
  if not r.get('error'):
    return r.get('signedUrl')
  return False


def job_url_if_authorised(job_id):
  user_email = request.headers.get('X-Goog-Authenticated-User-Email',
                                   'UserNotLoggedIn')
  user_email = user_email.replace('accounts.google.com:', '')
  user_email = user_email.replace('@ons.gov.uk', '')
  job_data = job_data_by_job_id(job_id)
  job_data = job_data.json()
  # {'jobid': 11, 'userid': 'UserNotLoggedIn', 'status': 'results-exported', 'totalrecs': 28, 'recssofar': 28, 'startdate': '2023-03-14T14:55:30', 'enddate': '2023-03-14T16:01:34'}
  if job_data.get('userid', '') == user_email:
    # The user did submit this job
    return job_result_by_job_id(job_id)
  else:
    return False
