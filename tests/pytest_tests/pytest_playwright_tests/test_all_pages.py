""" Playwright tests against each page. """
from playwright.sync_api import Page, BrowserType, expect
import pytest
from pprint import pprint

from tests.pytest_tests.pytest_playwright_tests.utils.constants import BASE_URL, ALL_PAGE_NAMES, ROLES, role_to_username, get_page_url_from_page_name, get_just_header_pages


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

  # Get a username and details about a user given a role
  user_info_for_role = role_to_username(user_role)

  username = user_info_for_role.get('username')

  # Set the username in the browser
  page.set_extra_http_headers({
    'X-Goog-Authenticated-User-Email': username,
  })
  # The browser now thinks that a username assocaited with the current role is logged in

  # For every page (including ones that *might* be inaccesible)
  for page_name in ALL_PAGE_NAMES:
    page_url = get_page_url_from_page_name(page_name)
    testing_page_uri = f'{BASE_URL}{page_url}'
    page.goto(testing_page_uri)

    # Check the header is visible (even for inaccessible pages)
    expect(page.locator('header')).to_be_visible()

    # Get all allowed pages for the current role
    allowed_pages_info = user_info_for_role.get('allowed_pages_info')

    # Remove any pages that are subpages from the header check
    expected_header_pages = get_just_header_pages(allowed_pages_info)

    print(f'\n FOR THE USERNAME "{username}", with ROLE {user_role}, the EXPECTED HEADER PAGES are: {[ "name: " + x.get("page_name") + " url:" + x.get("url") for x in expected_header_pages]}\n\n')

    # Loop over all expected pages, check for link in header
    for allowed_page in expected_header_pages:
      link_element = page.locator('.ons-navigation__link').filter(has_text=allowed_page.get('page_name'))
      expected_page_uri = f'/{allowed_page.get("url")}'

      actual_link_element_uri = link_element.get_attribute('href')
      if actual_link_element_uri != expected_page_uri:
        print(f'\n Checking link element: {link_element} \n to have expected uri: "{expected_page_uri}"\n it actually has: "{actual_link_element_uri}"\n\n')
      expect(link_element).to_have_attribute('href', expected_page_uri)

