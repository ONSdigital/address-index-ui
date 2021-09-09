import os
import csv
from .page_error import PageErrorException

ALLOWED_EXTENSIONS = {'csv'}


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


def check_valid_upload(file):
  file_size = int(os.fstat(file.fileno()).st_size) / 1000000  # In MB
  max_file_size = 1  # In MB
  blank_fields_present = check_for_blank_fields(file)

  if blank_fields_present:
    return (
        False,
        f'Source file contains empty fields. Please check that your file conforms to the syntax of the example file. <br> <br> The row with this issue is "{"".join(blank_fields_present)}"',
        'Input file error')

  if file.filename == '':
    raise PageErrorException(error_title='File Type Error',
                             error_description='Please select a file')

  return True, '', '',
