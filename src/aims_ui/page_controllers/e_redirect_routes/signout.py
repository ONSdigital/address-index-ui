from aims_ui import app
from flask import redirect, session

page_name = 'logout'


@app.route('/logout', methods=['GET', 'POST'])
def logout():
  session.clear()  # invalidate the user's session (logging them out)

  return redirect('https://accounts.google.com/logout')
