import os
import csv

ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
  return '.' in filename and \
   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def blank_fields_present(file):
  contents = file.readlines()

  for row in contents:
    row = row.strip().decode('utf-8').split(',',maxsplit=1)
    if len(row) != 2:
      return row
  return False

def check_valid_upload(file):
    file_size = int(os.fstat(file.fileno()).st_size) / 1000000  # In MB
    max_file_size = 1  # In MB
    
    if blank_fields_present(file):
      return (False,
             'Source file contains empty fields. Please check that your file conforms to the syntax of the example file.',
             'Input file error')

    if file.filename == '':
      return (False,
             'Please select a file',
             'File Type Error')

    if file_size > max_file_size:
      return (False, 
          f'File size is too large. Please enter a file no larger than {max_file_size} MB',
          'File Size Error')

    return True,'','', 



