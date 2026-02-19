import pytest

from aims_ui.app_helpers.classification_utils.validation import get_full_classification_for_code_or_label, classification_is_valid
from .a_classification_test_helpers import return_expected_csv_content_with_updated_key_names_and_handled_ancillary_values

valid_classification_objects = return_expected_csv_content_with_updated_key_names_and_handled_ancillary_values(
)


def generate_input_variants(input_value):
  """ Given an input value, return a list of variants of that value with different whitespace, *'s and case """
  variants = [
      input_value,
      input_value.lower(),
      f'  {input_value}  ',
      f'\t{input_value}\n',
      input_value + '*',
      '*' + input_value,
  ]
  return variants


# For every classification object, check that submitting the label or the code will return the code
# and that the code is returned in uppercase,
# and that any *'s dont affect the result
@pytest.mark.parametrize('classification_object', valid_classification_objects)
def test_get_full_classification_for_code_or_label(classification_object):
  code = classification_object.get('code')
  label = classification_object.get('label')

  # All codes should end in an strisk
  code_we_expect = code + '*'

  # Get the code matched through the helper
  code_matched_by_helper = get_full_classification_for_code_or_label(code)

  assert code_matched_by_helper == code_we_expect, (
      f"The code '{code}' should have returned '{code_we_expect}' but instead we got '{code_matched_by_helper}'."
  )

  # Get the label matched through the helper
  label_matched_by_helper = get_full_classification_for_code_or_label(label)

  assert label_matched_by_helper == code_we_expect, (
      f"The label '{label}' should have returned '{code_we_expect}' but instead we got '{label_matched_by_helper}'."
  )

  # Now check variants of the input code:
  code_variants = generate_input_variants(code)
  for variant in code_variants:
    code_variant_matched_by_helper = get_full_classification_for_code_or_label(
        variant)
    assert code_variant_matched_by_helper == code_we_expect, (
        f"The code variant '{variant}' should have returned '{code_we_expect}' but instead we got '{code_variant_matched_by_helper}'."
    )


# Now check classification is valid function
@pytest.mark.parametrize('classification_object', valid_classification_objects)
def test_classification_is_valid(classification_object):
  code = classification_object.get('code')

  classification_is_valid_result = classification_is_valid(code)

  assert classification_is_valid_result is True, (
      f"The code '{code}' should have been valid, but classification_is_valid returned False."
  )


# Codes and labels that don't exist
invalid_codes_and_labels = [
    'NonExistentCode',
    'blah',
    True,
    False,
    None,
    123,
    45.67,
    0,
    -1,
    '!@#$%',
    '---',
    '???',
    'NonExistentCode*',
    '  NonExistentCode  ',
    '*NonExistentCode*',
    'nonexistentcode',
    'Non Existent Code',
    'NonExistentCode123',
    'True',
    'False',
    'None',
    '123',
    [],
    {},
    (),
]

@pytest.mark.parametrize('invalid_code_or_label', invalid_codes_and_labels)
def test_classification_is_valid_for_invalid_codes_and_labels(invalid_code_or_label):
  classification_is_valid_result = classification_is_valid(invalid_code_or_label)

  assert classification_is_valid_result is False, (
      f"The code or label '{invalid_code_or_label}' should have been invalid, but classification_is_valid returned True."
  )