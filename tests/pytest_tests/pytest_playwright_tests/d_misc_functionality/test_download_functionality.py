import csv
import io
import json

import pytest
from playwright.sync_api import Page

from tests.pytest_tests.pytest_playwright_tests.utils.constants import BASE_URL, DOWNLOADS, STATIC_FILES
""" Check that all downloads links return expected file content """

page_url = f'{BASE_URL}static/downloads/'


@pytest.mark.parametrize('download_info', STATIC_FILES)
def test_static_file(page: Page, download_info):
  url = f'{BASE_URL}{download_info["url_modifier"]}'
  page.goto(url)

  expected_file_content = download_info.get('expected_content')

  actual_content = page.locator('body').inner_text()
  actual_content_json = json.loads(actual_content)

  print(f'Details for expected and actual content:')
  # Include types, content and length of expected and actual content
  print(
      f'Expected Content: {type(expected_file_content)}, {expected_file_content}, {len(expected_file_content)}'
  )
  print(
      f'Actual Content: {type(actual_content)}, {actual_content}, {len(actual_content)}'
  )

  assert expected_file_content == actual_content_json



@pytest.mark.parametrize('download_info', DOWNLOADS)
def test_downloadable_file(page: Page, download_info):
  expected_file_content = download_info.get('expected_content')

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

  assert expected_file_content == downloaded_file
