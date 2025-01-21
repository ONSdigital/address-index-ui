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


@pytest.fixture
def set_inputs(page: Page):
  """ Fixture to set inputs on a page, given the input selection methods and content """

  def _set_inputs(inputs: list):
    """ An input should be a dict with the following keys: type, label_text/css_selector, content_to_set"""

    for inp in inputs:
      # Select input by label, or css if label not provided
      input_label_text = inp.get('label_text')
      input_type = inp.get('type')

      if input_label_text:
        input_element = page.get_by_label(input_label_text)
      else:
        css_selector = inp.get('css_selector')
        input_element = page.locator(f'{css_selector}')

      if input_type == 'input':
        input_element.fill(str(inp.get('content_to_set')))
      elif input_type == 'checkbox':
        if inp.get('content_to_set') == 'checked':
          input_element.check()
        else:
          input_element.uncheck()

    # Submit the search
    page.get_by_text('Search', exact=True).click()

    return page

  return _set_inputs
