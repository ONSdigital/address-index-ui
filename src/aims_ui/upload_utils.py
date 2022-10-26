import os
import csv

ALLOWED_EXTENSIONS = {'csv'}


class FileUploadException(Exception):
  """Exception raised for errors caused by uploading a file, from size to content validation"""
  def __init__(self, error_title='', error_description=''):
    self.error_title = error_title
    self.error_description = error_description
    super().__init__(self.error_title)


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


def check_valid_upload(file):

  record_limit_exceeded = check_for_record_limit(file, 5001)

  if record_limit_exceeded:
    raise FileUploadException(
        error_title='Input file error',
        error_description=f'Source file contains more than 5000 addresses')

  blank_fields_present = check_for_blank_fields(file)

  if blank_fields_present:
    raise FileUploadException(
        error_title='Input file error',
        error_description=
        f'Source file contains empty fields. Please check that your file conforms to the syntax of the example file. <br> <br> The row with this issue is "{"".join(blank_fields_present)}"'
    )

  if file.filename == '':
    raise FileUploadException(error_title='File Type Error',
                              error_description='Please select a file')

  return True, '', '',
