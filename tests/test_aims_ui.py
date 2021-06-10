import os
import tempfile
import json
import pytest

from src import aims_ui

def test_info_page(client):
    """Test the info page exists, and the ENV variable is being displayed."""
    required_keys = ['ENV','PLATFORM','VERSION']

    rv = client.get('/info')
    response_dict = json.loads(rv.data)

    all_keys_present = True 
    for key in required_keys:
      if key not in response_dict.keys():
        all_keys_present = False

    assert all_keys_present

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
