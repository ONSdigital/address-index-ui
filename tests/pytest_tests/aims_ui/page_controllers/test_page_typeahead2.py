from importlib import import_module
from unittest.mock import Mock
import json

import aims_ui
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


def test_typeahead2_get_creates_autosuggest_file(monkeypatch, tmp_path):
  page = import_module('aims_ui.page_controllers.a_single_matches.page_typeahead2')
  monkeypatch.setattr(page, 'get_endpoints', lambda called_from: [])
  monkeypatch.setattr(page, 'check_user_has_access_to_page', lambda page_name: True)
  monkeypatch.setattr(page, 'get_page_location', lambda endpoints, page_name: 'typeahead2.html')
  monkeypatch.setattr(page, 'get_fields', lambda page_name: [])
  monkeypatch.setattr(page, 'get_api_auth', lambda: None)
  monkeypatch.setattr(page, 'render_template', lambda template, **context: context)
  monkeypatch.setattr(page, 'delete_input', lambda session: None)
  monkeypatch.setattr(page, 'multiple_uprn_lookup', lambda siblings: Mock(**{
      'json.return_value': {'response': {'addresses': [
          {'formattedAddress': 'Selected address', 'uprn': '123'}
      ]}}
  }))
  static_folder = tmp_path / 'static'
  (static_folder / 'downloads').mkdir(parents=True)
  monkeypatch.setattr(app, 'static_folder', str(static_folder))
  monkeypatch.setattr(aims_ui, '__file__', str(tmp_path / '__init__.py'))
  file_path = static_folder / 'downloads' / 'test_for_typeahead_child_addresses.json'

  with app.test_request_context('/typeahead2'):
    page.typeahead2.__wrapped__()

  assert json.loads(file_path.read_text(encoding='utf-8')) == [
      {'en': 'Selected address', 'uprn': '123'}
  ]
  autosuggest = import_module('aims_ui.page_controllers.d_misc_functionality.download_handler').autosuggest
  assert json.loads(autosuggest.__wrapped__('test_for_typeahead_case')) == [
      {'en': 'Selected address', 'uprn': '123'}
  ]