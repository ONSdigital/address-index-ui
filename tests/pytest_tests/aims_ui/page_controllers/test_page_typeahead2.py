from importlib import import_module
from unittest.mock import Mock

from aims_ui import app


def test_typeahead2_post_prints_autosuggest_value(monkeypatch, capsys):
  page = import_module('aims_ui.page_controllers.a_single_matches.page_typeahead2')
  monkeypatch.setattr(page, 'get_endpoints', lambda called_from: [])
  monkeypatch.setattr(page, 'check_user_has_access_to_page', lambda page_name: True)
  monkeypatch.setattr(page, 'get_page_location', lambda endpoints, page_name: 'typeahead2.html')
  monkeypatch.setattr(page, 'get_fields', lambda page_name: [])
  monkeypatch.setattr(page, 'get_api_auth', lambda: None)
  monkeypatch.setattr(page, 'render_template', lambda template, **context: context)
  lookup = Mock()
  monkeypatch.setattr(page, 'multiple_uprn_lookup', lookup)

  with app.test_request_context('/typeahead2', method='POST', data={'url-input-autosuggest': 'Selected address'}):
    response = page.typeahead2.__wrapped__()

  assert capsys.readouterr().out == 'Selected address\n'
  assert response['page_name'] == 'typeahead2'
  lookup.assert_not_called()