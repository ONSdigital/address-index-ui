from aims_ui.page_helpers.api.api_interaction import job_result_formatter
import json


def get_recs_so_far_message(single_job_data):
  """ Given data for one job, format the progress message """
  recs_so_far = single_job_data.get('recssofar', 'NA')
  total_recs = single_job_data.get('totalrecs', 'NA')

  return f'{recs_so_far} of {total_recs}'


def get_friendly_header_row_export(ui_metadata):
  """ Given a valid json metadata object, return a nicely formatted Header Row flag for the user """
  header_row_export = ui_metadata.get('header_row_export', 'NA')

  return str(header_row_export)


def get_friendly_paf_nag_preference(ui_metadata):
  """ Given a valid json metadata object, return a nicely formatted Header Row flag for the user """
  pafdefault = ui_metadata.get('pafdefault', 'false')
  paf_nag_preference = "NAG"
  if pafdefault == 'true': paf_nag_preference = "PAF"
  return str(paf_nag_preference)


def format_single_job(job_data):
  """ Given data for a single job, format it into a dict """
  single_job_data = {
      'jobid': job_data.get('jobid'),
      'topic': job_data.get('topic'),
      'dataset': job_data.get('dataset'),
      'status': job_data.get('status'),
      'userid': job_data.get('userid'),
      'uimetadata': job_data.get('uimetadata'),
      'recssofar': job_data.get('recssofar'),
      'totalrecs': job_data.get('totalrecs'),
      'username': job_data.get('username'),
  }

  # Now add artificially created data
  single_job_data['recssofarmessage'] = get_recs_so_far_message(
      single_job_data)
  single_job_data['downloadlink'] = job_result_formatter(
      single_job_data.get('jobid'))

  # If the dataset is not None (blank string is ok)
  dataset = single_job_data.get('dataset')
  dataset = 'NA' if dataset == '' else dataset
  if dataset:
    # It is the new format, fill in information from dataset, username etc
    ui_metadata = json.loads(single_job_data.get('uimetadata', '{}'))
    single_job_data['username'] = single_job_data.get('userid', 'NA')
    single_job_data['jobname'] = single_job_data.get('dataset', 'NA')
    single_job_data['header_row_export'] = get_friendly_header_row_export(
        ui_metadata)
    single_job_data['paf_nag_preference'] = get_friendly_paf_nag_preference(
        ui_metadata)
  else:
    # The userid stores a json of the metadata
    try:
      ui_metadata_old = json.loads(single_job_data.get('userid'))
      single_job_data['username'] = ui_metadata_old.get('username', 'NA')
      single_job_data['jobname'] = ui_metadata_old.get('user_tag', 'NA')
      single_job_data['header_row_export'] = get_friendly_header_row_export(
          ui_metadata_old)
      single_job_data['paf_nag_preference'] = get_friendly_paf_nag_preference(
          ui_metadata_old)
    except json.JSONDecodeError:
      # Not a json? Simply put all the data in the username column
      single_job_data['username'] = single_job_data.get('userid', 'NA')

  return single_job_data


def get_results_plus_metadata(jobs_data):
  """ Given the jobs for the current user, expand the "uimetadata" json into the jobs data and return a list"""

  # Format each job data into a dict
  final_jobs = [format_single_job(job_data) for job_data in jobs_data]
  #print(f'Final jobs: {final_jobs}')

  return final_jobs
