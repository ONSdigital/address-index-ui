""" Helpers to setup browser environment for tests """

from tests.pytest_tests.pytest_playwright_tests.utils.constants import role_to_username


def login_as_role(page, user_role):
  """ Login with a username matching the role provided and reutrn the username """

  # Get a username and details about a user given a role
  user_info_for_role = role_to_username(user_role)

  username = user_info_for_role.get('username')

  # Set the username in the browser
  page.set_extra_http_headers({
      'X-Goog-Authenticated-User-Email': username,
  })
  # The browser now thinks that a username assocaited with the current role is logged in

  return username
