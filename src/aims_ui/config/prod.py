"""FLASK PROD CONFIG"""
import os
import logging

if not (API_URL := os.getenv('API_URL')):
  raise RuntimeError('no API_URL ENV variable set')

if not (SECRET_KEY := os.getenv('SECRET_KEY')):
  raise RuntimeError('no SECRET_KEY ENV variable set')

JWT_K_VALUE = str(os.getenv('JWT_K_VALUE'))

logging.info(' \n\n KVALUE is: ' + JWT_K_VALUE)
logging.info(' \n\n OS  ---------- KVALUE is: ' + str(os.getenv('JWT_K_VALUE')))
