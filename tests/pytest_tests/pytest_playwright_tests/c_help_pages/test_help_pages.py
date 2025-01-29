import pytest
from playwright.sync_api import Page, expect

from tests.pytest_tests.pytest_playwright_tests.utils.constants import (
    ALL_PAGE_NAMES, BASE_URL, ROLES, LOCATION_OPTIONS, EPOCH_OPTIONS,
    get_just_header_pages, get_page_url_from_page_name, role_to_username)
from tests.pytest_tests.pytest_playwright_tests.utils.constants import GENERIC_TEST_INPUTS

# Define input settings for all elements, expected result

# yapf: disable
help_page_tests = [
  {
    'test_name': 'Help Home Page Links and Content',
    'test_description': 'Check that the help page has the correct links by navigating to each one',
    'user_role': 'default',
    'start_page_name': 'help',
    'test_outputs': [
      {
        'type': 'link',
        'visible_text': 'Confidence Score',
        'url': 'help/confidence_score',
        'page_text_content': ['The two scores go into a Sigmoid function which takes into account all the returned scores to give an easy to understand pseudo-percentage for each result. The API can be told (e.g. via the UI) to apply a minimum value of the confidence score, e.g. reject all values under 10. An address with a confidence score of 70 or more can safely be assumed to be the clear winner. An ambiguous address such as 12 Station Road London will return two or more results with a score of around 55.',
                              'The Confidence Score is a number from 0-100 which approximately represents a percentage chance of the address being correct. It is calculated using input from two sources:',
                              '1) The search engine underlying score. This is a number from 0 to about 50 which Elasticsearch outputs for each result. It doesn\'t mean much other than the higher the number then better the \'hit\'',
                              '2) A bespoke score calculation. A complex deterministic analysis is performed on each matching address awarding points for different parts of the address that match.',
                              'For a full explanation see section 5 of this paper:',
                              'onsworkingpaperseriesno17usingdatasciencefortheaddressmatchingservice',
                              ]
      },
      {
        'type': 'link',
        'visible_text': 'Submit Feedback',
        'url': 'help/submit_feedback',
        'page_text_content': ['Please provide feedback via ServiceNow.',
                              'You can do this by searching for \'AIMS\', selecting \'REQUEST\' then select Option \'Provide Feedback\'.',
                              'Then type your feedback in the blank box and click the send button.',
        ],
      },
       {
        'type': 'link',
        'visible_text': 'Help and Documentation',
        'url': 'help/help_and_feedback',
        'page_text_content': ['For further help and documentation please visit:',
                              'https://intranet.ons.statistics.gov.uk/news/improving-data-quality-through-the-address-index-matching-service',
                              'Which contains the latest updates, information and a video tutorial.',
                              'Please note that you will only be able to access the link if you\'re on ONS network.',
        ]
      },
    ]
  }
]
# yapf: enable


@pytest.mark.parametrize('test', help_page_tests)
def test_help_pages(page: Page, test: dict, login_and_goto):
  """ Given the location of the main help page and a user role, check for access to each page and asses against expected page content"""
  print(
      f'Testing Help Page "{test.get("test_name")}" expected outputs: {test.get("test_outputs")}'
  )

  # Login as the user for this test
  page = login_and_goto(test.get('user_role'), test.get('start_page_name'))

  # Check the outputs
  test_outputs = test.get('test_outputs')

  for out in test_outputs:
    output_type = out.get('type')
    output_visible_text = out.get('visible_text')
    output_expected_url = out.get('url')

    if output_type == 'link':
      link_to_help_page = page.get_by_text(output_visible_text)
      expect(link_to_help_page).to_be_visible()

      # Navigate to the link
      link_to_help_page.click()

      # Now we're on a specific help page, check the URL and content
      for text in out.get('page_text_content'):
        text = page.get_by_text(text)
        expect(text).to_be_visible()

      # Return to the help page using the 'help' breadcrumb
      breadcrumb_nav = page.get_by_role("navigation", name="Breadcrumbs")

      # Find the link by its accessible name
      help_link = breadcrumb_nav.get_by_role("link", name="Help")

      # Interact with the link
      help_link.click()
