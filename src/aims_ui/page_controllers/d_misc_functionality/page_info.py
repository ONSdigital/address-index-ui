import os

from flask import jsonify

from aims_ui import app


@app.route('/info')
def info():
  key_info = {}
  key_info['ENV'] = os.getenv('FLASK_ENV')
  key_info['PLATFORM'] = os.getenv('PLATFORM')
  key_info['VERSION'] = app.config.get('APP_VERSION')
  key_info['LOCAL_STORAGE_VERSION'] = app.config.get('LOCAL_STORAGE_VERSION')

  return jsonify(key_info)
