import pytest

from aims_ui.app_helpers.classification_utils.autosuggest import get_classification_autosuggest_list, get_classification_autosuggest_list_reversed, get_full_classification_autosuggest
from .a_classification_test_helpers import return_expected_csv_content_with_updated_key_names_and_handled_ancillary_values

all_classification_objects = return_expected_csv_content_with_updated_key_names_and_handled_ancillary_values(
)


@pytest.mark.parametrize('classification_object', all_classification_objects)
def test_get_classification_autosuggest_list(classification_object):
  expected_output = {
      'en': classification_object.get('code'),
      'category': classification_object.get('label'),
  }
  autosuggest_list = get_classification_autosuggest_list()

  assert expected_output in autosuggest_list, (
      f"The classification object with code '{classification_object.get('code')}' and label '{classification_object.get('label')}' should have been present in the autosuggest list however it was not found."
  )


@pytest.mark.parametrize('classification_object', all_classification_objects)
def test_get_classification_autosuggest_list_reversed(classification_object):
  expected_output = {
      'en': classification_object.get('label'),
      'category': classification_object.get('code'),
  }
  autosuggest_list_reversed = get_classification_autosuggest_list_reversed()

  assert expected_output in autosuggest_list_reversed, (
      f"The classification object with code '{classification_object.get('code')}' and label '{classification_object.get('label')}' should have been present in the reverse autosuggest list however it was not found."
  )


@pytest.mark.parametrize('classification_object', all_classification_objects)
def test_get_full_classification_autosuggest(classification_object):
  expected_output = [{
      'en': classification_object.get('code'),
      'category': classification_object.get('label'),
  }, {
      'en': classification_object.get('label'),
      'category': classification_object.get('code'),
  }]

  full_autosugest_list = get_full_classification_autosuggest()

  missing = [
      item for item in expected_output if item not in full_autosugest_list
  ]

  assert not missing, (
      f"The following classification objects were missing from the final autosuggest list: {missing}"
  )
