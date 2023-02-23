import os
from . import app
from .models.get_endpoints import get_endpoints
from flask import (
    render_template,
    request,
    redirect,
    session,
    url_for,
)

page_name = 'logout'


@app.route('/logout', methods=['GET', 'POST'])
def logout():
  session.clear()  # invalidate the user's session (logging them out)

  return redirect('https://accounts.google.com/logout')
