import os
import tempfile

import pytest

from src import aims_ui


@pytest.fixture
def client():
    db_fd, aims_ui.app.config['DATABASE'] = tempfile.mkstemp()
    aims_ui.app.config['TESTING'] = True

    with aims_ui.app.test_client() as client:
        with aims_ui.app.app_context():
            aims_ui.init_db()
        yield client

    os.close(db_fd)
    os.unlink(aims_ui.app.config['DATABASE'])
