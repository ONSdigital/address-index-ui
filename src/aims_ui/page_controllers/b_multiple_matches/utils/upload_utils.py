import logging

ALLOWED_EXTENSIONS = {'csv'}


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

  for row in contents:
    row = row.strip().decode('utf-8').split(',', maxsplit=1)
    id, uprn = row

    # Check if the id or uprn already exists in their respective sets
    if id in ids or uprn in uprns:
      return True

    # Add the id and uprn to their respective sets
    ids.add(id)
    uprns.add(uprn)

  # If no duplicates were found
  return False


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
    # Check that there aren't any duplicate ID fields
    duplicate_id_detected = check_for_duplicate_id(file)
    if duplicate_id_detected:
      raise FileUploadException(
          error_title='Duplicate ID or UPRNs Detected',
          error_description=
          f'One or more duplicate IDs have been detected. Check that all ID fields are unique.'
      )

  return True, '', '',
