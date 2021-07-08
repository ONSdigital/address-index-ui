"""FLASK TEST CONFIG"""
import os

API_URL = 'http://localhost:9001/'

if not (SECRET_KEY := os.getenv('SECRET_KEY')):
  raise RuntimeError('no SECRET_KEY ENV variable set')
