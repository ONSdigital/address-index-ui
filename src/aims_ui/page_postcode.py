import os
from . import app
from flask import render_template, request
from flask_login import login_required
from .models.get_endpoints import get_endpoints
from .models.get_fields import get_fields


@login_required
@app.route('/postcode', methods=['GET', 'POST'])
def postcode():

  if request.method == 'POST':
    print(request)

  return render_template('postcode.html',
                         endpoints=get_endpoints(),
                         searchable_fields=get_fields('postcode'))
