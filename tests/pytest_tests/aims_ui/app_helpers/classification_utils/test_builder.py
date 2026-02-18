import pytest
import json

from aims_ui.app_helpers.classification_utils.builder import parse_classification_csv_content, handle_ancillary_duplicates, get_classification_file_content_as_dict
from .a_classification_test_helpers import return_expected_csv_content_as_json, return_expected_csv_content_with_updated_key_names_and_handled_ancillary_values

parsed_csv_content = parse_classification_csv_content()


@pytest.mark.parametrize(
    'expected_obj',
    return_expected_csv_content_as_json(),
    ids=lambda obj: f"{obj['Concatenated']}",
)
def test_parse_classification_csv_content(expected_obj):
  """
    Test each classification row for:
    - Missing keys
    - Unexpected keys
    - Incorrect values
  """

  # Locate matching object by primary identifier
  match = next(
      (item for item in parsed_csv_content
       if item['Concatenated'] == expected_obj['Concatenated']),
      None,
  )

  # Check for entire missing object
  assert match is not None, (
      "Missing an entire object.\n"
      f"Expected object:\n{json.dumps(expected_obj, indent=2, sort_keys=True)}\n"
      "Perhaps a row has been deleted from the original CSV file?")

  expected_keys = set(expected_obj.keys())
  parsed_csv_content_keys = set(match.keys())

  missing_keys = expected_keys - parsed_csv_content_keys
  unexpected_keys = parsed_csv_content_keys - expected_keys

  assert not missing_keys, (
      f"{expected_obj['Concatenated']} missing keys: {missing_keys}")

  assert not unexpected_keys, (
      f"{expected_obj['Concatenated']} unexpected keys: {unexpected_keys}")

  # Compare values per key
  mismatches = {
      key: {
          'expected': expected_obj[key],
          'parsed_csv_content': match[key],
      }
      for key in expected_keys if expected_obj[key] != match[key]
  }

  assert not mismatches, ("\n".join(
      (f"The row with the 'Concatenated' value "
       f"'{expected_obj['Concatenated']}' exists, "
       f"but has an unexpected attribute.\n"
       f"It's missing '{key}' which should be "
       f"'{expected_obj[key]}'. "
       f"Instead, we got '{match[key]}'.") for key in mismatches))


@pytest.mark.parametrize(
    'code,expected_label',
    [
        ('RB', 'Residential Ancillary Building'),
        ('LB', 'Land Ancillary Building'),
        ('CB', 'Commercial Ancillary Building'),
        ('MB', 'Military Ancillary Building'),
    ],
)
def test_handle_ancillary_duplicates(code, expected_label):
  """
    Check that each ancillary code has its label correctly replaced.
    """

  test_class_list = [
      {
          'code': 'RB',
          'label': 'This should be replaced'
      },
      {
          'code': 'LB',
          'label': 'This should be replaced'
      },
      {
          'code': 'CB',
          'label': 'This should be replaced'
      },
      {
          'code': 'MB',
          'label': 'This should be replaced'
      },
  ]

  replaced_list = handle_ancillary_duplicates(test_class_list)

  obj = next(item for item in replaced_list if item['code'] == code)

  assert obj['label'] == expected_label, (
      f"Object with code '{code}' has incorrect label. "
      f"Expected '{expected_label}' but got '{obj['label']}'")


def test_classification_file_content_as_dict():
  """
    Test that the classification file content is correctly transformed into a dict.
    - Each object should have the expected keys
    - Each key should have the expected content
    - There should be no additional rows
    - There should be no missing rows
    """

  known_good_list = get_classification_file_content_as_dict()
  expected_list = return_expected_csv_content_with_updated_key_names_and_handled_ancillary_values()

  # Convert to dict keyed by 'code' for easier comparison
  actual_by_code = {obj['code']: obj for obj in known_good_list}
  expected_by_code = {obj['code']: obj for obj in expected_list}

  # Check for missing objects
  for code, expected_obj in expected_by_code.items():
    if code not in actual_by_code:
      raise AssertionError(
          f"We were expecting an object with the code '{code}' to exist. "
          f"The full missing object json is:\n"
          f"'{json.dumps(expected_obj, indent=2)}'")

  # Check for unexpected objects 
  for code, actual_obj in actual_by_code.items():
    if code not in expected_by_code:
      raise AssertionError(
          f"We were not expected an object with the code '{code}' to be provided. "
          f"The full extra object json is:\n"
          f"'{json.dumps(actual_obj, indent=2)}'")

  # Check keys and values 
  for code, expected_obj in expected_by_code.items():
    actual_obj = actual_by_code[code]

    expected_keys = set(expected_obj.keys())
    actual_keys = set(actual_obj.keys())

    # Missing keys
    missing_keys = expected_keys - actual_keys
    if missing_keys:
      missing_key = next(iter(missing_keys))
      raise AssertionError(
          f"Object with code '{code}' did not have all the expected keys.\n"
          f"It was missing '{missing_key}' and that key should have had the value "
          f"'{expected_obj[missing_key]}'")

    # Unexpected extra keys
    extra_keys = actual_keys - expected_keys
    if extra_keys:
      extra_key = next(iter(extra_keys))
      raise AssertionError(
          f"Object with code '{code}' had an unexpected key '{extra_key}' "
          f"with value '{actual_obj[extra_key]}'")

    # Value comparison
    for key in expected_keys:
      actual_value = actual_obj[key]
      expected_value = expected_obj[key]

      if actual_value != expected_value:
        raise AssertionError(
            f"Object with code '{code}' had a key with an unexpected value.\n"
            f"The key '{key}' had a value of '{actual_value}' - "
            f"but we were expecing key '{key}' to have a value of '{expected_value}'"
        )
