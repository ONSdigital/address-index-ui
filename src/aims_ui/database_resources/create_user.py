import sqlite3
import hashlib, binascii, os

con = sqlite3.connect('auth.db')
cur = con.cursor()

username = input('Enter new username: ')
print("")
password = input('Enter ' + str(username) + "'s new password:  ")


# Salt and hash the password
def hash_password(password):
  """Hash a password for storing."""
  salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
  pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt,
                                100000)
  pwdhash = binascii.hexlify(pwdhash)
  return (salt + pwdhash).decode('ascii')


hashed_password = hash_password(password)

cur.execute('INSERT INTO USERS VALUES (?, ?)', (username, hashed_password))

con.commit()

print("Successfully added anew user")
con.close()
