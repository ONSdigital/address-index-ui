from flask import redirect, url_for

from aims_ui import app


# Keep this for backwards compatibility!
# Users who've bookmarked "/login" need to be redirected
@app.route('/login', methods=['GET', 'POST'])
def login():
  return redirect(url_for('singlesearch').replace('http', 'https', 1))
