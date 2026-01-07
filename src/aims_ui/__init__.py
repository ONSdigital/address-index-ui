import os
import time

from flask import Flask
from .config import base as config_base
from aims_ui.app_helpers.logging import setup_logging

setup_logging(os.getenv('PLATFORM'))

app = Flask(__name__, instance_relative_config=False)

ENV = os.getenv('FLASK_ENV', 'testing')

app.config.from_object(config_base)

if ENV == 'development':
  from .config import dev as config_env
elif ENV == 'testing':
  from .config import test as config_env
elif ENV == 'production':
  from .config import prod as config_env
else:
  raise RuntimeError('invalid environment ' + str(ENV))

app.config.from_object(config_env)

try:
  os.makedirs(app.instance_path)
except OSError:
  pass

classifications = None


def get_classifications_cached():
  global start_time, classifications, last_pop_time
  if classifications is None:
    # Populate classifications list at start of program
    last_pop_time = time.time()
    classifications = get_classifications()
    return classifications
  else:
    current_time = time.time()
    time_since_last_population = current_time - last_pop_time
    # More than 60 seconds since last API population of classifications
    if time_since_last_population > 60:
      classifications = get_classifications()
      last_pop_time = time.time()
      return classifications
    else:
      # Use previously cached results
      return classifications


# Must import here to avoid circular imports
from aims_ui.page_helpers.api.api_interaction import get_epoch_options

epoch_options = None


def get_epoch_options_cached():
  global epoch_start_time, epoch_options, default_epoch, epoch_last_pop_time
  if epoch_options is None:
    # Populate epoch options list at start of program
    epoch_last_pop_time = time.time()
    epoch_options, default_epoch = get_epoch_options()
    return epoch_options, default_epoch
  else:
    epoch_current_time = time.time()
    epoch_time_since_last_population = epoch_current_time - epoch_last_pop_time
    # More than 120 seconds since last epoch sync
    if epoch_time_since_last_population > 60:
      epoch_options, default_epoch = get_epoch_options()
      epoch_last_pop_time = time.time()
      return epoch_options, default_epoch
    else:
      # Use previously cached results
      return epoch_options, default_epoch


# Setup headers for all requests to Flaskapp
@app.after_request
def add_header(response):
  # Cache Security Headers
  response.headers['Cache-Control'] = 'no-store'
  response.headers['Pragma'] = 'no-cache'
  response.headers['X-Frame-Options'] = 'DENY'

  return response


# Setup 'misc_functionality' page controllers
from aims_ui.page_controllers.d_misc_functionality.page_info import info
from aims_ui.page_controllers.d_misc_functionality.page_settings import settings
from aims_ui.page_controllers.d_misc_functionality.download_handler import download_handler
from aims_ui.page_controllers.d_misc_functionality.page_custom_response import custom_response

# Setup routes that immedaitely redirect elsewhere
from aims_ui.page_controllers.e_redirect_routes.login import login
from aims_ui.page_controllers.e_redirect_routes.signout import logout

# Setup 'single_matches' page controllers
from aims_ui.page_controllers.a_single_matches.page_uprn import uprn
from aims_ui.page_controllers.a_single_matches.page_postcode import postcode
from aims_ui.page_controllers.a_single_matches.page_typeahead import typeahead
from aims_ui.page_controllers.a_single_matches.page_singlesearch import singlesearch
from aims_ui.page_controllers.a_single_matches.page_radiussearch import radiussearch

# Setup 'multiple_matches' page controllers
from aims_ui.page_controllers.b_multiple_matches.page_multiple_address import multiple_address
from aims_ui.page_controllers.b_multiple_matches.page_multiple_address_results import multiple_address_results
from aims_ui.page_controllers.b_multiple_matches.page_multiple_address_original import multiple_address_original
from aims_ui.page_controllers.b_multiple_matches.page_multiple_address_attributes import multiple_address_attributes
from aims_ui.page_controllers.b_multiple_matches.page_uprn_multiple_match import uprn_multiple_match

# Setup 'help' page controller
from aims_ui.page_controllers.c_help_pages.page_help import help

# Setup standalone pages (in root directory)
from aims_ui.page_address_info import address_info

# Import classifications here to avoid circular import
from aims_ui.page_helpers.api.api_interaction import get_classifications

# Setup API forwarding routes used to bypass crossorigin issues
from aims_ui.api_access.routes.uprn_route import uprn_route
