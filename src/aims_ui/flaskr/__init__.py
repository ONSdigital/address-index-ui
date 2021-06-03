import os

from flask import Flask
import config.base as config_base


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)

    ENV = os.getenv('FLASK_ENV')

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

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello World!'

    return app
