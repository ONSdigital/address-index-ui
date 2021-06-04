"""FLASK PROD CONFIG"""
import os

SECRET_KEY = os.getenv('SECRET_KEY')

if not (SECRET_KEY := os.getenv('SECRET_KEY')):
    raise RuntimeError('no SECRET_KEY ENV variable set')
