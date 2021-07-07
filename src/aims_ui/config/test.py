"""FLASK TEST CONFIG"""
import os

if not (SECRET_KEY := os.getenv('SECRET_KEY')):
  raise RuntimeError('no SECRET_KEY ENV variable set')

if not (API_URL := os.getenv('API_URL')):
    raise RuntimeError('no API_URL ENV variable set')

if not (API_JWT := os.getenv('API_JWT')):
    raise RuntimeError('no API_JWT ENV variable set')
