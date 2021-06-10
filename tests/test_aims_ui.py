import os
import tempfile

import pytest

from src import aims_ui

def test_info_page(client):
    """Test the info page exists, and the ENV variable is being displayed."""
    rv = client.get('/info')
    assert b'ENV' in rv.data

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
