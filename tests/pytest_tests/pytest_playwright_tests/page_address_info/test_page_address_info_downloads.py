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

   # Get the content of the downloaded file and check it matches the expected content
  downloaded_file_content = download.text()

  # With the message the download file is as follows: \n\n'{file}', but we expected: \n\n'{expected_file_content}'
  assert downloaded_file_content == expected_file_content, (
    f"The content of the downloaded file did not match the expected content. Please check that the file contains the correct attribute descriptions and that the formatting matches the expected formatting.\n\nDownloaded file content:\n{downloaded_file_content}\n\nExpected file content:\n{expected_file_content}"
  )


