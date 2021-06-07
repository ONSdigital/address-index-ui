import os

from flask import jsonify


def get_info():
  key_info = {}
  key_info['ENV'] = os.getenv('FLASK_ENV')
  key_info['PLATFORM'] = os.getenv('PLATFORM')

  return jsonify(key_info)
