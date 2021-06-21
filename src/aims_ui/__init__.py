import os

from flask import Flask
from flask_login import LoginManager
from .config import base as config_base
from .logging import setup_logging
from .models import User

setup_logging(os.getenv('PLATFORM'))

app = Flask(__name__, instance_relative_config=False)

ENV = os.getenv('FLASK_ENV')

app.config.from_object(config_base)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


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

from . import info
from . import login
from . import index
