import sqlite3
import hashlib, binascii, os

con = sqlite3.connect('auth.db')
cur = con.cursor()

def get_pass(uname):
  for hashed_password in cur.execute ('SELECT password FROM USERS WHERE username=?', (uname,) )  :
    return hashed_password[0]

username = input('Enter your username: ')
print('')
input_password = input('Please enter your password:')
stored_password = get_pass(username)

def verify_password(stored_password, provided_password):
  """Verify a stored password against one provided by user"""
  salt = stored_password[:64]
  stored_password = stored_password[64:]
  pwdhash = hashlib.pbkdf2_hmac('sha512', 
                            provided_password.encode('utf-8'), 
                            salt.encode('ascii'), 
                            100000)
  pwdhash = binascii.hexlify(pwdhash).decode('ascii')
  return pwdhash == stored_password

print('Password Correct?:  ' )
print(verify_password(stored_password, input_password))

con.close()
