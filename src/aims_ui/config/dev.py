"""FLASK DEVEOPMENT CONFIG"""
import os

SECRET_KEY = b'secretkey'
API_URL = os.getenv('API_URL')
#API_URL = 'http://localhost:9001'

