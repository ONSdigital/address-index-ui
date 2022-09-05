import os
from flask_login import login_required
from flask import render_template, request, session, send_file, url_for
from . import app
from .models.get_endpoints import get_endpoints
from .api_interaction import api
import json
import csv

page_name = 'multiple_address_results'


@login_required
@app.route(f'/multiple_address_results', methods=['GET', 'POST'])
def multiple_address_results():
  endpoints = get_endpoints(called_from=page_name)

  for endpoint in endpoints:
    endpoint.current_selected_endpoint = url_for(page_name)

  return render_template(
      f'{page_name}.html',
      endpoints=endpoints,
  )

