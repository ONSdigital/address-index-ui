import pytest
from playwright.sync_api import Page, expect

from tests.pytest_tests.pytest_playwright_tests.utils.constants import (
    ALL_PAGE_NAMES, BASE_URL, ROLES, LOCATION_OPTIONS, EPOCH_OPTIONS,
    get_just_header_pages, get_page_url_from_page_name, role_to_username)

import re
""" When there is a problem with an input, the Design System Component should show an error message or prompt """

GENERIC_TEST_INPUTS = {
    'searchable_address': {
        'type': 'input',
        'label_text': 'Enter Search String',
        'content_to_set': '039482934',
    },
    'available_epoch': {
        'type': 'checkbox',
        'css_selector': 'input[type="radio"][id="39"]',
        'content_to_set': 'checked',
    }
}


def test_blank_input(page: Page, set_inputs):
  """ If there's a blank input parameter submitted, the component should show an error message """
  page.goto(BASE_URL)

  test_inputs = [
      {
          'type': 'input',
          'label_text': 'Enter Search String',
          'content_to_set': ''
      },
      GENERIC_TEST_INPUTS['available_epoch'],
  ]

  print(f'Testing Single Search Blank Input Story with inputs: {test_inputs}')

  # Set inputs and submit
  page = set_inputs(test_inputs)

  expect(page.get_by_text('Missing parameter: input')).to_be_visible()


def test_search_uprn_sugesgion(page: Page, set_inputs):
  """ If a completely numerical search is submitted, the "UPRN search" suggestion should be shown """
  page.goto(BASE_URL)

  test_inputs = [
      GENERIC_TEST_INPUTS['searchable_address'],
      GENERIC_TEST_INPUTS['available_epoch'],
  ]

  print(f'Testing Single Search Story with inputs: {test_inputs}')

  # Set inputs and submit
  page = set_inputs(test_inputs)

  uprn_suggesgion_link = page.get_by_text('Try this service for UPRN searches')

  # Expect the suggestion to be visible
  expect(uprn_suggesgion_link).to_be_visible()

  # Expect the link to include the inputted UPRN
  link_element = page.get_by_text('Try this service for UPRN searches')
  link_element.click()

  # Get the 'input' feild and check it's value of the UPRN page
  uprn_input = page.get_by_label('To get started, enter a UPRN')
  expect(uprn_input).to_have_value('039482934')


def test_search_xml_error(page: Page, set_inputs):
  """ If an xml injection is attempted, the page should show an error message """
  page.goto(BASE_URL)

  test_inputs = [{
      'type':
      'input',
      'label_text':
      'Enter Search String',
      'content_to_set':
      """<?xml version="1.0" ?> <!DOCTYPE root [   <!ENTITY test SYSTEM "file:///etc/passwd"> ]> <root>   <foo>&test;</foo> </root>""",
  }]

  print(f'Testing Single Search Story with inputs: {test_inputs}')

  # Set inputs and submit
  page = set_inputs(test_inputs)

  # Expect error message to be visible
  expect(
      page.get_by_text('XML Attack Detected. This incident will be reported.')
  ).to_be_visible()


illegal_classifications = ['Octopus', 'Chicken', '*£"&^$', 'NonSense']


@pytest.mark.parametrize('illegal_classification', illegal_classifications)
def test_classification_error(page: Page, illegal_classification, set_inputs):
  """ When entering a classification that doesn't exist, the component should show an error message """
  page.goto(BASE_URL)

  test_inputs = [
      GENERIC_TEST_INPUTS['searchable_address'],
      GENERIC_TEST_INPUTS['available_epoch'], {
          'type': 'input',
          'label_text': 'Classification',
          'content_to_set': illegal_classification,
      }
  ]

  print(f'Testing Single Search Story with inputs: {test_inputs}')

  # Set inputs and submit
  page = set_inputs(test_inputs)

  # Expect error message to be visible
  expect(
      page.get_by_text(
          'Invalid classification filter value provided. Filters must exactly match a classification code (see /classifications) or use a pattern match such as RD*. There are also four presets: residential, commercial, workplace, and educational.'
      )).to_be_visible()


illegal_limits = [
    {
        'value': 0,
        'error_message': 'Limit parameter is too small, minimum = 1',
    },
    {
        'value': -1,
        'error_message': 'Limit parameter is too small, minimum = 1',
    },
    {
        'value': 100,
        'error_message': 'Limit parameter is too large, maximum = 50'
    },
    {
        'value': 51,
        'error_message': 'Limit parameter is too large, maximum = 50'
    },
    {
        'value': 'abc',
        'error_message': 'Limit parameter is not numeric',
    },
    {
        'value': '1.5',
        'error_message': 'Limit parameter is not numeric',
    },
]


@pytest.mark.parametrize('illegal_limits', illegal_limits)
def test_limit_parameter(page: Page, illegal_limits, set_inputs):
  """ When entering a classification that doesn't exist, the component should show an error message """
  page.goto(BASE_URL)

  test_inputs = [
      GENERIC_TEST_INPUTS['searchable_address'],
      GENERIC_TEST_INPUTS['available_epoch'], {
          'type': 'input',
          'label_text': 'Limit',
          'content_to_set': illegal_limits.get('value'),
      }
  ]

  print(f'Testing Single Search Story with inputs: {test_inputs}')

  # Set inputs and submit
  page = set_inputs(test_inputs)

  # Expect error message to be visible
  expect(page.get_by_text(illegal_limits.get('error_message'))).to_be_visible()
