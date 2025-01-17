import pytest
from playwright.sync_api import Page, expect

from tests.pytest_tests.pytest_playwright_tests.utils.constants import (
    ALL_PAGE_NAMES, BASE_URL, ROLES, LOCATION_OPTIONS, EPOCH_OPTIONS,
    get_just_header_pages, get_page_url_from_page_name, role_to_username)


# Check presence of reusable components and their labels
def test_reusable_components(page: Page):
  page.goto(BASE_URL)

  expect(page).to_have_title('Address Index')


def test_search_box(page: Page):
  page.goto(BASE_URL)

  expect(page.locator('input[name="input"]')).to_be_visible()


def test_classification_filter(page: Page):
  page.goto(BASE_URL)

  expect(page.locator('input[name="classificationfilter"]')).to_be_visible()


def test_classification_download(page: Page):
  page.goto(BASE_URL)

  # Check that a link with the href x is visible
  expect(
      page.locator('a',
                   has_text="Click here to download a list of classifications")
  ).to_be_visible()


@pytest.mark.parametrize('location', LOCATION_OPTIONS)
def test_checkbox_locations(page: Page, location: str):
  page.goto(BASE_URL)
  checkbox = page.get_by_text(location)

  expect(checkbox).to_be_visible()


#@pytest.mark.parametrize('epoch', EPOCH_OPTIONS)
#def test_checkbox_locations(page: Page, epoch: str):
#  page.goto(BASE_URL)
#
#  epoch_radio = page.get_by_role('input').filter(has_text=epoch.get('number'))
#
#  expect(epoch_radio).to_be_visible()


def test_minimum_match(page: Page):
  page.goto(BASE_URL)

  expect(page.get_by_label('Minimum match %')).to_be_visible()


def test_limit(page: Page):
  page.goto(BASE_URL)

  expect(page.get_by_label('Limit')).to_be_visible()


#def test_include_historical_data(page: Page):
#  page.goto(BASE_URL)
#
#  expect(page.get_by_text('Include historical address data').filter(has_not=page.locator('span'))).to_be_visible()


def test_submit_button(page: Page):
  page.goto(BASE_URL)

  expect(page.get_by_text('Search', exact=True)).to_be_visible()


def test_clear_button(page: Page):
  page.goto(BASE_URL)

  expect(page.get_by_text('Clear filters')).to_be_visible()
