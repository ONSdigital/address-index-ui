import os

from flask import Flask
from .config import base as config_base


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=False)

    ENV = os.getenv('FLASK_ENV')

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    if ENV == 'development':
        from .config import dev as config_env
    elif ENV == 'testing':
        from .config import test as config_env
    elif ENV == 'production':
        from .config import prod as config_env
    else:
        raise RuntimeError('invalid environment ' + ENV)

    app.config.from_object(config_base)
    app.config.from_object(config_env)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
