import os

from flask import Flask
from .config import base as config_base
from .logging import setup_logging
from .info import get_info

setup_logging(os.getenv('PLATFORM'))

app = Flask(__name__, instance_relative_config=False)

ENV = os.getenv('FLASK_ENV')

app.config.from_object(config_base)

if ENV == 'development':
  from .config import dev as config_env
elif ENV == 'testing':
  from .config import test as config_env
elif ENV == 'production':
  from .config import prod as config_env
else:
  raise RuntimeError('invalid environment ' + ENV)

app.config.from_object(config_env)

try:
  os.makedirs(app.instance_path)
except OSError:
  pass


@app.route('/info')
def info():
  return get_info()
