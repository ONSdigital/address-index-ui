import os
from . import app
from flask import jsonify
from importlib_metadata import version

def get_version():
  print(version('aims_ui'))

  return "s"

@app.route('/info')
def info():
  key_info = {}
  key_info['ENV'] = os.getenv('FLASK_ENV')
  key_info['PLATFORM'] = os.getenv('PLATFORM')
  key_info['VERSION'] = get_version()

  return jsonify(key_info)
