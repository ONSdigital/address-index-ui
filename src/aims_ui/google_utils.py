from flask import request


def get_user_email():
  user_email = request.headers.get('X-Goog-Authenticated-User-Email',
                                   'UserNotLoggedIn@ons.gov.uk')
  return user_email


def get_username():
  # Get just the username from logged in SSO auth, given "request"
  user_email = get_user_email()
  username = user_email.replace('accounts.google.com:', '')
  username = username.replace('@ons.gov.uk', '')

  return username
