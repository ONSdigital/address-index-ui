import os, csv


def build_downloads_info(DOWNLOADS):
  # Loop over key, value in downloads
  for key, download in DOWNLOADS.items():
    current_dir = os.path.dirname(__file__)

    # Build the path to "current_dir/downloads/classifications.csv"
    csv_file_path = os.path.join(current_dir, 'downloads',
                                 download.get('file_name'))

    # Open and read the CSV
    with open(csv_file_path, "r", encoding="utf-8") as csv_file:
      reader = csv.reader(csv_file)

      content = []
      for row in reader:
        content.append(row)

    # By comparing each row, if an error is thrown it gives the exact line the problem is on
    download['content'] = content

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
