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


def check_valid_upload(file):
  file_size = int(os.fstat(file.fileno()).st_size) / 1000000  # In MB
  max_file_size = 1  # In MB
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
