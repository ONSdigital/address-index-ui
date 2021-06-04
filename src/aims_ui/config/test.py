"""FLASK TEST CONFIG"""
import os

if not (SECRET_KEY := os.getenv('SECRET_KEY')):
    raise RuntimeError('no SECRET_KEY ENV variable set')
