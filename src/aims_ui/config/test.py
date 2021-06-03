import os
"""FLASK TEST CONFIG"""


SECRET_KEY=os.getenv('SECRET_KEY')
DATABASE_URI = 'TESTURI'

if SECRET_KEY is None:
  raise RuntimeError('no SECRET_KEY ENV variable set')
