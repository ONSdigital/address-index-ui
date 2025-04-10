from aims_ui.page_controllers.b_multiple_matches.utils.multiple_address_results import (
    get_recs_so_far_message, 
    get_friendly_header_row_export, 
    format_single_job)


def test_get_recs_so_far_message():
  """ Recs so far message is for the user and should show 'x of y' in the processed column """

  tests = [
    {
      'expected_message': '10 of 100',
      'job_data': {
        'recssofar': 10,
        'totalrecs': 100,
      },
    },
    {
      'expected_message': '0 of 0',
      'job_data': {
        'recssofar': 0,
        'totalrecs': 0,
      },
    },
    {
      'expected_message': 'NA of NA',
      'job_data': {},
    },
  ]

  for test in tests:
    job_data = test.get('job_data')
    actual_message = get_recs_so_far_message(job_data)

    assert actual_message == test.get('expected_message')

def test_get_friendly_header_row_export():
  """ Check the header row export is returned as a string """
  tests = [
    {
      'expected_message': 'True',
      'ui_metadata': {
        'header_row_export': True,
      },
    },
    {
      'expected_message': 'False',
      'ui_metadata': {
        'header_row_export': False,
      },
    },
    {
      'expected_message': 'NA',
      'ui_metadata': {},
    },
  ]

  for test in tests:
    ui_metadata = test.get('ui_metadata')
    actual_message = get_friendly_header_row_export(ui_metadata)

    assert actual_message == test.get('expected_message')






