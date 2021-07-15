import os
import sqlite3
import hashlib, binascii, os


def authenticate_user(input_username, input_password, cur):
  """Authenticate password given username"""
  def get_pass(uname):
    """Get passwordfor a user, given the username"""
    for hashed_password in cur.execute(
        'SELECT password FROM USERS WHERE username=?', (uname, )):
      return hashed_password[0]

  def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'),
                                  salt.encode('ascii'), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

  stored_password = get_pass(input_username)
  if stored_password is None:
    return None

  return verify_password(stored_password, input_password)
