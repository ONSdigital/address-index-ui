from flask import Flask
import os
import aims_ui.config.base as config_base

app = Flask(__name__)

ENV = os.getenv('FLASK_ENV')

if ENV=='development':
    import aims_ui.config.dev as config_env
elif ENV=='testing':
    import aims_ui.config.test as config_env
elif ENV=='production':
    import aims_ui.config.prod as config_env
else:
    raise RuntimeError('invalid environment ' + ENV)

app.config.from_object(config_base)
app.config.from_object(config_env)

print(app.config['DATABASE_URI'])
