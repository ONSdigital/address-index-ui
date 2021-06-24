import os
import tempfile
import json
import pytest
from flask import url_for

from src import aims_ui

def test_info_page(client):
    """Test the info page exists, and the ENV variable is being displayed."""
    required_keys = ['ENV','PLATFORM','VERSION']

    rv = client.get('/info')
    response_dict = json.loads(rv.data)

    assert all(k in response_dict for k in required_keys)

def test_static_pages_are_200(client):
    """Basic Check to see if pages are present, returning a 200, and also contain some form of content"""
    urls = [ 'uprn',
        'landing',
        'address',
        'postcode',
        'typeahead',
        'multiple_address',
        ]

    for url in urls:
      response = client.get('/'+url)
      response_dict = json.loads(response.data)
      assert response.status_code == 200
      assert response_dict != {}
  

@pytest.fixture
def client():
    db_fd, aims_ui.app.config['DATABASE'] = tempfile.mkstemp()
    aims_ui.app.config['TESTING'] = True

    with aims_ui.app.test_client() as client:
        with aims_ui.app.app_context():
            pass
        yield client

    os.close(db_fd)
    os.unlink(aims_ui.app.config['DATABASE'])
