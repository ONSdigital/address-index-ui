import logging

from aims_ui.page_controllers.b_multiple_matches.utils.multiple_match_utils import remove_header_row

ALLOWED_EXTENSIONS = {'csv'}


def validate_limit_parameter(all_user_input, limit_name='limit'):
  """ Valid limit rules and exceptions for multiple match pages """
  # Raise exception with title 'Limit Parameter Error' and description 'Limit parameter must be a positive integer'
  limit = all_user_input.get(limit_name, 'not set')

  if limit == 'not set':
    raise Exception(
        'Limit Parameter Error',
        'Limit parameter appears to be unset. Please set a limit between 1 and 10'
    )
  if not limit.isdigit():
    raise Exception(
        'Limit Parameter Error',
        'Limit parameter must be a positive integer between 1 and 10')

  # If limit is not between 1 and 10
  if not 1 <= int(limit) <= 10:
    raise Exception(
        'Limit Parameter Error',
        'Limit parameter must be a positive integer between 1 and 10')


class FileUploadException(Exception):
  """Exception raised for errors caused by uploading a file, from size to content validation"""
  def __init__(self, error_title='', error_description=''):
    self.error_title = error_title
    self.error_description = error_description
    super().__init__(self.error_title)


def escape_html_string(htmlstring):
  escapes = {'\"': '&quot;', '\'': '&#39;', '<': '&lt;', '>': '&gt;'}
  # This is done first to prevent escaping other escapes.
  htmlstring = htmlstring.replace('&', '&amp;')
  # Replace characters that would escape
  for seq, esc in escapes.items():
    htmlstring = htmlstring.replace(seq, esc)

  return htmlstring


def remove_script_and_html_from_str(inp):
  """Remove script tags for input sanitisation"""
  # Remove key phrases that allow script injection
  no_allowed = ['<scrpit>', '</script>', '[]']
  for phrase in no_allowed:
    inp = inp.replace(phrase, '')
  # Replace all html characters with their HTML escape codes
  inp = escape_html_string(inp)
  return inp


def allowed_file(filename):
  return '.' in filename and \
   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def check_for_blank_fields(file):
  contents = file.readlines()
  file.seek(0)

  for row in contents:
    row = row.strip().decode('utf-8').split(',', maxsplit=1)
    row = [x.replace(',', '') for x in row]
    if '' in row:
      return row
  return False


def check_for_record_limit(file, maxlines):
  contents = file.readlines()
  file.seek(0)
  rows = 0

  for row in contents:
    rows = rows + 1
  if (rows > maxlines):
    return True
  else:
    return False


def check_for_duplicate_id(file):
  contents = file.readlines()
  file.seek(0)

  ids = set()
  uprns = set()

  line_count = 0
  for row in contents:
    row = row.strip().decode('utf-8').split(',', maxsplit=1)
    id, uprn = row

    # Check if the id or uprn already exists in their respective sets
    if id in ids or uprn in uprns:
      return True, line_count

    # Add the id and uprn to their respective sets
    ids.add(id)
    uprns.add(uprn)

    line_count += 1

  # If no duplicates were found
  return False, 0


def check_for_valid_header_row(file):
  """ Check if the header row is valid, or if there is no header row """
  contents = file.readlines()
  file.seek(0)

  # True if a header row has been removed
  if remove_header_row(contents):
    return False, 0

  # Now if there's still a non-numeric header row, throw error
  error_detected, error_line = check_for_non_numeric_id_or_uprn(file)
  return error_detected, 1  # Override to line 1 as it's a problem with header row


def check_for_non_numeric_id_or_uprn(file):
  """ Check if the ID or UPRN fields are non-numeric, ignoring the header row """
  contents = file.readlines()
  file.seek(0)

  remove_header_row(contents)

  row_counter = 2  # Start after header row and +1 to adjust for 0th array index
  for row in contents:
    row = row.strip().decode('utf-8').split(',', maxsplit=1)
    id, uprn = row

    if not id.isdigit() or not uprn.isdigit():
      return True, row_counter
    row_counter += 1

  return False, 0


def check_valid_upload(file, limit, called_from='address'):

  record_limit_exceeded = check_for_record_limit(file, limit)

  if record_limit_exceeded:
    logging.info(
        'Record Limit Exceeded (if unexpected, check user groups and limits)')
    raise FileUploadException(
        error_title='Input file error',
        error_description=f'Source file contains more than {limit} addresses')

  blank_fields_present = check_for_blank_fields(file)

  if blank_fields_present:
    logging.info('Input file contains blank fields')
    raise FileUploadException(
        error_title='Input file error',
        error_description=
        f'Source file contains empty fields. Please check that your file conforms to the syntax of the example file. <br> <br> The row with this issue is "{"".join(blank_fields_present)}"'
    )

  if file.filename == '':
    raise FileUploadException(error_title='File Type Error',
                              error_description='Please select a file')

  if called_from == 'uprn':
    # Check that a valid header is being used, or none at all (also valid)
    error_detected, error_line = check_for_valid_header_row(file)
    if error_detected:
      raise FileUploadException(
          error_title='Invalid Header Row Detected',
          error_description=
          f'An invalid header row was detected. <br><br> Please check that the header row is either valid or that there is no header row at all. <br><br> We detected a problem on line: {error_line}',
      )

    # Check that all the IDs and UPRNS are numeric
    error_detected, error_line = check_for_non_numeric_id_or_uprn(file)
    if error_detected != False:
      raise FileUploadException(
          error_title='Non-numeric ID or UPRN Detected',
          error_description=
          f'One of more lines of the file contain a non-numeric ID or UPRN. <br><br> Please check that there is no header row and that all ID and UPRN fields are numeric. <br><br> We detected a problem on line: {error_line}',
      )

    # Check that there aren't any duplicate ID fields
    error_detected, error_line = check_for_duplicate_id(file)
    if error_detected:
      raise FileUploadException(
          error_title='Duplicate ID or UPRNs Detected',
          error_description=
          f'One or more duplicate IDs have been detected. <br><br>Check that all ID fields are unique. <br><br> We detected a problem on line: {error_line}'
      )

  return True, '', '',
