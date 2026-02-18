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

