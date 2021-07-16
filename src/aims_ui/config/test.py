"""FLASK TEST CONFIG"""
import os

API_URL = 'http://localhost:9001/'

if not (SECRET_KEY := os.getenv('SECRET_KEY')):
  SECRET_KEY = 'Shhh, I`m a secret key!'
