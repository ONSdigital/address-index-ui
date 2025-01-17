"""FLASK TEST CONFIG"""
import os
from aims_ui import app

API_URL = 'http://localhost:9001/'

if not (SECRET_KEY := os.getenv('SECRET_KEY')):
  SECRET_KEY = 'Shhh, I`m a secret key!'

# Override the default user groups with additional usernames for testing
additional_usernames = [
    {
        'name_of_group': 'default',
        'usernames': ['testDefaultExplicit']
    },
    {
        'name_of_group': 'developers',
        'usernames': ['testDeveloperExplicit']
    },
    {
        'name_of_group': 'bulk_removed',
        'usernames': ['testBulkRemovedExplicit']
    },
    {
        'name_of_group': 'limited_bulk',
        'usernames': ['testBulkLimitedExplicit']
    },
]

for user in app.config.get('USER_GROUPS'):
  for additional_username in additional_usernames:
    if user.get('name') == additional_username.get('name_of_group'):
      user['usernames'].extend(additional_username.get('usernames'))
