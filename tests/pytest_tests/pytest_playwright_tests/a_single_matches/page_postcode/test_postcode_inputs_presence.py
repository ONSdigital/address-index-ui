import pytest
from playwright.sync_api import Page, expect

from tests.pytest_tests.pytest_playwright_tests.utils.constants import (
    ALL_PAGE_NAMES, ROLES, LOCATION_OPTIONS, EPOCH_OPTIONS, BASE_URL,
    get_just_header_pages, get_page_url_from_page_name, role_to_username)
""" Check that expected inputs are present """

page_name = 'postcode'
page_url = f'{BASE_URL}{get_page_url_from_page_name(page_name)}'


# Check presence of reusable components and their labels
def test_search_box(page: Page):
  """ The main 'input' box for searching for a postcode """
  page.goto(page_url)

  expect(page.get_by_label('To get started, enter a PostCode')).to_be_visible()


def test_classification_filter(page: Page):
  """ The 'classification' typeahead component """
  page.goto(page_url)

  expect(page.locator('input[name="classificationfilter"]')).to_be_visible()


def test_classification_download(page: Page):
  """ Test the download link for classifications is present """
  page.goto(page_url)

  # Check that a link with the href x is visible
  expect(
      page.locator('a',
                   has_text="Click here to download a list of classifications")
  ).to_be_visible()


@pytest.mark.parametrize('epoch', EPOCH_OPTIONS)
def test_epoch_options_present(page: Page, epoch: str):
  """ The radio buttons that select an epoch """
  page.goto(page_url)

  epoch_radio = page.locator(
      f'input[type="radio"][id="{epoch.get("number")}"]')

  expect(epoch_radio).to_be_visible()


def test_limit(page: Page):
  """ The 'limit' input box """
  page.goto(page_url)

  expect(page.get_by_label('Limit')).to_be_visible()


def test_submit_button(page: Page):
  page.goto(page_url)

  expect(page.get_by_text('Search', exact=True)).to_be_visible()


def test_clear_button(page: Page):
  page.goto(page_url)

  expect(page.get_by_text('Clear filters')).to_be_visible()
