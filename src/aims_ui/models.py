from .database_resources.login_as_user import authenticate_user
from flask_login import UserMixin
from six import text_type
import uuid


from flask_login import UserMixin

users = []  


class User(UserMixin):
  def __init__(self):
    self.id = str(uuid.uuid4())

  def is_authenticated(self, username, password):
    return authenticate_user(username, password)

  def is_active(self):
    return True
  
  def is_anonymous(self):
    return False

  def get_id(self):
    try:
      return text_type(self.id)
    except AttributeError:
      raise NotImplementedError('No `id` attribute - override `get_id`')


