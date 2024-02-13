from . import app
from .google_utils import get_username, get_user_email


def get_header(username=True):
  """ Get defaut header for API requests """
  header = {
      "Content-Type": "application/json",
      "Authorization": app.config.get('JWT_TOKEN_BEARER'),
  }

  if username:
    header.user = get_username()

  return header
