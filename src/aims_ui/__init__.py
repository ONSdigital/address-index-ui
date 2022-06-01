import os
import sqlite3
import time

from flask import Flask, g
from flask_login import LoginManager
from .config import base as config_base
from .logging import setup_logging
from .models.user_model import User, users

setup_logging(os.getenv('PLATFORM'))

app = Flask(__name__, instance_relative_config=False)

ENV = os.getenv('FLASK_ENV')

app.config.from_object(config_base)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
  maybe_user = next((user for user in users if user.id == user_id), None)
  return maybe_user


if ENV == 'development':
  from .config import dev as config_env
elif ENV == 'testing':
  from .config import test as config_env
elif ENV == 'production':
  from .config import prod as config_env
else:
  raise RuntimeError('invalid environment ' + str(ENV))

app.config.from_object(config_env)

try:
  os.makedirs(app.instance_path)
except OSError:
  pass

DATABASE = '/path/to/database.db'


def get_db():
  db = getattr(g, '_database', None)
  if db is None:
    db = g._database = sqlite3.connect(
        os.path.join(os.path.dirname(__file__), 'database_resources/auth.db'))
  return db


@app.teardown_appcontext
def close_connection(exception):
  db = getattr(g, '_database', None)
  if db is not None:
    db.close()


classifications = None


def get_classifications_cached():
  global start_time, classifications, last_pop_time
  if classifications is None:
    # Populate classifications list at start of program
    last_pop_time = time.time()
    classifications = get_classifications()
    return classifications
  else:
    current_time = time.time()
    time_since_last_population = current_time - last_pop_time
    # More than 60 seconds since last API population of classifications
    if time_since_last_population > 60:
      classifications = get_classifications()
      last_pop_time = time.time()
      return classifications
    else:
      # Use previously cached results
      return classifications


# Must import here to avoid circular imports
from .api_interaction import get_epoch_options

epoch_options = None


def get_epoch_options_cached():
  global epoch_start_time, epoch_options, default_epoch, epoch_last_pop_time
  if epoch_options is None:
    # Populate epoch options list at start of program
    epoch_last_pop_time = time.time()
    epoch_options, default_epoch = get_epoch_options()
    return epoch_options, default_epoch
  else:
    epoch_current_time = time.time()
    epoch_time_since_last_population = epoch_current_time - epoch_last_pop_time
    # More than 120 seconds since last epoch sync
    if epoch_time_since_last_population > 60:
      epoch_options, default_epoch = get_epoch_options()
      epoch_last_pop_time = time.time()
      return epoch_options, default_epoch
    else:
      # Use previously cached results
      return epoch_options, default_epoch

cached_tooltip_data = None
# Cache the contents of the tooltip file to prevent excessive reading from disk
def get_cached_tooltip_data():
  global cached_tooltip_data
  if cached_tooltip_data != None:
    return cached_tooltip_data
  dir_path = os.path.dirname(os.path.realpath(__file__))
  f = open(f'{dir_path}/static/downloads/tool_tip_clerical_information.csv',
           'r')
  tool_tip_data = []
  for line in f.readlines():
    temp = line.split(',')
    temp = [ x.lstrip().rstrip() for x in temp if x.strip() ]
    if temp != []:
      # Convert temp into an object
      temp = {
          'name': temp[1],
          'description': temp[2],
          }
      tool_tip_data.append(temp)
  cached_tooltip_data = tool_tip_data

  return tool_tip_data



from . import info
from . import login
from . import about
from . import page_uprn
from . import page_postcode
from . import page_typeahead
from . import page_multiple_address
from . import page_singlesearch
from . import page_address_info
from . import download_handler
from .api_interaction import get_classifications
