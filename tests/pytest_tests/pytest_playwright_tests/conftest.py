""" Special Configuration File for Pytest Playwright Tests """

import pytest


@pytest.fixture(scope="session", autouse=True)
def global_setup_available_everywhere():
  print('Global setup run ONCE for all tests')

  # Check here that there's a version of the API that's accessible to the UI
