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

  # Redirect user to the homepage
  return render_template(
      'logout.html',
      endpoints=get_endpoints(called_from=page_name),
  )
  # Optional return to homepage for testing
  return redirect(url_for('singlesearch').replace('http', 'https', 1))
