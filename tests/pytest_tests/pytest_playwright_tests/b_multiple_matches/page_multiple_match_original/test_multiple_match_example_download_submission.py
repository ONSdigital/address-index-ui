from pathlib import Path

import pytest
from playwright.sync_api import Page, expect

from tests.pytest_tests.pytest_playwright_tests.utils.constants import (BASE_URL)


def test_downloading_example_file_and_submitting_it_for_matching(page: Page):
  url_extension = '/multiple_address_original'
  page.goto(f'{BASE_URL}{url_extension}')

  download_path = Path.cwd() / 'multiple_match_example_file.csv'

  with page.expect_download() as download_info:
    page.get_by_role('link', name='sample file').click()

  download = download_info.value
  download.save_as(download_path)

  page.set_input_files('#file_upload', download_path)

  with page.expect_download() as matched_download_info:
    page.get_by_role('button', name='Submit').click()

  matched_download = matched_download_info.value
  matched_download.save_as(Path.cwd() / 'matched_output.csv')

  assert (Path.cwd() / 'matched_output.csv').exists()
