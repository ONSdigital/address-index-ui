""" Playwright tests against each page. """
import pytest
from playwright.sync_api import Page, expect

from tests.pytest_tests.pytest_playwright_tests.utils.constants import (
    ALL_PAGE_NAMES,
    BASE_URL,
    ROLES,
    get_just_header_pages,
    get_page_url_from_page_name,
    role_to_username
)
from tests.pytest_tests.pytest_playwright_tests.utils.setup_helpers import login_as_role


def test_title_tag(page: Page):
  page.goto(BASE_URL)

  expect(page).to_have_title('Address Index')


def test_header_visible(page: Page):
  page.goto(BASE_URL)

  expect(page.locator('header')).to_be_visible()


@pytest.mark.parametrize('user_role', ROLES)
def test_available_header_pages(page: Page, user_role: str):
  """ Test that the header contains the correct navigation links for each role """

  page.context.clear_cookies()

  # Login with a username matching the role and return username
  username = login_as_role(page, user_role)

  # For every page (including ones that *might* be inaccesible)
  for page_name in ALL_PAGE_NAMES:
    page_url = get_page_url_from_page_name(page_name)
    testing_page_uri = f'{BASE_URL}{page_url}'
    page.goto(testing_page_uri)

    # Check the header is visible (even for inaccessible pages)
    expect(page.locator('header')).to_be_visible()

    # Get all allowed pages for the current role
    user_info_for_role = role_to_username(user_role)
    allowed_pages_info = user_info_for_role.get('allowed_pages_info')

    # Remove any pages that are subpages from the header check
    expected_header_pages = get_just_header_pages(allowed_pages_info)

    print(
        f'\n FOR THE USERNAME "{username}", with ROLE {user_role}, the EXPECTED HEADER PAGES are: {[ "name: " + x.get("page_name") + " url:" + x.get("url") for x in expected_header_pages]}\n\n'
    )

    # Loop over all expected pages, check for link in header
    for allowed_page in expected_header_pages:
      link_element = page.locator('.ons-navigation__link').filter(
          has_text=allowed_page.get('page_name'))
      expected_page_uri = f'/{allowed_page.get("url")}'

      actual_link_element_uri = link_element.get_attribute('href')
      if actual_link_element_uri != expected_page_uri:
        print(
            f'\n Checking link element: {link_element} \n to have expected uri: "{expected_page_uri}"\n it actually has: "{actual_link_element_uri}"\n\n'
        )
      expect(link_element).to_have_attribute('href', expected_page_uri)
