from . import app
from flask import render_template
from flask_login import login_required
from .models.get_endpoints import get_endpoints


@login_required
@app.route('/settings')
def settings():
  col_options = [{'value': x, 'text': x} for x in range(1, 8)]
  col_options_inc0 = [{'value': x, 'text': x} for x in range(0, 6)]

  return render_template('settings.html',
                         endpoints=get_endpoints(),
                         col_options=col_options,
                         col_options_inc0=col_options_inc0)
