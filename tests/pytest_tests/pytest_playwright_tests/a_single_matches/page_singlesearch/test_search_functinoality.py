import pytest
from playwright.sync_api import Page, expect

from tests.pytest_tests.pytest_playwright_tests.utils.constants import (
    ALL_PAGE_NAMES, BASE_URL, ROLES, LOCATION_OPTIONS, EPOCH_OPTIONS,
    get_just_header_pages, get_page_url_from_page_name, role_to_username)

# Define input settings for all elements, expected result

# yapf: disable
TESTS = [
    {
        'test_name': 'basic_search',
        'user_role': 'default',
        'test_inputs': [
          {
            'type': 'input',
            'label_text': 'Enter Search String',
            'content_to_set': 'Big Wave Media',
          },
          {
            'type': 'checkbox',
            'css_selector': 'input[type="radio"][id="39"]',
            'content_to_set': 'checked',
          }
        ],
        'test_outputs': [
            {
              'type': 'text',
              'visible_text': '10023117117', 
            },
       ]
    },
]
# yapf: enable


@pytest.mark.parametrize('test', TESTS)
def test_search_filters(page: Page, test: dict, login_and_goto):
  """ Given a dict of inputs, check against the dict of outputs """
  print(f'Testing Single Searh Story with inputs: {test.get("test_inputs")} and expected outputs: {test.get("test_outputs")}')

  # Login as the user for this test
  page = login_and_goto(test.get('user_role'), 'singlesearch')

  # Fill in the inputs
  test_inputs = test.get('test_inputs')

  for inp in test_inputs:
    # Select input by label, or css if label not provided
    input_label_text = inp.get('label_text')
    input_type = inp.get('type')

    if input_label_text:
      input_element = page.get_by_label(input_label_text)
    else: 
      css_selector = inp.get('css_selector')
      input_element = page.locator(f'{css_selector}')
    
    if input_type == 'input':
      input_element.fill(inp.get('content_to_set'))
    elif input_type == 'checkbox':
      if inp.get('content_to_set') == 'checked':
        input_element.check()
      else:
        input_element.uncheck()

  # Submit the search
  page.get_by_text('Search', exact=True).click()

  # Check the outputs
  test_outputs = test.get('test_outputs')

  for out in test_outputs:
    output_type = out.get('type')
    output_visible_text = out.get('visible_text')

    if output_type == 'text':
      expect(page.get_by_text(output_visible_text)).to_be_visible()
