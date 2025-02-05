import pytest
from playwright.sync_api import Page, expect

from tests.pytest_tests.pytest_playwright_tests.utils.constants import (
    ALL_PAGE_NAMES, ROLES, LOCATION_OPTIONS, EPOCH_OPTIONS, BASE_URL,
    get_just_header_pages, get_page_url_from_page_name, get_redirect_endpoints, role_to_username)

""" Test routes that when loaded, simply redirect the user elsewhere """

# Get all endpoints that redirect a user
redirect_endpoints = get_redirect_endpoints()

@pytest.mark.parametrize('endpoint_info', redirect_endpoints)
def test_search_box(page: Page, endpoint_info, login_and_goto):
  """ Test visiting a page then checking it redirects elsewhere """

  # Login as user_role and visit start url
  print(endpoint_info)

  # Expect the url to be the redirect_url
  expect(page.url).to_equal(f'{BASE_URL}{endpoint_info.get("redirect_url")}')




