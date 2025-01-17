""" Special Configuration File for Pytest Playwright Tests """

import pytest
from playwright.sync_api import Page

from tests.pytest_tests.pytest_playwright_tests.utils.constants import BASE_URL, get_page_url_from_page_name
from tests.pytest_tests.pytest_playwright_tests.utils.setup_helpers import login_as_role


@pytest.fixture(scope="session", autouse=True)
def global_setup_available_everywhere():
  print('Global setup run ONCE for all tests')

  # Check here that there's a version of the API that's accessible to the UI


@pytest.fixture
def login_and_goto(page: Page):
  """ Fixture to login as a user role and go to a page """

  def _login_and_goto(user_role: str, page_name: str):
    page.context.clear_cookies()
    login_as_role(page, user_role)
    page_url = get_page_url_from_page_name(page_name)
    page.goto(f"{BASE_URL}{page_url}")
    return page

  return _login_and_goto
