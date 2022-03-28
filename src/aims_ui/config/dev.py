"""FLASK DEVEOPMENT CONFIG"""
import os

SECRET_KEY = b'secretkey'
LOCAL_API = os.getenv('LOCAL_API')
LOCAL_API_URL =  'http://localhost:9001'
REMOTE_API_URL =  'https://initial-test-bulk-1.aims.gcp.onsdigital.uk'

if str(LOCAL_API) == 'True':
  API_URL = LOCAL_API_URL
else:
  API_URL = REMOTE_API_URL
