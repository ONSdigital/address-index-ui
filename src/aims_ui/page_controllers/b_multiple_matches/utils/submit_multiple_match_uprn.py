import csv
import logging
from io import BytesIO, StringIO

from aims_ui.models.get_addresses import get_addresses
from aims_ui.page_controllers.b_multiple_matches.utils.multiple_match_utils import (
    get_preffered_format_of_address,
    remove_header_row
)
from aims_ui.page_controllers.f_error_pages.page_error import page_error
from aims_ui.page_helpers.api.api_interaction import submit_uprn_mm_job

page_name = 'multiple_match_submit'


def uprn_multiple_address_match(file, all_user_input):
  # Only provide downloadable output
  csv_headers = ['uprn', 'matchedAddress', 'confidenceScore']

  contents = file.readlines()
  remove_header_row(contents)

  proxy = StringIO()
  writer = csv.writer(proxy)

  if all_user_input.get('header_row_export') == 'True':
    writer.writerow(csv_headers)

  line_count = 0

  file_content_formatted = []
  for line in contents:
    line = line.strip().decode('utf-8')
    given_id, uprn = line.split(',', maxsplit=1)
    file_content_formatted.append({'id': given_id, 'uprn': uprn})

  try:
    result = submit_uprn_mm_job(file_content_formatted, all_user_input)
  except:
    logging.error(
        f'Error on a UPRN Multiple API call for:\n "{all_user_input}"')
    return page_error(None, None, page_name)

  matched_addresses = get_addresses(result.json(), 'multiple_uprn')

  def finalize(line_count):
    # Creating the byteIO object from the StringIO Object
    mem = BytesIO()
    mem.write(proxy.getvalue().encode())
    mem.seek(0)
    proxy.close()
    return mem, line_count

  for adrs in matched_addresses:
    line_count += 1
    actual_address_type, preffered_address_format = \
        get_preffered_format_of_address(adrs,all_user_input)
    writer.writerow([
        adrs.uprn.value,
        adrs.formatted_address.value,
        adrs.confidence_score.value,
    ])

  return finalize(line_count)
