from .info import info

def setup_routes(app):
  @app.route('/info')
  def x():
    return info()

