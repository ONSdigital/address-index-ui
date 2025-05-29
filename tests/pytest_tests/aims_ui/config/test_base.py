from flask import Flask

from src.aims_ui.config import base as config_base


def get_base_config_dict():
  app = Flask(__name__, instance_relative_config=False)
  app.config.from_object(config_base)

  # Convert the config object to a dictionary
  config_dict = {key: app.config[key] for key in app.config.keys()}

  return config_dict


def test_default_group_access():
  """ Check that the default group denies api access, has correct bulk limits """

  conf = get_base_config_dict()
  user_groups_conf = conf.get('USER_GROUPS')
  for group in user_groups_conf:
    if group.get('name') == 'default':
      default_group = group

  default_pages_removed = default_group.get('pages_to_remove')

  # Ensure custom response is in the default group's pages to remove
  assert 'custom_response' in default_pages_removed

  # Check bulk limits for the default group
  bulk_limits = default_group.get('bulk_limits')

  assert bulk_limits.get('limit_mini_bulk') == 5000
  assert bulk_limits.get('limit_vast_bulk') == 100000
  assert bulk_limits.get('limit_uprn_match') == 5000


def test_secure_cookie():
  """ Check that the secure cookie is set to True """

  conf = get_base_config_dict()

  assert conf['SESSION_COOKIE_SECURE'] == True


def test_base_classification_list():
  """ Check that the default_classification contains expected keys """

  # Deffine keys that should always be in the config
  keys_that_should_be_present = [
      'DEBUG',
      'TESTING',
      'PROPAGATE_EXCEPTIONS',
      'SECRET_KEY',
      'PERMANENT_SESSION_LIFETIME',
      'USE_X_SENDFILE',
      'SERVER_NAME',
      'APPLICATION_ROOT',
      'SESSION_COOKIE_NAME',
      'SESSION_COOKIE_DOMAIN',
      'SESSION_COOKIE_PATH',
      'SESSION_COOKIE_HTTPONLY',
      'SESSION_COOKIE_SECURE',
      'SESSION_COOKIE_SAMESITE',
      'SESSION_REFRESH_EACH_REQUEST',
      'MAX_CONTENT_LENGTH',
      'SEND_FILE_MAX_AGE_DEFAULT',
      'TRAP_BAD_REQUEST_ERRORS',
      'TRAP_HTTP_EXCEPTIONS',
      'EXPLAIN_TEMPLATE_LOADING',
      'PREFERRED_URL_SCHEME',
      'TEMPLATES_AUTO_RELOAD',
      'MAX_COOKIE_SIZE',
      'AIMS_UI_PAGES_LOCATION',
      'ALL_PAGE_NAMES',
      'API_AUTH_TYPE',
      'API_BSC_AUTH_PASSWORD',
      'API_BSC_AUTH_USERNAME',
      'API_JWT_TOKEN',
      'API_JWT_TOKEN_BEARER',
      'API_JWT_K_VALUE',
      'BM_API_URL',
      'BM_JWT_TOKEN',
      'BM_JWT_TOKEN_BEARER',
      'BM_MAX_JOBS',
      'DEFAULT_BULK_LIMITS',
      'DEFAULT_CLASSIFICATION_CLASS_LIST',
      'DEFAULT_EPOCH_OPTIONS',
      'DEFAULT_EPOCH_SELECTED',
      'JSONIFY_PRETTYPRINT_REGULAR',
      'PROJECT_DOMAIN',
      'USER_AUTHS',
      'USER_GROUPS',
      'FLASK_ENV',
      'UI_EXPOSED_PORT',
  ]

  # Get the actual config keys
  conf_keys = get_base_config_dict().keys()

  # Check every single expected key is present
  for key in conf_keys:
    assert key in keys_that_should_be_present
