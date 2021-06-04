import os

from flask import Flask
import config.base as config_base


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=False)

    ENV = os.getenv('FLASK_ENV')

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    if ENV == 'development':
        import config.dev as config_env
    elif ENV == 'testing':
        import config.test as config_env
    elif ENV == 'production':
        import config.prod as config_env
    else:
        raise RuntimeError('invalid environment ' + ENV)

    app.config.from_object(config_base)
    app.config.from_object(config_env)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
