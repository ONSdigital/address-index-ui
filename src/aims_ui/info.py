import os
import logging
from . import app
from flask import jsonify
from importlib_metadata import version

def get_version():
  try:
    return version('aims_ui')
  except PackageNotFoundError as e:
    logging.error('Package not found, try installing as a package')
    return 'Unknown'

@app.route('/info')
def info():
  key_info = {}
  key_info['ENV'] = os.getenv('FLASK_ENV')
  key_info['PLATFORM'] = os.getenv('PLATFORM')
  key_info['VERSION'] = get_version()

  return jsonify(key_info)
