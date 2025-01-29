import pytest
from playwright.sync_api import Page, expect
import csv
import os
import io

from tests.pytest_tests.pytest_playwright_tests.utils.constants import (
    ALL_PAGE_NAMES, ROLES, LOCATION_OPTIONS, EPOCH_OPTIONS, BASE_URL,
    DOWNLOADS, get_just_header_pages, get_page_url_from_page_name,
    role_to_username)
""" Check that all downloads links return expected file content """

page_url = f'{BASE_URL}static/downloads/'


@pytest.mark.parametrize('download_info', DOWNLOADS)
def test_download_static_files(page: Page, download_info):
  """ Test the download endpoint for static files serves the expected content """

  print(
      f'Testing download endpoint: {download_info.get("download_name")}. Info: {download_info}'
  )

  # Create request context
  request_context = page.context.request

  # Download the file
  download_url_location = BASE_URL + download_info.get('url_modifier')
  response = request_context.get(download_url_location)

  csv_text = response.text()
  csv_file_like = io.StringIO(csv_text)

  downloaded_file = []
  reader = csv.reader(csv_file_like)
  for row in reader:
    downloaded_file.append(row)

  expected_file_content = download_info.get('expected_content')
  assert expected_file_content == downloaded_file
