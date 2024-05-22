import json
import logging
from aims_ui.page_helpers.api.api_helpers import job_api
from aims_ui.page_helpers.google_utils import get_username


def generate_tag_name(username, user_tag, optional_metadata={}):
  """ Generate tag (username and tag in JSON format) """
  data = {'username': username, 'user_tag': user_tag}
  merged_data = data | optional_metadata
  return json.dumps(merged_data)


def get_tag_data(tag):
  """ Return dict of JSON values saved with job """
  # Always return {'username': tag, 'user_tag':''}
  try:
    data = json.loads(tag)
  except json.JSONDecodeError:
    # Old version - either just username or split with "::"
    if ':' not in tag:  # Deal with very old standard
      return {'username': tag, 'user_tag': ''}
    # Deal with old "split" method
    username = tag.split('::')[0]
    user_tag = tag.split('::')[1]
    data = {'username': username, 'user_tag': user_tag}
  return data


def job_data_by_current_user():
  """ From a list of all jobs, filter by userId """
  # Get the full list of jobs
  r = job_api('/jobs')

  # [{'jobid': 1, 'userid': ...},
  jobs_json = r.json().get('jobs', [])

  current_user = get_username()

  final_jobs = []
  for job in jobs_json:
    userid = job.get('userid', {})
    tag_data = get_tag_data(userid)
    username = tag_data.get('username', '')
    if current_user == username:
      final_jobs.append(job)

  return final_jobs


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
  username = get_username()  # Username of currently logged in user

  job_data = job_data_by_job_id(job_id)
  job_data = job_data.json()
  # {'jobid': 11, 'userid': 'UserNotLoggedIn', 'status': 'results-exported', 'totalrecs': 28, 'recssofar': 28, 'startdate': '2023-03-14T14:55:30', 'enddate': '2023-03-14T16:01:34'}

  json_tag_data = get_tag_data(job_data.get('userid', '{}'))
  userId = json_tag_data.get('username', '')

  if userId == username:
    # The user did submit this job
    return job_result_by_job_id(job_id)
  else:
    logging.error('Job download attempted on an unauthorised job')
    return False
