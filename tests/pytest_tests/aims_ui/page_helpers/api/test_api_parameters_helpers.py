import pytest

from aims_ui.page_helpers.api.api_parameters_helpers import remove_non_existant_parameters

ACCEPTABLE_PARAMETERS = [
    'input', 'name', 'offset', 'limit', 'classificationfilter', 'rangekm',
    'lat', 'lon', 'historical', 'matchthreshold', 'verbose', 'epoch', 'eboost',
    'nboost', 'sboost', 'wboost', 'lboost', 'mboost', 'jboost', 'pafdefault',
    'fallback', 'highlight', 'favourpaf', 'favourwelsh',
    'limitperaddress', 'groupfullpostcodes'
]


@pytest.mark.parametrize('param', ACCEPTABLE_PARAMETERS)
def test_remove_non_existant_parameters(param):
  # Provide one valid parameter and one invalid parameter
  test_params = {
      param: 'valid_value',
      'invalid_parameter': 'should_be_removed'
  }

  result = remove_non_existant_parameters(test_params)

  # Check valid parameter was NOT removed
  assert param in result, (
      f"Expected '{param}' to be acceptable, but was removed. "
      f"Provided '{list(test_params.keys())}', got '{result}'")

  # Check invalid parameter WAS removed
  assert 'invalid_parameter' not in result
