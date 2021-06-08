import os
from . import app
from flask import jsonify


@app.route('/info')
def info():
  key_info = {}
  key_info['ENV'] = os.getenv('FLASK_ENV')
  key_info['PLATFORM'] = os.getenv('PLATFORM')

  return jsonify(key_info)
