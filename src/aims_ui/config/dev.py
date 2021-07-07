"""FLASK DEVEOPMENT CONFIG"""
import os

SECRET_KEY = b'secretkey'
FLASK_DEBUG = 0

if not (API_URL := os.getenv('API_URL', 'https://whitelodge-eq-ai-api.census-gcp.onsdigital.uk')):
    raise RuntimeError('no API_URL ENV variable set')

if not (API_JWT := os.getenv('API_JWT', 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.5W2EgODHpsts672J4psiGH31H-vJBz1r56_Tr9_8pPU')):
    raise RuntimeError('no API_JWT ENV variable set')
