from aims_ui.models.utilities.sibling_lookup import get_level_1_siblings, get_level_2_siblings, get_siblings


def test_get_siblings_by_level():
  response = {
      'response': {
          'address': {
              'relatives': [
                  {'level': 1, 'siblings': [10008880491]},
                  {'level': 2, 'siblings': [10007963077, 10007963078]},
              ]
          }
      }
  }

  assert get_siblings(response, 1) == [10008880491]
  assert get_level_1_siblings(response) == [10008880491]
  assert get_level_2_siblings(response) == [10007963077, 10007963078]
  assert get_siblings(response, 3) == []


def test_get_siblings_when_relatives_are_missing():
  response = {'response': {'address': {}}}

  assert get_level_1_siblings(response) == []
  assert get_level_2_siblings(response) == []
  assert get_level_1_siblings({}) == []


def test_get_siblings_when_level_has_no_siblings():
  response = {'response': {'address': {'relatives': [{'level': 2, 'siblings': []}]}}}

  assert get_level_1_siblings(response) == []
  assert get_level_2_siblings(response) == []