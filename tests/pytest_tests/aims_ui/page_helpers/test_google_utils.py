from flask import Flask

from aims_ui.page_helpers.google_utils import get_current_group, get_user_email, get_username

# Setup fake app for testing
app = Flask(__name__)


def test_get_user_email():
  """ Given a user id, check just the email is returned """

  test_email = 'username@ons.gov.uk'

  with app.test_request_context(
      headers={'X-Goog-Authenticated-User-Email': test_email}):
    email = get_user_email()
    assert email == test_email


def test_get_username():
  """ From an email, get just the username """

  test_email = 'username@ons.gov.uk'

  with app.test_request_context(
      headers={'X-Goog-Authenticated-User-Email': test_email}):
    username = get_username()
    assert 'username' == username

  test_email = 'test45uSerName@ons.gov.uk'
  with app.test_request_context(
      headers={'X-Goog-Authenticated-User-Email': test_email}):
    username = get_username()
    assert 'test45uSerName' == username


def test_current_group():
  """ Test default group is returned if user not in any group """

  test_email = 'userNotLoggedIn@ons.gov.uk'
  with app.test_request_context(
      headers={'X-Goog-Authenticated-User-Email': test_email}):
    group = get_current_group()
    assert group.get('name') == 'default'

  test_email = 'blank@ons.gov.uk'
  with app.test_request_context(
      headers={'X-Goog-Authenticated-User-Email': test_email}):
    group = get_current_group()
    assert group.get('name') == 'default'

  test_email = ''
  with app.test_request_context(
      headers={'X-Goog-Authenticated-User-Email': test_email}):
    group = get_current_group()
    assert group.get('name') == 'default'
