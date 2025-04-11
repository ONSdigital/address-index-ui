import pytest
from playwright.sync_api import Page, expect

from tests.pytest_tests.pytest_playwright_tests.utils.constants import USER_ROLE_MAP, get_redirect_endpoints
""" Test routes that when loaded, simply redirect the user elsewhere """

# Get all endpoints that redirect a user
redirect_endpoints = get_redirect_endpoints()


@pytest.mark.parametrize('current_role', USER_ROLE_MAP)
@pytest.mark.parametrize('endpoint_info', redirect_endpoints)
def test_page_redirects(page: Page, endpoint_info, current_role,
                        login_and_goto_url):
  """ Test visiting a page then checking it redirects elsewhere """

  # Create url
  url = f'{endpoint_info.get("url")}'
  user_role = current_role.get('role')
  login_and_goto_url(user_role, url)

  # For debugging print out everything above and iteration values
  print(
      f'Role: {user_role}, Endpoint: {endpoint_info.get("url")} -> {endpoint_info.get("redirect_url")} -> {endpoint_info.get("redirect_visible_items")} '
  )

  # If a 'redirect_url' is provided, explicitly check the url
  redirect_url = endpoint_info.get('redirect_url')
  if redirect_url != None:
    # Check explicitly for the url
    expected_url = endpoint_info.get('redirect_url')
    page.wait_for_url(expected_url)
  else:
    # Check for present elements on the page to be redirected to
    expected_texts = endpoint_info.get('redirect_visible_elements')
    for expected_text in expected_texts:
      expect(
          page.locator('body').filter(has_text=expected_text)).to_be_visible()
