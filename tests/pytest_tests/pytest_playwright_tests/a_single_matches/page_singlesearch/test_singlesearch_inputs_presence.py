import pytest
from playwright.sync_api import Page, expect
import csv

from tests.pytest_tests.pytest_playwright_tests.utils.constants import (
    ALL_PAGE_NAMES, BASE_URL, ROLES, LOCATION_OPTIONS, EPOCH_OPTIONS,
    DOWNLOADS, get_just_header_pages, get_page_url_from_page_name,
    get_download_info, role_to_username)
""" Check that expected inputs are present """


# Check presence of reusable components and their labels
def test_search_box(page: Page):
  """ The main 'input' box for searching for an address """
  page.goto(BASE_URL)

  expect(page.locator('input[name="input"]')).to_be_visible()


def test_classification_filter(page: Page):
  """ The 'classification' typeahead component """
  page.goto(BASE_URL)

  expect(page.locator('input[name="classificationfilter"]')).to_be_visible()


def test_classification_download(page: Page):
  """ Test the download link for classifications is present """
  page.goto(BASE_URL)

  # Check that a link with the href x is visible
  expect(
      page.locator('a',
                   has_text="Click here to download a list of classifications")
  ).to_be_visible()


@pytest.mark.parametrize('location', LOCATION_OPTIONS)
def test_checkbox_geo_options(page: Page, location: str):
  """ The checkboxes that select a location (i.e England, Wales, etc) """
  page.goto(BASE_URL)
  checkbox = page.get_by_text(location)

  expect(checkbox).to_be_visible()


@pytest.mark.parametrize('epoch', EPOCH_OPTIONS)
def test_epoch_options_present(page: Page, epoch: str):
  """ The radio buttons that select an epoch """
  page.goto(BASE_URL)

  epoch_radio = page.locator(
      f'input[type="radio"][id="{epoch.get("number")}"]')

  expect(epoch_radio).to_be_visible()


def test_minimum_match(page: Page):
  """ The 'minimum match' dropdown """
  page.goto(BASE_URL)

  expect(page.get_by_label('Minimum match %')).to_be_visible()


def test_limit(page: Page):
  """ The 'limit' input box """
  page.goto(BASE_URL)

  expect(page.get_by_label('Limit')).to_be_visible()


def test_download_classification(page: Page):
  page.goto(BASE_URL)

  with page.expect_download() as download_info:
    page.get_by_text(
        "Click here to download a list of classifications").click()

  download = download_info.value

  # Save to a temporary path or let Playwright pick a location
  download_path = download.path()  # Local path where the file got downloaded

  with open(download_path, "r", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)

    actual_file_content = []
    for row in reader:
      actual_file_content.append(row)

  expected_download_content = get_download_info(
      'classifications')['expected_content']

  assert actual_file_content == expected_download_content


def test_include_historical_data(page: Page):
  page.goto(BASE_URL)

  historical_checkbox = page.locator('input[type="checkbox"][id="historical"]')
  expect(historical_checkbox).to_be_visible()


def test_submit_button(page: Page):
  page.goto(BASE_URL)

  expect(page.get_by_text('Search', exact=True)).to_be_visible()


def test_clear_button(page: Page):
  page.goto(BASE_URL)

  expect(page.get_by_text('Clear filters')).to_be_visible()
