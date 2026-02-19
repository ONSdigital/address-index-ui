import pytest

from aims_ui.app_helpers.classification_utils.hierarchy import get_class_info_from_code, get_classification_list_as_string
from .a_classification_test_helpers import return_expected_csv_content_with_updated_key_names_and_handled_ancillary_values, return_classifications_code_and_expected_string_pairs

codes_that_dont_exist = [
    # Integers
    0,
    42,
    -7,
    999999,
    123456789,
    # Floats
    3.14,
    -0.001,
    2.71828,
    1e6,
    -5.5,
    # Booleans
    True,
    False,
    # None / null-like
    None,
    # Strings — lowercase only
    'abcde',
    'nonexistent',
    'testcode',
    'lowercase',
    'invalid',
    # Strings — uppercase only (no numbers)
    'ABCDE',
    'INVALID',
    'NOTREAL',
    'SAMPLE',
    'XXXXX',
    # Strings — numbers only
    '12345',
    '00000',
    '987654',
    '42',
    '999',
    # Strings — mixed case (no numbers)
    'AbCdE',
    'MixedCase',
    'TestString',
    'NoDigits',
    'CamelCase',
    # Strings — symbols / punctuation
    '!@#$%',
    '-----',
    '???',
    'code!',
    '###',
    # Empty / whitespace strings
    '',
    ' ',
    '   ',
    # Other types
    [],
    {},
    (),
    [1, 2, 3],
    {
        'code': 'X1Y2Z3'
    },
]


@pytest.mark.parametrize('code', codes_that_dont_exist)
def test_class_info_from_code_none_for_non_existent_code(code):
  # None of the above should return anything but None, as they do not exist in classifications
  result = get_class_info_from_code(code)
  assert result is None, (
      f"The code '{code}' should not have been present in the classifications data, "
      f"however we matched '{code}' to '{result}'.")


valid_classification_objects = return_expected_csv_content_with_updated_key_names_and_handled_ancillary_values(
)


@pytest.mark.parametrize('classification_object', valid_classification_objects)
def test_get_class_info_from_code_valid_codes(classification_object):
  # For each valid code, check we get the full data
  code = classification_object.get('code')

  result = get_class_info_from_code(code)
  assert result == classification_object, (
      f"The code '{code}' should have returned the full classification object, "
      f"We were expecting '{classification_object}'\n,"
      f"however we got '{result}' instead.")


# List of objects: [{'code': 'ZW99TP', 'class_list_string': '[Primary] [Secondary] [Tertiary] [Quaternary]'}, ...]
classification_codes_and_matching_full_strings = return_classifications_code_and_expected_string_pairs(
)


@pytest.mark.parametrize('code_string_pair',
                         classification_codes_and_matching_full_strings)
def test_get_classification_list_as_string_valid_codes(code_string_pair):
  code = code_string_pair.get('code')
  expected_string = code_string_pair.get('class_list_string')

  string_of_hierarchy_breakdown = get_classification_list_as_string(code)

  # Does the expected string (from the static test data) match the string from get_classification_list_as_string
  assert string_of_hierarchy_breakdown == expected_string, (
      f"For the code '{code}', we were expecting the string '{expected_string}', "
      f"but instead got '{string_of_hierarchy_breakdown}'.",
      "Note that output is case, spacing and punctuation sensitive, so check for any discrepancies there."
  )
