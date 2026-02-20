import pytest
from playwright.sync_api import Page, expect

from tests.pytest_tests.pytest_playwright_tests.utils.constants import BASE_URL , JS_DOWNLOADS
""" Test that a user can download the attributes data from the Address Info page inside the clerical information section """


def test_page_address_info_download(page: Page):
  """ Check that the page allows the expected download """
  page.goto(BASE_URL + '/address_info/10091471048')

  # Get the element with the visible text content "Clerical Information"
  clerical_info_element = page.get_by_text('Clerical Information')
  # Click on the element to expand the section
  clerical_info_element.click()

  # Expect the phrase "Click here to download a list of attributes and descriptions" to be visible
  expect(page.get_by_text(
      'Click here to download a list of attributes and descriptions')).to_be_visible()
  
  # Now click on the 'click here to download' link
  download_link = page.get_by_text('Click here')

  # Get the expected download content, download_name is "Attribute Descriptions"
  dynamic_file_info = next((item for item in JS_DOWNLOADS if item["download_name"] == "Attribute Descriptions"), None)
  expected_file_content = dynamic_file_info.get('expected_content')

  # Expect the download to have started and the file name to be 'address_attributes.txt'
  with page.expect_download() as download_info:
    download_link.click()
  download = download_info.value
  assert download.suggested_filename == 'address_attributes.txt', (
      f"The downloaded file should have been named 'address_attributes.txt' but was named '{download.suggested_filename}' instead."
  )

  # Get the temporary file path
  downloaded_file_path = download.path()

  # Read the file contents
  with open(downloaded_file_path, 'r', encoding='utf-8') as f:
    downloaded_file_content = f.read()

  assert downloaded_file_content == expected_file_content