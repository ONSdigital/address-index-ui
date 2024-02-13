
def get_user_email(request):
  user_email = request.headers.get('X-Goog-Authenticated-User-Email',
                                   'UserNotLoggedIn@ons.gov.uk')
  return user_email

def get_username(request):
  # Get just the username from logged in SSO auth, given "request"
  user_email = get_user_email(request)
  username = user_email.replace('accounts.google.com:', '')
  username = user_email.replace('@ons.gov.uk', '')

  return username

