import os
import tempfile
import json
import pytest
from flask import url_for

from src import aims_ui


def test_info_page(client):
  """Test the info page exists, and the ENV variable is being displayed."""
  required_keys = ['ENV', 'PLATFORM', 'VERSION']

  rv = client.get('/info')
  response_dict = json.loads(rv.data)

  assert all(k in response_dict for k in required_keys)


def test_static_pages_are_200(client):
  """Basic Check to see if pages are present, returning a 200, and also contain some form of content"""
  urls = [
      'uprn',
      'settings',
      'postcode',
      'typeahead',
  ]

  for url in urls:
    response = client.get('/' + url)
    if response.status_code == 404:
      raise Exception(
          f'Page not found error for {url}, got response: {response}')

    assert response.status_code == 200
