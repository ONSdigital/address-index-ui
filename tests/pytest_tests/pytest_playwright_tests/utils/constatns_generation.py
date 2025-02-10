import csv
import json
import os


def get_content_of_file(file_name: str):
  """ Given a file name, return the content of the file """
  current_dir = os.path.dirname(__file__)

  # Build the path to "current_dir/downloads/classifications.csv"
  file_path = os.path.join(current_dir, 'downloads', file_name)

  if 'json' in file_name:
    with open(file_path, "r", encoding='utf-8-sig') as inp_file:
      content = json.load(inp_file)
    return content

  # Open and read the CSV
  with open(file_path, "r", encoding="utf-8") as inp_file:
    reader = csv.reader(inp_file)

    content = []
    for row in reader:
      content.append(row)

  return content


def build_downloads_info(DOWNLOADS: list):
  """ Build info into the DOWNLOADS global dict, such as expected file content"""
  # Loop over key, value in downloads
  for download in DOWNLOADS:
    file_content = get_content_of_file(download.get('file_name'))
    download['expected_content'] = file_content

  return DOWNLOADS


def get_allowed_pages_full_info(allowed_pages: list, endpoints: list):
  """ Given a list of allowed pages, return the page info for all pages """
  allowed_pages_info = [
      page for page in endpoints if page.get('page_name_test') in allowed_pages
  ]
  return allowed_pages_info


def build_user_role_map(user_role_map: dict, all_page_names: list,
                        endpoints: list):
  """ Loop through all groups and build the 'allowed pages array"""
  for group in user_role_map:
    allowed_pages = []
    for page_name in all_page_names:
      if page_name not in group.get('pages_to_remove'):
        allowed_pages.append(page_name)
    group['allowed_pages'] = allowed_pages
    group['allowed_pages_info'] = get_allowed_pages_full_info(
        allowed_pages, endpoints)

  return user_role_map
