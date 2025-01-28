import pytest
from playwright.sync_api import Page, expect

from tests.pytest_tests.pytest_playwright_tests.utils.constants import (
    ALL_PAGE_NAMES, BASE_URL, ROLES, LOCATION_OPTIONS, EPOCH_OPTIONS,
    get_just_header_pages, get_page_url_from_page_name, role_to_username)
from tests.pytest_tests.pytest_playwright_tests.utils.constants import GENERIC_TEST_INPUTS

# Define input settings for all elements, expected result

# yapf: disable
TESTS = [
    {
        'test_name': 'basic_search',
        'user_role': 'default',
        'test_inputs': [
          GENERIC_TEST_INPUTS['searchable_postcode'],
          GENERIC_TEST_INPUTS['available_epoch'],
        ],
        'test_outputs': [
            {
              'type': 'text',
              'visible_text': '100040222196',
            },
       ]
    },
]
# yapf: enable


@pytest.mark.parametrize('test', TESTS)
def test_search_filters(page: Page, test: dict, login_and_goto, set_inputs):
  """ Given a dict of inputs, check against the dict of outputs """
  print(
      f'Testing Postcode Story with inputs: {test.get("test_inputs")} and expected outputs: {test.get("test_outputs")}'
  )

  # Login as the user for this test
  page = login_and_goto(test.get('user_role'), 'postcode')

  # Fill in the inputs
  test_inputs = test.get('test_inputs')
  page = set_inputs(test_inputs)

  # Check the outputs
  test_outputs = test.get('test_outputs')

  for out in test_outputs:
    output_type = out.get('type')
    output_visible_text = out.get('visible_text')

    if output_type == 'text':
      expect(page.get_by_text(output_visible_text)).to_be_visible()
