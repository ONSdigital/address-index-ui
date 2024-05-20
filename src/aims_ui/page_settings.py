from . import app
from flask import render_template
from flask_login import login_required
from .models.get_endpoints import get_endpoints
from .security_utils import check_user_has_access_to_page

page_name = 'settings'
pages_location = app.config.get('AIMS_UI_PAGES_LOCATION', '')


@login_required
@app.route('/settings')
def settings():
  endpoints = get_endpoints(called_from=page_name)
  access = check_user_has_access_to_page(page_name, endpoints)
  if access != True:
    return access

  col_options = [{'value': x, 'text': x} for x in range(1, 8)]
  col_options_inc0 = [{'value': x, 'text': x} for x in range(0, 6)]

  return render_template(
    f'{pages_location}{page_name}.html',
    endpoints=endpoints,
    col_options=col_options,
    col_options_inc0=col_options_inc0)
