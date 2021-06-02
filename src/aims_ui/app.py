from flask import Flask
import os

app = Flask(__name__)

ENV = os.environ.get('FLASK_ENV')

if ENV=='development':
    import aims_ui.config.development as config_env
elif ENV=='test':
    import aims_ui.config.test as config_env
elif ENV=='prod':
    import aims_ui.config.prod as config_env
else:
    raise Exception('invalid environment ' + ENV)

app.config.from_object(config_env)
