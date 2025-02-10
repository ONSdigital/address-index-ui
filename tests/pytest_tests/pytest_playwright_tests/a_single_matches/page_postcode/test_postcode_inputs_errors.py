import pytest
from playwright.sync_api import Page, expect

from tests.pytest_tests.pytest_playwright_tests.utils.constants import (
    BASE_URL,
    GENERIC_TEST_INPUTS,
    TEST_XML_INJECTIONS,
    XML_ERROR_MESSAGE,
    get_page_url_from_page_name,
    set_input_content
)

""" When there is a problem with an input, the Design System Component should show an error message or prompt """

page_name = 'postcode'
page_url = f'{BASE_URL}{get_page_url_from_page_name(page_name)}'


def test_epoch_options(page: Page, set_inputs):
  """ The test Epoch Options should be available including 50 which the tets dataset shouldn't have """
  page.goto(page_url)

  test_inputs = [
      GENERIC_TEST_INPUTS['searchable_postcode'], 
      GENERIC_TEST_INPUTS['unavailable_epoch'], 
  ]

  print(f'Testing {page_name} Story with inputs: {test_inputs}')

  # Set inputs and submit
  page = set_inputs(test_inputs)

  # As Epoch '50' is unavailable, expect an error message
  expect(
      page.get_by_text(
          'Requested Epoch is not available. Current available epochs are 111.'
      )).to_be_visible()


# yapf: disable
illegal_postcode_inputs = [
    {
        'postcode_input':'',
        'error_message': 'Not found error. This is likely due to a blank search feild. Please check your inputs.'
    },
    {
        'postcode_input':'CHEESE',
        'error_message': 'Postcode supplied is not valid according to the UK addresses pattern match.',
    },
    {
        'postcode_input':'23488732472',
        'error_message': 'Postcode supplied is not valid according to the UK addresses pattern match.',
    },
]
# yapf: enable


@pytest.mark.parametrize('illegal_postcode', illegal_postcode_inputs)
def test_blank_input(page: Page, set_inputs, illegal_postcode):
  """ Enter an illegal option into the postcode input and check for error message """
  page.goto(page_url)

  test_inputs = [
      set_input_content(GENERIC_TEST_INPUTS['searchable_postcode'],
                        illegal_postcode.get('postcode_input')),
      GENERIC_TEST_INPUTS['available_epoch'],
  ]

  print(f'Testing {page_name} Story with inputs: {test_inputs}')

  # Set inputs and submit
  page = set_inputs(test_inputs)

  expect(page.get_by_text(
      illegal_postcode.get('error_message'))).to_be_visible()


@pytest.mark.parametrize('xml_injection', TEST_XML_INJECTIONS)
def test_search_xml_error(page: Page, set_inputs, xml_injection):
  """ If an xml injection is attempted, in the 'postcode entry' component should show an error message """
  page.goto(page_url)

  test_inputs = [
      set_input_content(GENERIC_TEST_INPUTS['searchable_postcode'],
                        xml_injection),
      GENERIC_TEST_INPUTS['available_epoch'],
  ]

  print(f'Testing {page_name} Story with inputs: {test_inputs}')

  # Set inputs and submit
  page = set_inputs(test_inputs)

  # Expect error message to be visible
  expect(page.get_by_text(XML_ERROR_MESSAGE)).to_be_visible()


illegal_classifications = ['Octopus', 'Chicken', '*£"&^$', 'NonSense']


@pytest.mark.parametrize('illegal_classification', illegal_classifications)
def test_classification_error(page: Page, illegal_classification, set_inputs):
  """ When entering a classification that doesn't exist, the component should show an error message """
  page.goto(page_url)

  test_inputs = [
      GENERIC_TEST_INPUTS['searchable_postcode'],
      GENERIC_TEST_INPUTS['available_epoch'],
      set_input_content(GENERIC_TEST_INPUTS['available_classification'],
                        illegal_classification),
  ]

  print(f'Testing {page_name} Story with inputs: {test_inputs}')

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
        'value': 201,
        'error_message': 'Limit parameter is too large, maximum = 200'
    },
    {
        'value': 4000,
        'error_message': 'Limit parameter is too large, maximum = 200'
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
  """ When entering an invalid limit, the component should show an error message """
  page.goto(page_url)

  test_inputs = [
      GENERIC_TEST_INPUTS['searchable_postcode'],
      GENERIC_TEST_INPUTS['available_epoch'],
      set_input_content(GENERIC_TEST_INPUTS['available_limit'],
                        illegal_limits.get('value')),
  ]

  print(f'Testing {page_name} Story with inputs: {test_inputs}')

  # Set inputs and submit
  page = set_inputs(test_inputs)

  # Expect error message to be visible
  expect(page.get_by_text(illegal_limits.get('error_message'))).to_be_visible()
