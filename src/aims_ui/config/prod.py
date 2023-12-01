"""FLASK PROD CONFIG"""
import os

if not (API_URL := os.getenv('API_URL')):
  raise RuntimeError('no API_URL ENV variable set')

if not (SECRET_KEY := os.getenv('SECRET_KEY')):
  raise RuntimeError('no SECRET_KEY ENV variable set')

JWT_K_VALUE = os.getenv('jwt_k_value')
