from flask import request
from aims_ui import app


def get_current_group():
  access_groups = app.config.get('USER_GROUPS')
  username = get_username()

  for group in access_groups:
    if username in group.get('usernames', []):
      return group

  # User not in a group, return default group
  for group in access_groups:
    if group.get('name') == 'default':
      return group


def get_user_email():
  # Set the 'not logged in' username to use with API requests (local only)
  user_email = request.headers.get('X-Goog-Authenticated-User-Email',
                                   'UserNotLoggedIn@ons.gov.uk')
  return user_email


def get_username():
  """ Function to remove email domain markup leaving just username """
  # Get just the username from logged in SSO auth, given "request"
  user_email = get_user_email()
  username = user_email.replace('accounts.google.com:', '')
  username = username.replace('@ons.gov.uk', '')

  return username

def get_usernames(usernames):
  """ Run the 'get_username' function on a list of usernames """
  return [ get_username(x) for x in usernames ] 