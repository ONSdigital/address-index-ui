import os
import sqlite3

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
        db = g._database = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'database_resources/auth.db'))
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

from . import info
from . import login
from . import landing
from . import page_uprn
from . import page_postcode
from . import page_typeahead
from . import page_multiple_address
from . import page_singlesearch
