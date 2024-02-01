from . import app
import logging
from flask import render_template, request, session, url_for
from flask_login import login_required
from .models.get_endpoints import get_endpoints

page_name = 'custom_response'


@login_required
@app.route('/custom_response')
def page_custom_response():
  # Custom Response Page, allows a user to build or deffine custom requests

  return (render_template(
      'custom_response.html',
      endpoints=get_endpoints(called_from=page_name),
  ))


