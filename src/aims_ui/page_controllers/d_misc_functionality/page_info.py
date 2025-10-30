import os

from flask import jsonify
from importlib_metadata import PackageNotFoundError, version

from aims_ui import app


def get_version():
  try:
    return version('aims_ui')
  except PackageNotFoundError as e:
    app.logger.warning(
        'Unable to determine aims_ui version, aims_ui was not installed as a package'
    )
    return 'Unknown'


@app.route('/info')
def info():
  key_info = {}
  key_info['ENV'] = os.getenv('FLASK_ENV')
  key_info['PLATFORM'] = os.getenv('PLATFORM')
  key_info['VERSION'] = get_version()
  key_info['LOCAL_STORAGE_VERSION'] = app.config.get('LOCAL_STORAGE_VERSION')

  return jsonify(key_info)
