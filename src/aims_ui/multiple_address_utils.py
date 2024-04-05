import requests
import tarfile
import io
import json
from flask import request
import logging
from . import app
from .api_helpers import get_header, job_api
from .google_utils import get_username


def job_data_by_job_id(job_id):
  url = f'/bulk-progress/{job_id}'
  r = job_api(url)
  return r


def job_result_by_job_id(job_id):
  url = f'/bulk-result/{job_id}'
  r = job_api(url)
  r = r.json()
  if not r.get('error'):
    return r.get('signedUrl')
  return False


def job_url_if_authorised(job_id):
  username = get_username()

  job_data = job_data_by_job_id(job_id)
  job_data = job_data.json()
  # {'jobid': 11, 'userid': 'UserNotLoggedIn', 'status': 'results-exported', 'totalrecs': 28, 'recssofar': 28, 'startdate': '2023-03-14T14:55:30', 'enddate': '2023-03-14T16:01:34'}

  submittedJobUserId = job_data.get('userid', '')

  # Remove label
  if "::" in submittedJobUserId:
    parts = submittedJobUserId.split("::")
    submittedJobUserId = parts[0]

  if submittedJobUserId == username:
    # The user did submit this job
    return job_result_by_job_id(job_id)
  else:
    logging.error('Job download attempted on an unauthorised job')
    return False
