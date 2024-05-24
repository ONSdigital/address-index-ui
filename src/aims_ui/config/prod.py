"""FLASK PROD CONFIG"""
import os
import base64

if not (API_URL := os.getenv('API_URL')):
  raise RuntimeError('no API_URL ENV variable set')

if not (SECRET_KEY := os.getenv('SECRET_KEY')):
  raise RuntimeError('no SECRET_KEY ENV variable set')

API_JWT_K_VALUE = str(os.getenv('API_JWT_K_VALUE'))
API_JWT_K_VALUE = base64.b64decode(API_JWT_K_VALUE)
